import googlesearch
import webbrowser
import sys

site_type = sys.argv[1]
query = sys.argv[2]


site_types = {"health": ["sec.gov", 'healthcare.gov'],
            "example": ["yahoo.com"]
        }

for item in site_types[site_type]:
    for url in googlesearch.search(item + query, stop=5):
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)