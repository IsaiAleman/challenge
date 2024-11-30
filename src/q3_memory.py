import json
import re
from collections import defaultdict
from typing import List, Tuple

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    mention_pattern = re.compile(r'@(\w+)')

    mention_counts = defaultdict(int)

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                tweet = json.loads(line)
                content = tweet.get('content', '')
                mentions = mention_pattern.findall(content)
                for username in mentions:
                    mention_counts[username] += 1
            except json.JSONDecodeError:
                continue 

    top_mentions = sorted(mention_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    return top_mentions