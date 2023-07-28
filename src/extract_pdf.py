# -*- coding: utf-8 -*-

"""PDFからテキストを抽出

PDFからテキストを抽出する

"""

import PyPDF2
import os
import unicodedata


def to_full_width(s):
    """
    半角文字を全角文字に変換する
    Args:
        s (str): 半角文字を含む文字列
    Returns:
        str: 全角文字に変換された文字列
    """
    return "".join(
        c
        if unicodedata.east_asian_width(c) in "WF"
        else unicodedata.normalize("NFKC", c)
        for c in s
    )


# PDFファイルのパス
dir_path = os.path.dirname(os.path.realpath(__file__))
pdf_path = os.path.join(dir_path, "your_file.pdf")

# PDFファイルを読み込む
with open(pdf_path, "rb") as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)

    # PDFの各ページに対して処理を行う
    for page_number in range(len(reader.pages)):
        page = reader.pages[page_number]
        text = to_full_width(page.extract_text())

        # テキストファイルに書き出す
        with open(
            os.path.join(dir_path, f"data/output_page_{page_number}.txt"),
            "w",
            encoding="utf-8",
        ) as output_file:
            output_file.write(text)
