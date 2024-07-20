**Problem:**
Design a Flask application that scrapes data from a specific website, extracts the desired information, and displays it in a structured format.

**Flask Application Design:**

### HTML Files:

- **index.html**: The main page of the application. It should contain:
    - A form to enter the URL to be scraped.
    - A button to submit the form and initiate the scraping process.
- **results.html**: Displays the results of the scraping process. It should include:
    - A table or list to display the extracted data.
    - Navigation buttons to allow users to paginate through the results.

### Routes:

- **GET /**: Renders the `index.html` page.
- **POST /scrape**: Receives the submitted URL, performs the scraping process, and extracts the desired data. The extracted data is then passed to the `results.html` page for display.
- **GET /results**: If the user navigates to the results page directly, this route checks for any previously scraped data and renders the `results.html` page accordingly.
- **GET /results/<page_number>**: Handles pagination by rendering the `results.html` page with the specified page number.