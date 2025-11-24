from models.enums import FileType
from strategies.classifier import classify_link

def test_classify_link_by_extension():
    assert classify_link("x.csv") == FileType.CSV
    assert classify_link("x.xlsx") == FileType.XLSX
    assert classify_link("x.zip") == FileType.ZIP
    assert classify_link("x.html") == FileType.HTML
