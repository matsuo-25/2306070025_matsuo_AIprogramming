## システム設計図
<img width="575" height="224" alt="image" src="https://github.com/user-attachments/assets/6e5c0dea-8c11-4fc2-8f81-fa261f709962" />



## コード説明図
app.py

 └── index() : ルート画面 + 入力処理 + 入力フォーム + 結果表示
 
       └── get_definition(word) @ logic.py

logic.py

 └── get_definition(word): API呼び出し
 
       └── Free Dictionary API (dictionaryapi.dev)
