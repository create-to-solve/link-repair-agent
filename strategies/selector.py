from models.enums import FileType
from strategies.classifier import classify_link

_PRIORITY = [FileType.CSV, FileType.XLSX, FileType.ZIP, FileType.OTHER, FileType.HTML]

def rank_links(links):
    scored = [(link, classify_link(link)) for link in links]
    scored.sort(key=lambda x: _PRIORITY.index(x[1]))
    return scored

def choose_best_link(links):
    ranked = rank_links(links)
    return ranked[0] if ranked else None
