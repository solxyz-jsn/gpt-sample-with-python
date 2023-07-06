# Pythonを利用したOpenAI APIサンプル

Pythonでの実装方法をいくつか紹介します。

## 環境準備

事前にPythonはインストールされているものとします。

Pythonの基礎知識はSolxyz Academy「Python言語基礎」で学ぶことができます。

または[公式ドキュメント](https://docs.python.org/ja/3/)で学習してください。

### リポジトリのクローン

```PowerShell
git clone https://github.com/solxyz-jsn/gpt-sample-with-python.git
```

### 仮想環境の作成

```PowerShell
python -m venv gpt-sample
```

### 仮想環境のアクティブ化

```PowerShell
.\gpt-sample\Scripts\activate.ps1
```

### 利用ライブラリのインストール

```PowerShell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### .envファイルの作成

```PowerShell
New-Item .env
```

### Open AIのアクセスキーの設定

作成された`.env`ファイルを開き、以下を保存します。

```.env
OPENAI_API_KEY='あなたのアクセスキー'
```

## 実行方法

### シンプルな例


