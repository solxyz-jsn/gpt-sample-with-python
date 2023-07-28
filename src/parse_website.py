# -*- coding: utf-8 -*-

"""リクエストサンプル

Webサイトのテーブルからデータを取得するサンプル

"""

import os
import requests
from bs4 import BeautifulSoup
import pandas as pd


def parse_website(url):
    """
    Webサイトのテーブルをパースしてデータを抽出する。

    Parameters
    ----------
    url : str
        パースするWebサイトのURL。

    Returns
    -------
    pandas.DataFrame
        抽出したデータを含むDataFrame。

    """
    # Webサイトのフェッチ
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

    return df


def save_to_csv(df, filename):
    """
    DataFrameをCSVファイルに保存する。

    Parameters
    ----------
    df : pandas.DataFrame
        保存するDataFrame。
    filename : str
        保存するファイル名。

    """
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        df.to_csv(os.path.join(dir_path, filename), index=False, encoding="utf-8-sig")
        print(f"CSVファイル '{filename}' を保存しました。")
    except Exception as e:
        print(f"CSVファイル '{filename}' の保存に失敗しました。エラー: {e}")


def main():
    """
    WebサイトをパースしてデータをCSVファイルに保存する。
    """
    url = "https://www.solxyz.co.jp/about/history/"
    df = parse_website(url)

    # CSVファイルに保存
    save_to_csv(df, "data/history.csv")


if __name__ == "__main__":
    main()
