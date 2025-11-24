from enum import Enum

class FileType(str, Enum):
    CSV = "csv"
    XLSX = "xlsx"
    ZIP = "zip"
    HTML = "html"
    OTHER = "other"

class SourceStatus(str, Enum):
    PENDING = "pending"
    RESOLVED = "resolved"
    FAILED = "failed"
