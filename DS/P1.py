result = wp.page("Computer Science") 
fnal_result = result.content 
print(final_result) 

def plot_wordcloud(wc): 
    plt.axis("off") 
    plt.figure(figsize=(10, 10)) 
    plt.imshow(wc) 
    plt.show() 

# Generate word cloud
wc = WordCloud(width=500, heigt=500, backgroud_color="cyan", random_state=10, stopwords=STOPWORDS).generate(final_result) 
wc.to_file("ds.png") 
plot_wordcloud(wc)
    
#PRAC 2 WEB SCRAPING 
import pandas as pd
frm bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https"
page = urlopen(url)
htl_page = page.read().decode("utf-8")
soup = BeautifulSoup(html_page, "html.parser")
table = soup.find("table")