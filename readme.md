# Anime Download Scripts

Two Python scripts for downloading anime episodes from anime3rb.com. Choose between a Selenium-based or Playwright-based implementation.

## Scripts Overview

1. `animedownload_selenium.py`: Uses Selenium WebDriver
2. `animedownload_playwright.py`: Uses Playwright

## Requirements

### For Selenium Script (`animedownload_selenium.py`)
- Python 3.x
- selenium
- beautifulsoup4
- requests
- One of the following browsers and their corresponding WebDriver:
  - Firefox (geckodriver)
  - Chrome (chromedriver)
  - Edge (msedgedriver)

Install dependencies:
```bash
pip install selenium beautifulsoup4 requests
```

### For Playwright Script (`animedownload_playwright.py`)
- Python 3.x
- playwright
- beautifulsoup4

Install dependencies:
```bash
pip install playwright beautifulsoup4
python -m playwright install
```

## Usage

1. Run either script:
```bash
python animedownload_selenium.py
# or
python animedownload_playwright.py
```

2. Follow the prompts:
   - Enter download directory (first time only)
   - Choose your preferred browser
   - Enter anime name
   - Select the desired anime from the search results
   - Confirm to start downloading all episodes

The scripts will automatically:
- Create a directory for the anime
- Skip existing episodes
- Download the highest quality available
- Name files in format: `[anime-name]-ep[number].mp4`

## Note
Both scripts support Windows and Unix-based systems, automatically using the appropriate download method (PowerShell or wget) based on your operating system.
