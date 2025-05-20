def filter_articles(articles, keywords):
    recommended = []
    for title, link in articles:
        if any(kw.lower() in title.lower() for kw in keywords):
            recommended.append({'title': title, 'link': link})
    return recommended
