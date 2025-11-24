from dataclasses import dataclass

@dataclass
class Settings:
    user_agent: str = "LinkResolverAgent/0.1"
    request_timeout: float = 15.0
    max_retries: int = 3
    backoff_factor: float = 0.5
    connect_timeout: float = 5.0
    read_timeout: float = 10.0
    profile_samples: int = 100

DEFAULT_SETTINGS = Settings()
