import requests
import pandas
from bs4 import BeautifulSoup

response = requests.get("https://www.rottentomatoes.com/search?search=horror+")
# print(response)
soup = BeautifulSoup(response.content,'html.parser')
# print(soup)

# names=[name.text[1:-1] for name in names]
names = soup.find_all('a',class_="unset")
[names.find('a') for name in names]
# names=[name.text[0:-2] for name in names]
# name=[]
# for i in names[0:50]:
#     d=i.get_text()
#     name.append(d)
print(names)


#bike images
images=soup.find_all('img',class_="sl-img clr")
image=[]
for i in images[0:10]:
    d=i['src']
    image.append(d)
# print(image)

#bike prices
prices=soup.find_all('div',class_="Rs. 3.30 Crore")
price=[]
for i in prices[0:12]:
    d=i.get_text()
    price.append(d)
# print(price)

#bike reviews
reviews=soup.find_all('p',class_="review-item__preview")
review=[]
for i in reviews[0:12]:
    d=i.get_text()
    review.append(d)
# print(review)    

#bike links
links=soup.find_all('a',class_="modelurl")
link=[]
for i in links[0:12]:
    d="https://www.bikewale.com/"+i['href']
    link.append(d)
# print(link)   

# data={'Names':pandas.Series(names),
#       'Images':pandas.Series(image),
#       'Reviews':pandas.Series(review),
#       'Links':pandas.Series(link)
#       }
# print(data)
# df=pandas.DataFrame(data)
# print(df).
# df.to_csv("Enfield_data.csv")











































