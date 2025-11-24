from strategies.selector import choose_best_link
from models.enums import FileType

def test_choose_best_link_prioritises_csv():
    links = ["x.html", "x.xlsx", "x.csv"]
    best, ftype = choose_best_link(links)
    assert ftype == FileType.CSV
