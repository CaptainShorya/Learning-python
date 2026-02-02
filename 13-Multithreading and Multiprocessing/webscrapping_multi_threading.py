'''
Real-World Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping
Web scraping often involves making numerous network requests to 
fetch web pages. These tasks are I/O-bound because they spend a lot of
time waiting for responses from servers. Multithreading can significantly
improve the performance by allowing multiple web pages to be fetched concurrently.
'''

'''
bs4 -> Beautiful soup used for web scrapping any url
https://python.langchain.com/v0.2/docs/introduction/

https://docs.langchain.com/oss/python/langchain/middleware/overview

https://docs.langchain.com/oss/python/langchain/tools
'''
## WebScarping -> Automatically fetching data from websites and extracting useful information from their HTML pages using a program.
import threading # allows running multiple tasks concurrently
import requests # sends HTTP requests to websites
from bs4 import BeautifulSoup # parses HTML and extracts data

urls=[
'https://python.langchain.com/v0.2/docs/introduction/',

'https://docs.langchain.com/oss/python/langchain/middleware/overview',

'https://docs.langchain.com/oss/python/langchain/tools'

]

def fetch_content(url):
    response=requests.get(url) #Sends an HTTP GET request to the website,Server responds with page data (HTML)
    soup=BeautifulSoup(response.content,'html.parser') # Converts raw HTML into a parseable object.
    print(f'Fetched {len(soup.text)} characters from {url}') #soup.text → extracts all visible text from the page

threads=[] #keeps track of all created threads, Needed later to wait for their completion

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,)) # args=(url,) → arguments passed to the function(comma is required to make it a tuple)
    threads.append(thread) # Stores the thread for later use
    thread.start()
    # Multiple URLs are fetched at the same time

## Waiting for all threads to finish
for thread in threads:
    thread.join() #join() blocks the main program, Waits until all threads complete

print("All web pages fetched")

## -r means It tells pip : "Read package names from this file and install them.""