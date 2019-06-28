import googlesearch
import webbrowser
import sys

query = sys.argv[1]

print(query)

test = query +  " site:sec.gov"
print(test)
for url in googlesearch.search(test, stop=5):
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
