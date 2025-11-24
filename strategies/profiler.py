from io import StringIO
import requests
from config.settings import DEFAULT_SETTINGS
from models.enums import FileType

def profile_file(url: str, file_type: FileType):
    if file_type is not FileType.CSV:
        return {}
    try:
        r = requests.get(url, timeout=(5, 10), stream=True)
        r.raise_for_status()
        lines = []
        for i, line in enumerate(r.iter_lines(decode_unicode=True)):
            if i > 200:
                break
            lines.append(line)
        import pandas as pd
        df = pd.read_csv(StringIO("\n".join(lines)), nrows=DEFAULT_SETTINGS.profile_samples)
        return {"columns_sample": list(df.columns)}
    except Exception:
        return {}
