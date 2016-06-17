from bs4 import BeautifulSoup
import requests

soup = BeautifulSoup(requests.get("https://christopher.su").text)

# find by CSS class
soup.find_all("a", class_="nav")

# find by element id
soup.find_all(id='link2')
soup.find_all("p", id='link2')

# find by href contents
soup.find_all(href=re.compile("some_substring"))

if __name__ == '__main__':
  main()
