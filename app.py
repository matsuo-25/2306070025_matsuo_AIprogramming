import streamlit as st
from logic import get_definition

# タイトル
st.title("英単語辞書アプリ")

# ユーザー入力
word = st.text_input("検索したい英単語を入力してください")

# 入力があれば定義を取得して表示
if word:
    definition = get_definition(word)
    
    if definition:
        if isinstance(definition, list):
            st.subheader(f"検索結果: {word}")
            for d in definition:
                st.write(f"- {d}")
        else:
            st.error(definition)
