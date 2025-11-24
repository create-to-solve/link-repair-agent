import requests
from storage.cache_manager import read_cached, write_cache
from config.settings import DEFAULT_SETTINGS

class Fetcher:
    def __init__(self, user_agent=None):
        self.settings = DEFAULT_SETTINGS
        self.user_agent = user_agent or self.settings.user_agent

    def fetch_html(self, url: str, use_cache=True):
        if use_cache:
            cached = read_cached(url)
            if cached:
                return cached
        headers = {"User-Agent": self.user_agent}
        timeout = (self.settings.connect_timeout, self.settings.read_timeout)
        for _ in range(self.settings.max_retries):
            try:
                r = requests.get(url, headers=headers, timeout=timeout)
                r.raise_for_status()
                html = r.text
                write_cache(url, html)
                return html
            except Exception:
                pass
        raise RuntimeError("Failed to fetch HTML")
