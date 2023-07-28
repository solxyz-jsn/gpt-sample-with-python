import os
import pandas as pd
import pytest
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "src"))
from parse_website import parse_website, save_to_csv


@pytest.fixture
def sample_csv_data():
    """
    csvテスト用のサンプルデータを作成する。

    """
    data = [
        ["2021年1月", "サンプルデータ1"],
        ["2021年2月", "サンプルデータ2"],
        ["2021年3月", "サンプルデータ3"],
    ]
    return pd.DataFrame(data, columns=["year_month", "detail"])


@pytest.fixture
def sample_web_data():
    """
    Webパーステスト用のサンプルデータを作成する。

    """
    data = [
        ["1981(昭和56)年2月", "受託ソフトウェア開発事業を目的に埼玉県大宮市にて株式会社エポックシステム設立"],
        ["1982(昭和57)年2月", "東京都港区新橋に本社を移転"],
        ["1984(昭和59)年12月", "東京都港区芝大門に本社を移転"],
    ]
    return pd.DataFrame(data, columns=["year_month", "detail"])


def test_parse_website(sample_web_data):
    """
    parse_website関数をテストする。

    """
    url = "https://www.solxyz.co.jp/about/history/"
    df = parse_website(url)
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
    assert "year_month" in df.columns
    assert "detail" in df.columns
    assert df.iloc[0]["year_month"] == sample_web_data.iloc[0]["year_month"]
    assert df.iloc[0]["detail"] == sample_web_data.iloc[0]["detail"]
    assert df.iloc[1]["year_month"] == sample_web_data.iloc[1]["year_month"]
    assert df.iloc[1]["detail"] == sample_web_data.iloc[1]["detail"]
    assert df.iloc[2]["year_month"] == sample_web_data.iloc[2]["year_month"]
    assert df.iloc[2]["detail"] == sample_web_data.iloc[2]["detail"]


def test_save_to_csv(sample_csv_data):
    """
    save_to_csv関数をテストする。

    Parameters
    ----------
    sample_data : pandas.DataFrame
        テスト用のサンプルデータ。

    """
    filename = "test.csv"
    save_to_csv(sample_csv_data, os.path.join("./test", filename))
    dir_path = os.path.join(os.getcwd(), "src/test")
    file_path = os.path.join(dir_path, filename)
    print(file_path)
    assert os.path.exists(file_path)
    df = pd.read_csv(file_path)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(sample_csv_data)
    assert all(df.columns == sample_csv_data.columns)
    os.remove(file_path)
