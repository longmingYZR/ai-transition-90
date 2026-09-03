texts = [
    "excavadora, trituradora", 
" camion minero, excavadora", 
"trituradora, camion minero"
]

gran_list = []  #准备一个空的容器，用来装最后拆出来的所有机器名

# 把texts 里的每一条文本，依次拿出来处理
for x in texts:
    # 第一圈，machines = "excavadora, trituradora"
    machines = x.split(",")
    # 第一圈，machines = ["excavadora"," trituradora"]

    for item in machines:
        # 当前拿到的这个item是什么？
        # 第一圈第一个item = "excavadora"
        # 第一圈第二个item = " trituradora"


        item.strip()
        # strip 把两端的空格去掉

        gran_list.append(item.strip())
        # 把消好的数据装进 gran_list
        # 第一圈结束后，装进去的数据 gran_list = ["excavadora","trituradora"]
        # 第二圈结束后，装进去的数据 gran_list = ["excavadora","trituradora"，"camion minero","excavadora"]

print(gran_list)
# 打印最终的大列表
    











    
   


    
