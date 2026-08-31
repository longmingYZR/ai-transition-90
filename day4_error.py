try:
    number = int(input("请输入一个数字："))
    print("你输入的是：", number)

except ValueError:
    print("输入错误，请输入数字")
