# -*- coding: utf-8 -*-

"""リクエストサンプル

OpenAI APIを使用して、単純なリクエストを送るサンプル

"""

import openai
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込み
load_dotenv()

# APIキーを環境変数から取得
openai.api_key = os.getenv("OPENAI_API_KEY")

# 日本語を英語に翻訳
response = openai.ChatCompletion.create(
    # エンジンの指定
    model="gpt-3.5-turbo",
    # ユーザーの発言として、日本語を入力
    messages=[
        {"role": "user", "content": "日本語に翻訳してください: '{Hello World}'"},
    ],
    max_tokens=60,
)

# '{Hello World}'を日本語に翻訳すると、「{こんにちは、世界}」となります。
print(response.choices[0]["message"]["content"].strip())
