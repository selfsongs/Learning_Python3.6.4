#读取文件
with open('pi_digits.txt') as file_object:
    contents=file_object.read()
    print(contents)#输出最后有一行空白行
    print(contents.rstrip())#输出去掉空白行

#逐行读取文件
filename='pi_digits.txt'
with open(filename)as file_object:
    for line in file_object:
        print(line.rstrip())

#逐行读取文件并保存在列表中
filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line.rstrip())

#将文件内容保存成不含空格的字符串
filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
pi_string=''
for line in lines:
    pi_string+=line.strip()
print(pi_string)
print(len(pi_string))

#open(filename,'r')读，默认以只读方式打开
#open(filename,'w')写
#open(filename,'a')附加
#写入文件,python只能将字符串写入文本文件，要将数值数据存储到文本文件中
#必须先使用函数str()将其转换为字符串格式
filename='programming.txt'
with open(filename,'w')as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

filename='programming.txt'
with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
    
