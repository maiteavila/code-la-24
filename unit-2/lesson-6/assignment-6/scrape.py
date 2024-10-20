# import the requests library
import requests

# import beautifulsoup
from bs4 import BeautifulSoup

kamala_response = requests.get("https://kamalaharris.com/")
trump_response = requests.get("https://www.donaldjtrump.com/")

# print(response.text[:500])

kamala_soup_html = BeautifulSoup(kamala_response.text, "html.parser")
trump_soup_html = BeautifulSoup(trump_response.text, "html.parser")

kamala_soup_text = kamala_soup_html.get_text()
trump_soup_text = trump_soup_html.get_text()

kamala_data = open('kamala.txt', 'w')
kamala_data.write(kamala_soup_text)
kamala_data.close()

trump_data = open('trump.txt', 'w')
trump_data.write(trump_soup_text)
trump_data.close()


def getTitles(soupdata):  
  titles = soupdata.select("h2")
  if titles:
    for t in titles:
      print(t.text)
      
print("KAMALA........")
getTitles(kamala_soup_html)
print("TRUMP.........")
getTitles(trump_soup_html)