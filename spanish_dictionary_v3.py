import json

with open("dictionary.json", "r", encoding="utf-8") as file:
    dictionary = json.load(file)

def search_word(word):
    if word in dictionary:
        return dictionary[word]

    else:
        return None


word = input("请输入西语：")

result = search_word(word)

if result:
    print("中文：", result["中文"])
    print("英文：", result["英文"])

else:
    print("没有找到这个词")