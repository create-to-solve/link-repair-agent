from urllib.parse import urlparse
from models.enums import FileType

def classify_link(url: str, content_type=None):
    path = urlparse(url).path.lower()
    if path.endswith(".csv"):
        return FileType.CSV
    if path.endswith(".xlsx") or path.endswith(".xls"):
        return FileType.XLSX
    if path.endswith(".zip"):
        return FileType.ZIP
    if path.endswith(".html") or path.endswith(".htm"):
        return FileType.HTML
    return FileType.OTHER
