import hashlib
from pathlib import Path

DATA_DIR = Path("data")
CACHE_DIR = DATA_DIR / "cache"

def _hash_url(url: str) -> str:
    return hashlib.sha256(url.encode()).hexdigest()

def get_cache_path(url: str) -> Path:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    return CACHE_DIR / f"{_hash_url(url)}.html"

def read_cached(url: str):
    p = get_cache_path(url)
    return p.read_text() if p.exists() else None

def write_cache(url: str, content: str):
    p = get_cache_path(url)
    p.write_text(content)
