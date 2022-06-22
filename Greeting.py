# print("Good morning")

# print("Good afternoon")

# print("Good evening")
#変数
# num = 1

# num01 = 2

# num_01 = 3

# print(num)

# print(num01)

# print(num_01)

# num02 = 123

# num03 = 1.23

# print(type(num02))

# print(type(num03))

#bool型、正か誤

# a = 10

# b = 1

# bool01 = (a < b)

# print(bool01)
# print(type(bool01))

#リスト 複数のデータ

# c = ["sato","suzuki","takahashi"]
# c[1] = "tanaka"

# print(c[0])
# print(c[1])
# print(c[2])

#演算子

# x = 10
# y = 2
# z = 10

# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x % y)

# 関係演算子

# print(x > y)
# print(x < y)

# print(x <= y)
# print(x >= z)

# print(x == y)
# print(x != y)

# 論理演算子

# x = 8
# y = 3

# print(x >= 5 and x <= 10)
# print(y >= 5 and y <= 10)

# print(x == 3 or y == 3)
# print(x == 1 or y == 1)

# 複合代入演算子

# x = 8
# y = 12
# z = 20

# x += 10
# z += (y)

# print(x)
# print(z)

# 条件分岐

# age = 0

# if age >= 20:
#   print("adult")
# elif age == 0:
#   print("baby")
# else:
#   print("child")

# 繰り返し処理(ループ処理)

# for i in range(5):
#   print(i)

# 条件の数になったら終わるbreak

# for i in range(5):
#   if i == 3:
#     break
#   print(i)

# iの数になったらスキップされる

# for i in range(5):
#   if i == 3:
#     continue
#   print(i)

# for分ネスト

# for i in range(3):
#   for j in range(3):
#     print(i,j, sep="-")

# リストの中身

# arr = [2, 4, 6, 8, 10]
# for i in arr:
#   print(i)

# arr = [2, 4, 6, 8, 10]
# sum = 0
# for i in arr:
#   sum += i
# print(sum)

# 関数 = メゾット？

# def say_hello():
#   print("hello world")

# say_hello()

# def say_hello(greeting):
#    print(greeting)

# say_hello("hello world")

# 変数に代入

# def say_hello(greeting):
#    print(greeting)

# hello = say_hello
# hello("good morning")

# def add(num01,num02):
#     print(num01+num02)

# add(6,2)

# def add(num01,num02):
#     return(num01+num02)

# print(add(6,2))

# def add(num01,num02):
#     return(num01+num02)

# add_result=add(6,2)
# print(add_result)

# def add(a,b,c):
#   return (a+b+c)/3

# add_result=add(9,4,2)
# print(add_result)

# クラス

# class Student:
#   def avg(self):
#     print((80 + 70)/2)

# a001 = Student()
# a001.avg()

# 繰り返し使える
# class Student:
#   def avg(self,math,english):
#     print((math + english)/2)

# a001 = Student()
# a001.avg(30,70)
# #アトリビュートはクラス内の変数のこと↓
# a001.name = "sato"
# print(a001.name)

# アトリビュートはクラス内の変数のこと↑インスタンスごとにアトリビュートを定義
# それを解消するための記述↓

# class Student:

#   def __init__(self,name):   #←コンストラクタ(初期化メソッド)
#     self.name = name         #アトリビュート

#   def avg(self,math,english):  #メソッド
#     print((math + english)/2)

# a001 = Student("sato")     #a001=インスタンス  Student("sato")=クラス
# print(a001.name)

# a002 = Student("tanaka")
# print(a002.name)


# 実践


# class Student:

#   def __init__(self,name):
#     self.name = name

#     def calculate_avg(self,date):
#         sum = 0

#         for num in date:
#             sum += num

#         avg = sum/len(date)
#         return avg

#         def jedge(self,avg):

#             if(avg >= 60):
#                 result="passed"
#             else:
#                 result="failed"
#             return result

# a001 = Student("sato")
# date = [70,65,50,90,30]
# avg = a001.calculate_avg(date)
# result = a001.jedge(avg)

# print(avg)
# print(a001.name+""+result)