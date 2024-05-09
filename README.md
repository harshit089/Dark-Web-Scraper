# Dark-Web-Scraper

## Project Overview
This project features a comprehensive dark web crawler and search system built with Python and MongoDB. It is designed to autonomously navigate and collect data from specific onion sites, facilitating content analysis and user behavior studies within the dark web environment. The system includes both automatic and manual data extraction modes and provides robust search functionalities tailored to user-specified criteria.

## Features
- **Automatic and Manual Data Extraction:** Crawl dark web forums either automatically or based on user-defined settings.
- **Advanced Search Capabilities:** Search through collected data based on usernames, keywords, and specific date ranges.
- **Continuous Data Collection:** Utilizes multithreading to continuously collect data without user intervention.
- **Data Security and Anonymity:** Ensures secure and anonymous data collection through the Tor network.

## Technical Summary

### Programming Languages and Technologies
- **Python:** Primary programming language.
- **MongoDB:** Used for storing crawled data.
- **BeautifulSoup:** For parsing HTML content.
- **Multithreading:** To enhance the efficiency of data collection.
- **Dotenv:** For managing environment variables securely.
- **RequestsTor:** For making anonymized HTTP requests through Tor.

### Database Management
- Configured and managed MongoDB databases on MongoDB Atlas.
- Created collections to store thread headers and detailed post contents from dark web forums.

### Web Crawling and Data Parsing
- Implemented an autonomous crawler to navigate and fetch content from predefined dark web forums.
- Used BeautifulSoup for parsing HTML content to extract relevant data including user posts, metadata, and forum threads.

### Data Extraction
- Developed functions to manage user sessions on dark web forums, handling CSRF tokens and session cookies for authenticated requests.
- Systematic extraction and structuring of forum headers, post details, and user interactions.

### Search Functionality
- Responsive search interface for querying the MongoDB database.
- Integration of Texttable for formatted display of search results.

### User Interface and Interaction
- Interactive command-line interface (CLI) that guides users through search options.
- Functionality to save search results to text files for offline analysis.

### Multithreading and Automation
- Background threading for continuous web crawling.
- Scheduled updates to the database with the latest forum content.

### Error Handling and Network Resilience
- Comprehensive error handling to manage network issues and extraction anomalies.
- Retry mechanisms and logging to manage and record potential failures.

### Security and Anonymity
- Secure and anonymous connections to dark web resources via multiple Tor ports.

## Conclusion
This project effectively addresses the challenges associated with navigating and extracting data from the dark web. It provides a secure, efficient, and user-friendly system, making it an invaluable tool for researchers and analysts in fields such as cybersecurity, digital forensics, and online behavior analysis.

## Getting Started
To get a local copy up and running, follow these simple steps.

### Prerequisites
- Python 3.x
- MongoDB Atlas account
- Install dependencies: `pip install -r requirements.txt`

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/harshit089/Dark-Web-Scraper.git
