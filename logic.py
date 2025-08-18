import requests

def get_definition(word):
    """Free Dictionary APIを使って単語の定義を取得"""
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code != 200:
        return "単語が見つかりませんでした。"

    data = response.json()
    try:
        meanings = data[0]["meanings"]
        definitions = []
        for meaning in meanings:
            part_of_speech = meaning["partOfSpeech"]
            for d in meaning["definitions"]:
                definitions.append(f"({part_of_speech}) {d['definition']}")
        return definitions
    except Exception:
        return "定義の取得に失敗しました。"
