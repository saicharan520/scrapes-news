from flask import Flask, render_template, request, redirect
from scraper import scrape_verge
from models import init_db, insert_articles, get_articles, get_preferences, add_preference
from recommender import filter_articles

app = Flask(__name__)

@app.route('/')
def index():
    all_articles = get_articles()
    prefs = get_preferences()
    recommended = [{'title': a[0], 'link': a[1]} for a in all_articles]
    return render_template('index.html', articles=recommended, preferences=prefs)

@app.route('/scrape')
def scrape():
    articles = scrape_verge()
    print("Articles to insert:", articles[:5])  # Show first few
    insert_articles(articles)
    return redirect('/')


@app.route('/add_pref', methods=['POST'])
def add_pref():
    keyword = request.form['keyword']
    add_preference(keyword)
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
