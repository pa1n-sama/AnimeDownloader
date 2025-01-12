# Anime Downloader

A collection of two Python scripts for downloading anime episodes from anime3rb.com.

## Scripts Overview

1. `selenium_downloader.py`: Uses Selenium WebDriver for browser automation
2. `playwright_downloader.py`: Uses Playwright for browser automation

## Prerequisites

### For Selenium Script (`selenium_downloader.py`)
```bash
pip install selenium beautifulsoup4 requests
```

Additionally, you need to install one of these browsers and their corresponding WebDrivers:
- Firefox (geckodriver)
- Chrome (chromedriver)
- Edge (msedgedriver)

### For Playwright Script (`playwright_downloader.py`)
```bash
pip install playwright beautifulsoup4
playwright install
```

## Usage

### Selenium Script
1. Run the script:
   ```bash
   python selenium_downloader.py
   ```
2. Choose your preferred browser (Firefox/Chrome/Edge)
3. Enter the download directory path (first time only)
4. Enter the anime name
5. Select the anime from the search results
6. Confirm the download

### Playwright Script
1. Run the script:
   ```bash
   python playwright_downloader.py
   ```
2. Choose your preferred browser (Chromium/Firefox/WebKit)
3. Enter the download directory path (first time only)
4. Enter the anime name
5. Select the anime from the search results
6. Confirm the download

## Features
- Automatic episode downloading
- Multiple browser support
- Highest quality selection
- Resume capability (skips already downloaded episodes)
- Cross-platform support (Windows and Unix-based systems)

## Note
Make sure you have sufficient storage space and a stable internet connection. The scripts will create a directory for each anime and save episodes with proper naming conventions.
