def recommend_items(data, mood):
    return data[data['mood'] == mood]
