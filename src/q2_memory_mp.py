import json
import re
from collections import defaultdict
from typing import List, Tuple
from memory_profiler import profile

@profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
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

    emoji_counts = defaultdict(int)

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                tweet = json.loads(line)
                content = tweet.get('content', '')
                emojis = emoji_pattern.findall(content)
                for emoji in emojis:
                    emoji_counts[emoji] += 1
            except json.JSONDecodeError:
                continue

    top_emojis = sorted(emoji_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    return top_emojis

file_path = "farmers-protest-tweets-2021-2-4.json"
q2_memory(file_path)