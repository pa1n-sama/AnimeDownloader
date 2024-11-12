
# Anime Downloader

A Python script to search and bulk download anime episodes from `anime3rb.com`.

## Requirements

- **Python 3**
- **Packages**: `selenium`, `BeautifulSoup4`, `requests`
- **Geckodriver** (for Chrome WebDriver)

Install dependencies with:
```bash
pip install selenium beautifulsoup4 requests
```

## Usage

1. Make the script executable:
   ```bash
   chmod +x anime_downloader.py
   ```

2. Run the script:
   ```bash
   ./anime_downloader.py
   ```

3. Enter the anime name when prompted.
4. Select the anime from the list.
5. Confirm to download all episodes.

Episodes will be saved to:
```
/home/pain/Downloads/Videos/<anime_name>
```
