import requests
import pandas as pd
import time #載入定時函式庫
import os #載入作業系統函式庫
from io import StringIO
from bs4 import BeautifulSoup
import csv
 
# 抓取指定公司的財報資料

res = requests.get('https://mops.twse.com.tw/server-java/t13sa150_otc?&step=wh')
res.encoding = 'big5'

dfs = pd.read_html(StringIO(res.text))

path = os.path.join(os.getcwd(), 'data.html')
f = open(path, 'w+', encoding='utf8')
f.write(res.text)
f.close()

html = open(path, "r", encoding="utf8")
soup = BeautifulSoup(html, "html.parser")
table = soup.findAll("table")
rows = table[0].findAll("tr")
with open(os.path.join(os.getcwd(), 'data.csv'), "wt+", encoding='utf8', newline="") as f:
    writer = csv.writer(f)
    for row in rows:
        csv_row = []
        for cell in row.findAll(["td", "th"]):
            csv_row.append(cell.get_text())
        writer.writerow(csv_row)








