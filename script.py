from bs4 import BeautifulSoup
from hanziconv import HanziConv
import json

f = open("surname.html", 'r')
# source file is from https://en.wikipedia.org/wiki/List_of_common_Chinese_surnames
html_doc = f.read()
f.close()

soup = BeautifulSoup(html_doc, 'html.parser')
count = 1
result = []

for item in soup.find_all('tr'):
    this_block = False
    temp_td = []

    for td in item.find_all('td'):
        if td.text == str(count) or this_block:
            temp_td.append(td.text)
            if this_block == False:
                count += 1
                this_block = True
        else:
            break
    
    if len(temp_td) > 0:
        t_dict = {
            "No." : temp_td[0],
            "Zh_sim": temp_td[1],
            "Zh_tra": HanziConv.toTraditional(temp_td[1]),
            "mainland": temp_td[2], 
            "hongkong": temp_td[3],
            "taiwan": temp_td[4],
            "macao": temp_td[5],
            "singapore": temp_td[6],
            "malaysia": temp_td[7],
            "vietname": temp_td[8],
            "Korea": temp_td[9]
        }
        result.append(t_dict)

with open('surname.json', 'w') as outfile:
    json.dump(result, outfile)


        
