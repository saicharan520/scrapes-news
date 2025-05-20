import sqlite3

def init_db():
    conn = sqlite3.connect("news.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS articles (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    link TEXT
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS preferences (
                    id INTEGER PRIMARY KEY,
                    keyword TEXT
                )''')
    conn.commit()
    conn.close()

def insert_articles(articles):
    conn = sqlite3.connect("news.db")
    c = conn.cursor()
    for article in articles:
        c.execute("INSERT INTO articles (title, link) VALUES (?, ?)", (article['title'], article['link']))
    conn.commit()
    conn.close()

def get_articles():
    conn = sqlite3.connect("news.db")
    c = conn.cursor()
    c.execute("SELECT title, link FROM articles")
    articles = c.fetchall()
    conn.close()
    return articles

def get_preferences():
    conn = sqlite3.connect("news.db")
    c = conn.cursor()
    c.execute("SELECT keyword FROM preferences")
    keywords = [row[0] for row in c.fetchall()]
    conn.close()
    return keywords

def add_preference(keyword):
    conn = sqlite3.connect("news.db")
    c = conn.cursor()
    c.execute("INSERT INTO preferences (keyword) VALUES (?)", (keyword,))
    conn.commit()
    conn.close()
