import requests
from bs4 import BeautifulSoup
word=input("Enter the word=")
gsearch="https://www.google.com/search?q=" + word
r=requests.get(gsearch)
soup=BeautifulSoup(r.text,"html.parser")
soup.find('cite')
s = soup.findAll()
print(s)