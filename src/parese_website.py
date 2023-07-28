# -*- coding: utf-8 -*-

"""リクエストサンプル

Webサイトのテーブルからデータを取得するサンプル

"""

import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Webサイトのフェッチ
url = "https://www.solxyz.co.jp/about/history/"
response = requests.get(url)

# パース
soup = BeautifulSoup(response.text, "html.parser")

# dlタグを抽出
dl = soup.find("dl")

# dtタグとddタグを抽出
data = []
for dt, dd in zip(dl.find_all("dt"), dl.find_all("dd")):
    data.append([dt.text, dd.text])

# pandasのDataFrameに変換
df = pd.DataFrame(data, columns=["year_month", "detail"])

# csvファイルに保存
dir_path = os.path.dirname(os.path.realpath(__file__))
df.to_csv(os.path.join(dir_path, "data/history.csv"), index=False, encoding="utf-8-sig")
