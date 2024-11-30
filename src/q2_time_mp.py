import pandas as pd
import re
import orjson
from typing import List, Tuple
from memory_profiler import profile

@profile
def q2_time(file_path: str) -> List[Tuple[str, int]]:
    data = []
    with open(file_path, 'rb') as f:
        for line in f:
            tweet = orjson.loads(line)
            data.append({
                'content': tweet['content'],
            })

    df = pd.DataFrame(data)

    contents = df['content']

    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F300-\U0001F5FF"  # Symbols & Pictographs
        "\U0001F680-\U0001F6FF"  # Transport & Map Symbols
        "\U0001F1E0-\U0001F1FF"  # Flags
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE
    )

    def extract_emojis(text):
        return emoji_pattern.findall(text)

    df['emojis'] = contents.apply(extract_emojis)

    emojis_series = df['emojis'].explode()

    emojis_series = emojis_series.dropna()

    emoji_counts = emojis_series.value_counts()

    top_emojis = emoji_counts.head(10)

    result = list(top_emojis.items())

    return result

file_path = "farmers-protest-tweets-2021-2-4.json"
q2_time(file_path)