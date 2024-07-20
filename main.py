
# Flask Application Design:

# HTML Files:
# index.html: Main page with form to enter URL and submit
# results.html: Displays the results of the scraping process

# Routes:
# GET /: Renders index.html
# POST /scrape: Receives the submitted URL, performs scraping, and redirects to /results
# GET /results: If the user navigates to the results page directly, this route checks for any previously scraped data and renders results.html accordingly
# GET /results/<page_number>: Handles pagination by rendering results.html with the specified page number

from flask import Flask, render_template, request, redirect, url_for
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# Global variable to store the scraped data
scraped_data = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    # Get the URL from the form
    url = request.form['url']
    
    # Perform scraping using BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the desired data
    for item in soup.find_all('div', class_='item'):
        title = item.find('h3').text
        price = item.find('span', class_='price').text
        scraped_data.append((title, price))
    
    # Redirect to the results page
    return redirect(url_for('results'))

@app.route('/results')
def results():
    # Check if there is any scraped data
    if not scraped_data:
        return render_template('results.html', message="No data scraped yet. Please scrape data first.")
    
    # Paginate the results
    page = request.args.get('page', 1, type=int)
    per_page = 10
    paginated_data = scraped_data[(page - 1) * per_page:page * per_page]
    
    return render_template('results.html', data=paginated_data, page=page, total_pages=len(scraped_data) // per_page + 1)

if __name__ == '__main__':
    app.run()
