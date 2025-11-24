from strategies.parser import extract_links

def test_extract_links_basic():
    html = '''
    <a href="https://example.org/file.csv">CSV</a>
    <a href="https://example.org/page.html">HTML</a>
    <a href="https://example.org/file.csv">Duplicate</a>
    '''
    links = extract_links(html)
    assert len(links) == 2
    assert "https://example.org/file.csv" in links
