import pandas as pd
import datetime
from typing import List, Tuple
from memory_profiler import profile

@profile
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Read the NDJSON file into a pandas DataFrame
    df = pd.read_json(file_path, lines=True, encoding='utf-8')
    
    df['date'] = pd.to_datetime(df['date']).dt.date
    
    df['username'] = df['user'].apply(lambda x: x['username'])
    
    top_dates = df['date'].value_counts().nlargest(10).index.tolist()
    
    result = []
    for date in top_dates:
        df_date = df[df['date'] == date]
        top_user = df_date['username'].value_counts().idxmax()
        result.append((date, top_user))
    
    return result
    
file_path = "farmers-protest-tweets-2021-2-4.json"
q1_time(file_path)
