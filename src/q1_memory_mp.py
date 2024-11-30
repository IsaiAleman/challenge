from typing import List, Tuple
from datetime import datetime
from memory_profiler import profile

@profile
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    import json
    from collections import defaultdict
    import datetime

    date_counts = defaultdict(int)
    user_counts_per_date = defaultdict(lambda: defaultdict(int))

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            date_str = tweet['date'][:10]
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            username = tweet['user']['username']

            date_counts[date] += 1
            user_counts_per_date[date][username] += 1

    top_dates = sorted(date_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    result = []
    for date, _ in top_dates:
        user_counts = user_counts_per_date[date]
        top_user = max(user_counts.items(), key=lambda x: x[1])[0]
        result.append((date, top_user))

    return result

file_path = "farmers-protest-tweets-2021-2-4.json"
q1_memory(file_path)