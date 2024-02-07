import requests
from bs4 import BeautifulSoup

content = requests.get("https://www.python.org/jobs/")
html = content.text
website = BeautifulSoup(html,"html.parser")

movies = website.find("ol",{"class":"list-recent-jobs list-row-container menu"})

li = movies.find("li").find("h2")
cat = movies.find("li")

company_name = li.find("span",{"class":"listing-company-name"})
location = li.find("span",{"class":"listing-location"})
allcategory = cat.find("span",{"class":"listing-company-category"})

link = company_name.find("a")
name = company_name.text
where = location.find("a")
category = allcategory.find("a")

# for i in range(10):
#     i = movies.find_next("li")
#     link = i.find("span",{"class":"listing-company-name"}).find("a")
#     name = i.find("span",{"class":"listing-company-name"}).text
#     where = i.find("span",{"class":"listing-location"}).find("a")
#     category = i.find("span",{"class":"listing-company-category"}).find("a")

# i3 = i2.find("div")
# i4 = i3.find("div",{"class": "bloko-header-section-3"})
# i5 = i3.find("div",{"class":"vacancy-serp__vacancy-compensation"})
# i6 = i2.find("class",{"vacancy-serp-item-company"})
# i4,i5,i6

# найти  <tbody class="lister-list">

# HTML = movies.prettify() 
# with open("index.txt","w",encoding="utf-8") as file:
#     file.write(HTML)
