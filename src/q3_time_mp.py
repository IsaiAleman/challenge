import pandas as pd
import orjson
import re
from typing import List, Tuple
from memory_profiler import profile

@profile
def q3_time(file_path: str) -> List[Tuple[str, int]]:
    data = []
    with open(file_path, 'rb') as f:
        for line in f:
            tweet = orjson.loads(line)
            data.append({
                'content': tweet['content'],
            })

    df = pd.DataFrame(data)

    contents = df['content']

    mention_pattern = re.compile(r'@(\w+)')

    def extract_mentions(text):
        return mention_pattern.findall(text)

    df['mentions'] = contents.apply(extract_mentions)

    mentions_series = df['mentions'].explode()
    mentions_series = mentions_series.dropna()
    mention_counts = mentions_series.value_counts()
    top_mentions = mention_counts.head(10)

    result = list(top_mentions.items())

    return result

file_path = "farmers-protest-tweets-2021-2-4.json"
q3_time(file_path)