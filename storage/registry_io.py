import json
from datetime import datetime
from pathlib import Path
from models.registry_models import RawSource, ResolvedSource

REGISTRY_DIR = Path("registry")
RAW_SOURCES_PATH = REGISTRY_DIR / "raw_sources.yaml"
RESOLVED_SOURCES_PATH = REGISTRY_DIR / "resolved_sources.jsonl"

def load_raw_sources():
    import yaml
    with RAW_SOURCES_PATH.open("r") as f:
        data = yaml.safe_load(f) or {}
    return [RawSource(**ds) for ds in data.get("datasets", [])]

def append_resolved_source(resolved: ResolvedSource):
    line = resolved.model_dump()
    if isinstance(line.get("scanned_at"), datetime):
        line["scanned_at"] = line["scanned_at"].isoformat()
    with RESOLVED_SOURCES_PATH.open("a") as f:
        f.write(json.dumps(line) + "\n")

def iter_resolved_sources():
    if not RESOLVED_SOURCES_PATH.exists():
        return []
    with RESOLVED_SOURCES_PATH.open("r") as f:
        for line in f:
            if not line.strip():
                continue
            data = json.loads(line)
            if "scanned_at" in data:
                data["scanned_at"] = datetime.fromisoformat(data["scanned_at"])
            yield ResolvedSource(**data)
