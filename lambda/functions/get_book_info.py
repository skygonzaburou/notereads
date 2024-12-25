import requests
import json

base_url = "https://note.com/api"


def note_serch(term="おすすめ 本", sort="hot", size=1):
    requirements = f"/v3/searches?context=note&q={term}&size={size}&start={0}&sort={sort}"
    url = base_url + requirements
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print(f"Error: {response.status_code}")
        return
    
    return data


def note_detail(note_key):
    requirements = f"/v3/notes/{note_key}"
    url = base_url + requirements
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print(f"Error: {response.status_code}")
        return

    return data

    
def test_hashtag_serch_note():
    # url = "https://note.com/api/v3/searches?context=magazine&q=北海道&size=1&start=0"
    url = "https://note.com/api/v2/hashtags/"
    hashtag = "おすすめ本"
    sort = "?f=popular&"
    # paid_only = "paid_only=false"
    paid_only = "paid_only=true"
    # size = "&size=1&start=0"
    size = ""

    url = "https://note.com/api/v2/hashtags/おすすめ本"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print(f"Error: {response.status_code}")

    # ↑このAPIは検索結果を取得できない。。

    # print(response)
    # print(response.json())


if __name__ == "__main__":
    # hashtag_serch_note()
    # simple_search_note()
    # note_serch()
    # note_detail(98718492)
    # note_detail("n8af48ab561f3")
    pass
