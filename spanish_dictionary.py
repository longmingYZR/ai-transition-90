dictionary = {
    "excavadora": {
        "中文": "挖掘机",
        "英文": "excavotor"
    },
    "trituradora": {
        "中文": "破碎机",
        "英文": "crusher"
    },
    "camion minero": {
        "中文": "矿卡",
        "英文": "mining truck"
    }
}


word = "excavadora"

result = dictionary[word]

print("西语：", word)
print("中文：", result["中文"])
print("英文：", result["英文"])