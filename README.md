## システム設計図
+------------+       +---------------------+       +------------------+
|   Browser  | <---> | Flask (app.py)      | <---> | logic.py          |
| (ユーザー) |       | ルーティング+表示    |       | Free Dictionary API|
+------------+       +---------------------+       +------------------+

## コード説明図
app.py
 └── index() : ルート画面 + 入力処理 + 入力フォーム + 結果表示
       └── get_definition(word) @ logic.py

logic.py
 └── get_definition(word): API呼び出し
       └── Free Dictionary API (dictionaryapi.dev)
