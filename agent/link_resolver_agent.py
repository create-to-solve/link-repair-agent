from datetime import datetime
from models.enums import FileType, SourceStatus
from storage.registry_io import load_raw_sources, append_resolved_source
from strategies.fetcher import Fetcher
from strategies.parser import extract_links
from strategies.selector import choose_best_link
from strategies.profiler import profile_file
from models.registry_models import ResolvedSource

class LinkResolverAgent:
    def __init__(self, fetcher=None):
        self.fetcher = fetcher or Fetcher()

    def resolve_one(self, raw):
        html = self.fetcher.fetch_html(str(raw.landing_url))
        links = extract_links(html)
        best = choose_best_link(links)
        if not best:
            return ResolvedSource(
                dataset_id=raw.id,
                file_url=raw.landing_url,
                file_type=FileType.HTML,
                status=SourceStatus.FAILED,
                scanned_at=datetime.utcnow(),
                valid=False,
            )
        url, ftype = best
        profile = profile_file(url, ftype)
        return ResolvedSource(
            dataset_id=raw.id,
            file_url=url,
            file_type=ftype,
            status=SourceStatus.RESOLVED,
            scanned_at=datetime.utcnow(),
            valid=True,
            columns_sample=profile.get("columns_sample"),
            extra_metadata=profile,
        )

    def run(self):
        for raw in load_raw_sources():
            try:
                resolved = self.resolve_one(raw)
                append_resolved_source(resolved)
            except Exception as e:
                append_resolved_source(ResolvedSource(
                    dataset_id=raw.id,
                    file_url=raw.landing_url,
                    file_type=FileType.HTML,
                    status=SourceStatus.FAILED,
                    scanned_at=datetime.utcnow(),
                    valid=False,
                    extra_metadata={"exception": repr(e)},
                ))
