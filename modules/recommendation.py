import pandas as pd
def recommend_items(data, mood):
    recommendations = data[data['mood'] == mood]

    return recommendations.sample(n=min(5, len(recommendations))) if not recommendations.empty else pd.DataFrame()

