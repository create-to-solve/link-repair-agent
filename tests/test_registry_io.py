from pathlib import Path
from models.registry_models import ResolvedSource
from models.enums import FileType, SourceStatus
from storage.registry_io import append_resolved_source, iter_resolved_sources
from datetime import datetime

def test_append_and_iter_resolved_sources(tmp_path, monkeypatch):
    import storage.registry_io as rio

    reg = tmp_path / "registry"
    reg.mkdir()
    out = reg / "resolved_sources.jsonl"

    monkeypatch.setattr(rio, "RESOLVED_SOURCES_PATH", out)
    monkeypatch.setattr(rio, "REGISTRY_DIR", reg)

    rec = ResolvedSource(
        dataset_id="test",
        file_url="https://example.org/d.csv",
        file_type=FileType.CSV,
        status=SourceStatus.RESOLVED,
        scanned_at=datetime.utcnow(),
        valid=True,
    )

    append_resolved_source(rec)
    items = list(iter_resolved_sources())
    assert len(items) == 1
