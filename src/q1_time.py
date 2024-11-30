import pandas as pd
import orjson
from datetime import datetime
from typing import List, Tuple

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    data = []
    with open(file_path, 'rb') as f:
        for line in f:
            tweet = orjson.loads(line)
            data.append({
                'date': tweet['date'],
                'username': tweet['user']['username']
            })

    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date']).dt.date

    date_counts = df['date'].value_counts()
    top_dates = date_counts.nlargest(10).index

    df_top_dates = df[df['date'].isin(top_dates)]
    user_date_counts = df_top_dates.groupby(['date', 'username']).size().reset_index(name='counts')

    idx = user_date_counts.groupby('date')['counts'].idxmax()
    top_users = user_date_counts.loc[idx]

    result = list(zip(top_users['date'], top_users['username']))

    return result