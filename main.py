import requests
from bs4 import BeautifulSoup
from functions import parse_table
import pandas as pd



url = 'https://dominos.by/'
res = requests.get(url)  # подключаюсь по указанному урлу

soup = BeautifulSoup(res.text, "html.parser")
table = soup.find('div', {'class': 'product-grid__content'})

result = pd.DataFrame()

for item in table:
    parse = parse_table(item)
    result = result.append(parse, ignore_index=True)

result.to_excel('res.xlsx')

# .find('table') - ищет первое вхождение элемента в тексте
# .find_all('table') - ищет ВСЕ вхождения элемента в тексте
# find('table').text - возврат текста, который находится в объекте
# find('table').get('href') - вернет ссылки




#with open('test.html', 'w') as f:
    # открываю файл test.html в режиме записи (write)
#    f.write(res.text)  # И записываю в него ответ от сайта