import requests
import pandas
from bs4 import BeautifulSoup

response=requests.get("https://quotes.toscrape.com/")
# print(response)
soup=BeautifulSoup(response.content,'html.parser')
# print(soup)
# quotes=soup.find('span',class_='text')
# quote=[]
# for i in quotes:
#     d=i.get_text()
#     quote.append(d)
# print((quote))

# quote=soup.find('span',class_='text')
# quote.text
# print(quote.getText)
quotes=soup.find_all('span',class_='text')
#''is remove for using [1:-1]
quotes=[quote.text[1:-1] for quote in quotes]
# print(quotes)



authors=soup.find_all('small',class_='author')
authors=[author.text for author in authors]
# print(authors)

tags=soup.find_all('a',class_='tag')

tag=[]
for i in tags[0:10]:
    d=i.get_text()
    tag.append(d)
# print(tag)    
dataset={
    'quote':pandas.Series(quotes),
    'author':pandas.Series(authors),
    'tags':pandas.Series(tag)
}
df=pandas.DataFrame(dataset)
print(df)
df.to_csv("web2.csv")


























# for i in tags[0].find_all('a',class_='tag'):
#     print(i.text)
# total_tags=[]
# for i in range(len(tags)):
#     k=[]
#     for j in tags[i].find_all('div',class_='tags'):
#         k.append(j.text)
#     total_tags.append(','.join(k)) 
# print(total_tags)       










   













