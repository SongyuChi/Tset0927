# age=int(input("请输入你的年龄："))
# ctime=int(input("请输入你的入职时间："))
# rank=int(input("请输入你的级别："))
# if age>18:
#   print("年龄超过18，符合条件")
#   if age<30:
#       print("年龄未超过上限")
#       if ctime>2:
#           print("工作时长满足条件，你可以领取")
#       elif rank>3:
#           print("级别满足条件，可以领取")
#       else:
#           print("工时和级别均不满足，不可领取")
#
#   else:
#       print("年龄超过30，不可领取")
# else:
#     print("年龄不满18，不可领取")
import json

# import random
# num = random.randint(1,10)
# if int(input("请输入一个数字："))==num:
#     print("猜对啦！")
# elif int(input("猜错啦，再输一次："))==num:
#     print("这次猜对啦！")
# else:
#     if int(input("最后一次机会："))==num:
#         print("猜对啦！")
#     else:
#         print("猜错了，机会已用完，正确结果是%d" %num)


# import random
# num = random.randint(1,10)
# times=1
# test=int(input("请输入一个数字："))
# while test !=num:
#     if test>num:
#         print("猜大了，试试小一点的")
#         times+=1
#         test =int(input("请输入一个数字："))
#     else:
#         print("猜小了，试试大一点的")
#         times += 1
#         test = int(input("请输入一个数字："))
# print("猜对啦，谜底是%d，一共猜了%d次" %(num,times))



# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         times=i*j
#         if j<i :
#             print(f"\t{j}*{i}={times}", end='')
#         else:
#             print(f"\t{j}*{i}={times}")
#         j += 1
#     i+=1

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"\t{j}*{i}={j*i}",end='')
#     print()
# for j in range(1,2,5):              #range(i,j)  输出i到j-1
#     print(j)                                #range(i) 输出0到i-1      range(i,j,k) 步长为k，k可以为负
                                                                    # range(0, -10, -1) # 负数
                                                                       #[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

# money=10000
# worker_num=1
# odd=0
# for worker_num in range(1,21):
#     import random
#     odd=random.randint(1,10)
#     if odd<= 5:
#         print(f"员工编号{worker_num}绩效太低，发不了")
#         continue
#     if money<=0:
#         print("没钱了")
#         break
#     print(f"员工编号{worker_num}发工资1000元")
# print("发工资结束")
# def hesuan (a,tem):
#     print("请出示核酸报告！")
#     if a==1:
#         print("核酸正常")
#         if tem <37.5 :
#             print("体温正常，可以通行")
#         else:
#             print("体温报警，不可进入")
#     else:
#         print("无核酸报告，不可进入")
# a=int(input("请输入核酸报告："))#1代表有核酸报告 0代表没有
# tem=int(input("请输入体温："))
# hesuan(a,tem)




# global a
# a=0
# def testcsy():
#     global a
#     a+=1
# def testcsy2():
#     global a
#     a+=1
#                    #global a a+=1
# testcsy()
# testcsy2()
# print(a)                      # a=2
           # global 用于函数内部，对于某个全局变量a 当函数要使用它时需要声明一下 每个函数（使用a的）都需要写一下





# Error=0
# name=None
# money=500000
# def mainmenu(name):
#     print("------------主菜单--------------")
#     print(f"{name}客户您好！欢迎来到银行，请选择以下操作：")
#     print("查询余额  输入【1】")
#     print("存款     输入【2】")
#     print("取款     输入【3】")
#     print("退出     输入【4】")
#
#     global num
#     num=int(input("请输入您的选择："))
#     if num==1:
#         yue()
#     elif num==2:
#         cunkuan()
#     elif num==3:
#         qukuan()
#     else :
#         if num!=4:
#             print("输入错误，退出系统，请重新登陆！")
#             global Error
#             Error=1
#
# def yue ():
#     print("-------查询余额--------")
#     print(f"{name},您好！您的当前余额为：{money}")
# def cunkuan():
#     print("-------存款-------")
#     cun=int(input())
#     global money
#     money=money+cun
#     print(f"{name}，您好！您存款{cun}元成功")
#     print(f"{name},您好！您的当前余额为{money}元")
# def qukuan():
#     print("-------取款-------")
#     qu = int(input())
#     global money
#     money = money-qu
#     print(f"{name}，您好！您取款{qu}元成功")
#     print(f"{name},您好！您的当前余额为{money}元")
# name=input("请输入您的姓名：")
# mainmenu(name)
# while num!=4:
#     if Error==1:
#         break
#     mainmenu(name)
#匿名函数lambda ：    lambda 输入变量1，输入变量2，...: 输出值  （如x+y x[1]）   可用于一些简单函数的匿名实现，即直接写到代码里，不用单独定义函数了，详见215行list.sort的使用

# class Student:
#     def 函数名(参数):
#    student=Student()
#    k=student.函数名()                   #方法的定义



#my_list=["csy","20010508","male"]     #列表查询某元素下标索引功能，基本格式为：  列表名.index(元素)
# k=my_list.index("male")
# print(k)
                                        #修改某元素值，格式：列表名[下标]=新值
#my_list.insert(1,"communist")          #插入元素格式：列表名.insert(插入位置下标,新元素)
# my_list.append("Chinese")               #在末尾追加元素：列表名.append(元素)
# my_list.extend(["a","b"])               #传入多个，则为 列表名.extend([元素1，元素2，...])
# del my_list[0]                          #删除某元素： del 列表名[下标]
# k=my_list.pop(0)                        #删除某元素：列表名.pop(下标)    且可以返回删掉的元素
#print(k)
#.remove("csy")                    #删除满足条件的第一个的指定元素；列表名.[元素]
#print(my_list)
                                         #清空列表：  列表名.clear()
#k=my_list.count("20010508")                   #统计列表中某元素的数量； 列表名.count(元素)
#print(k)
#print(len(my_list))                               #求长度；len(列表名)
#index=0
# while index<len(my_list):
#     print(f"列表的元素：{my_list[index]}")
#     index=index + 1
#for x in my_list:
 #   print(f"列表中的元素：{x}")
#print(f"列表长度为:{len(my_list)}")

#序列的切片     序列是指元素可以连续，紧密地排列在一起且可以使用下标索引的一类数据容器。切片就是取出一个子序列。切片后得到新串，原来的不受影响
#my_list=[0,1,2,3,4,5]
#he_list=my_list[1:5:2]   #省略哪个表示直到哪头（或从哪开始）[起始:结尾:步长]  包括头不包括尾   [起始:结尾] 默认步长为1    [:]起始到结尾全输出  [::2]步长为2，从头到尾
#print(he_list)           #[::-1]倒着输出所有   [5:3:-1]从5输出到3后一个
# my_list ="万过薪月，员序程马黑来，nohtyp学"
# result_1=my_list[9:4:-1]
# print(result_1)

#list.sort功能的使用
# my_list=[["a", 11], ["b", 22], ["c", 33]]
# # def abc(x):
# #     return x[1]
# #my_list.sort(key=abc,reverse=False)   #key后边必须传入函数名，函数指定排序依据，如本例中x[1]为依据。reverse为True表示反向输出,False表示正向输出
# my_list.sort(key= lambda x: x[1],reverse=False)  #用匿名函数lambda 的替代方法
# print(my_list)




# list_1=[1,2,3,4,5,6,7,8,9,0]
# my_list=[]
# count=0
# cont=0
# while count<len(list_1):
#     k=list_1[count]
#     if k%2==0:
#         my_list.append(k)
#         cont+=1
#     count+=1
# #print(my_list)
# my_list.clear()
# for x in list_1:
#     if x%2==0:
#         my_list.append(x)
# print(my_list)                  #打印列表中所有元素
#
#
                            #列表定义：     列表名=[元素1，元素2，元素3]
                            #空列表定义： 列表名=list()   或者是     列表名=[]
                            #列表下标索引 ：列表名[0],列表名[1],这是从左往右前两个；列表名[-1]这是从右往左第一个，列表名[-2]从右往左第二个。
# my_list=[1,2,3]                                             #列表名[第一层下标][第二层下标]，嵌套列表取元素
# for ele in my_list:
#     print(f"列表的元素有：{ele}")



# tup=([1,2,3],4,5)          #定义元组，元组一经定义不可修改（要是元组里嵌套一个列表，可以改列表里的内容）
# print(tup)                              # 定义空元组： 元组名=()或者 元组名=tuple()
# tup[0][1]=6                            #注意元组只有一个元素时，要加个逗号，如 tuple(元素1，)
# print(tup)

#my_str="itheima itcast boxuegu"                #字符串.index("元素内容")
                                #字符串也是从右到左-1开始，从左到右0开始，不可以修改。
#he_str=" "
#he_str=my_str.replace("0","-1")   #字符串.replace(元素1，元素2)  这里元素可以是单个的也可以是一组
#print(f"my_str是：{my_str}"              #这里不是修改原字符串，只是以原字符串为基础参照，得到新的字符串，原来的还是原来的。
#print(f"he_str是：{he_str}")
#he_str=my_str.split(" ")        #字符串.split(分割符号（自定义）)是把字符串按分割符分割成若干元素，组成列表
#print(he_str)

#my_str.strip()         #把字符串前后空格去掉
#my_str.count("内容")    #统计内容出现的次数
# count=my_str.count("it")                           #字符串综合练习
# print(f"字符串中，共有it {count} 个")
# he_str=my_str.replace(" ","|")
# print(f"替换后，字符串为：{he_str}")
# k=he_str.split("|")
# print(f"字符串分割后为：{k}")



#集合  不允许重复元素出现，且不保证顺序,不支持下表索引访问。   定义空集合 集合名=set()  或者 集合名={}   集合名={元素1，元素2，原素3,，...}
# ab={1,2,3,4,4,5}
# print(ab)
# ab.add(6)                                 #集合中添加元素
# print(ab)
# ab.remove(6)                              #集合中移除元素
# print(ab)
# print(ab.pop())                           #集合中随机取一个元素,集合发生变化
# #ab.clear()                                #清空集合
# print(ab)
#                                           #集合1.difference(集合2) 取出集合1里有但是集合2里没有的，集合1,2本身不变，取出复制给新的集合
#                                           #集合1.difference_update(集合2) 在集合1内，删去和集合2一样的元素，集合1变，集合2不动
#                                           #集合1.union(集合2) 俩组成一个新集合，原来俩集合不动。
# print(len(ab))                            #求集合中元素个数
#

# my_list=["a","b","a","b","c","d","c","d"]
# jihe=set()
# for element in my_list:
#     jihe.add(element)
# print(jihe)

#字典          字典定义 ： 字典名={key:value,key:value,...}  key不可重复     空字典定义 字典名=dict()

# my_dict={"a":1,"b":2,"c":3}
# k=my_dict["b"]                  #查字典： 字典名[关键字key]  找出key对应内容
# print(k)

# score_dict={                      #字典嵌套
#     "wang":{"语文":77,
#             "数学":65,
#             "外语":89},
#     "zhou":{"语文":87,
#             "数学":85,
#             "外语":89},
#     "lin":{"语文":71,
#             "数学":35,
#             "外语":69}
# }
# #print(score_dict["wang"]["数学"])
#
# #  字典的操作
# score_dict["zhang"]={
#             "语文":77,
#             "数学":65,
#             "外语":8}                      #字典名[key]=value key已有，则是修改值；key没有，则是新增值

#score_dict={"a":1,"b":2,"c":3}
#k=score_dict.pop("lin")                   #从字典中取出“lin”对应元素，原字典被修改了
#print(score_dict)
#score_dict.clear                        #清空
#keys=score_dict.keys()                 #读取所有key
#遍历所有的内容
# for x in keys:                                #两种遍历方式都是可以的
#     print(f"KEY为{x}")
#     print(f"值为{score_dict[x]}")
# for y in score_dict:
#     print(f"2KEY为{y}")
#     print(f"2值为{score_dict[y]}")
                                    #len(字典名)    求元素个数

#字典综合练习


#函数的多返回值问题，  x,y=函数      函数里的return a,b 则实现多返回值。
# def one ():
#     return 1,2
# x,y=one()
# print(f"x为{x}，y为{y}")

#函数传入多个参数例子：
# def test_1(name,gender,age,):
#     print(name,gender,age)
# test_1("a","male",15)                      #这两种方式都可以
# test_1(name="b",gender="male",age=18)
 #关于args   传入任意个参数
# def abc(*args):
#     print(args)
# abc("a",18)
# def bcd(**kwargs):       #这种是必须按照字典格式传进去，格式为key=Value的模式
#     print(kwargs)
# bcd(a="Tom",b=18)


 #函数也可以作为参数调用
# def dda (x,y):
#     return x+y
#
# def kk (dda):
#     k=dda(1,2)
#     return k
#
# #print(kk(dda))
# print(kk(lambda x,y:x+y))    #等价于上面把dda传入，也就是不用单独写个函数dda了


#文件打开
#f=open("D:\测试0818.txt","r",encoding="UTF-8")       #打开文件
#print(f"读10个字节的结果是{f.read(10)}")                 #读文件，文件对象.read(num) 不写num就是读文件中所有的
#print(f"{f.read()}")                     #读文件指针是一定的，即上次读到哪，下次再读时就从那开始，所以这一行读不到所有的，因为指针已经在第10字节后面了。
#g=f.read()                                          #统计某元素的个数
#k=g.count('中')
#print(k)

#print(f"readlines{f.readlines()}")           #文件对象.readlines()  读文件所有行，并存到list结构里面，一行一个元素。
# print(f"readline{f.readline()}")              #readline   只读一行
# print(f"readline{f.readline()}")              #这里要注意指针位置的唯一性
# print(f"readline{f.readline()}")
# print(f"readline{f.readline()}")

#f.close()                                            #关闭文件，  文件对象.close()
#with open ("D:\测试0818.txt","r",encoding="UTF-8") as f  #打开文件的另一种方法，可以自动关闭，不用单独close了

#f=open("D:\测试0818.txt","w",encoding="UTF-8")       #写文件，w会把原来内容给全部清空，只是第一次w时清空之前的，本次程序里再往里写都不会再删前面的了。
#f.write("beidayanyuan")      #写到内存里
#f.flush()         #写到硬盘里
#f.close()          #也带有写的作用
# g=open("D:\测试0818.txt","r",encoding="UTF-8")
# print(f"{g.read()}")
#g.close()
#h=open("D:\测试0818.txt","a",encoding="UTF-8")    #也是写入，只不过不清空原来的
#h.write("\n hengmei")
#h.close()
#g=open("D:\测试0818.txt","r",encoding="UTF-8")
#for x in g:                                         #这里文件可以用for直接往出循环，但是不用for ，读文件内容就得加上read，for相当于包含了一个read 的功能
#   print(x)
#    print('d')


#如何debug

# try:
#     f=open("D:\测试0820.text","r",encoding="UTF-8")                #可能发生错误的代码
# except:                                                        #这种是捕获所有种类的异常
#     print("文件异常   ")
#     f=open("D:\测试0820.text", "w", encoding="UTF-8")               #如果发生错误，备选执行代码
# Name="abc"
# try:
#     print(Name)
# except NameError as a:                      #只捕获NameError 这种异常      a 是别名，用于输出提示 ，比如本例子中
#     print("错误了")
#     print(a)                                #捕获多种异常    except (异常类型1 异常类型2 ...) as a:
# else:
#     print("无异常")                          #无异常怎么办
# finally:
#     print("试验结束")                         #不论有无异常都是要执行的      else和 finally 都是可选的不是必须的

# def func1():
#     print("开始1")
#     1/0
#     print("结束1")
#
# def func2():
#     print("开始2")
#     func1()
#     print("结束2")
#
# def main():
#     try:
#         func2()
#     except:
#         print("出现异常了")
#main()

#模块

# import time                     # 导入模块基本语法 import 模块1，模块2
# print("开始")
# time.sleep(3)                    #使用模块功能，模块名.功能名()
# print("结束")

# from time import sleep            #从time模块导入sleep功能 ，一步解决;但是只能用sleep,直接用就行不用加time前缀了
# print("开始")
# sleep(3)
# print("结束")

# from time import *                  # 导入全部功能，但是也不用加time前缀了
#  print("开始")
#  sleep(3)
#  print("结束")
#
# import time as a                  # 加个别名，后面都用别名了
# print("开始")
# a.sleep(3)
# print("结束")

# from test0821 import addition           #另一种形式的别名这样用,这里是自定义的
# print("开始")
# a(3,2)
# print("结束")


#from test0821 import addition     #这里直接运行就能把addition调出来，（如果被调用的模块里使用了addition功能的话），所以为了
                                    #能够使模块里可以运行函数测试时，不会同时在这边也运行，就用到main了，详见test0821
#_all_=['模块内功能名1，模块内功能2，...']             #有这句时，如果使用from 模块 import *  则只能自动导入all里的功能
#if __name__ == '__main__':
    #addition(1, 2)

# import my_package0822                            #导入包
# my_package0822.my_module_1.dayin()

# from my_package0822 import my_module_1         #另一种形式的导入，同模块
# my_module_1.dayin()
# from my_package0822.my_module_1 import dayin      #另另一种
# dayin()


#文件，异常，包综合练习
#
# import my_package0822.my_module_1
# my_package0822.my_module_1.str_reverse("迟嵩禹")
# my_package0822.my_module_1.substr("csy",1,2)
# from my_package0822 import my_module_2
# my_module_2.print_file_info("D:\测试0818.txt")
# my_module_2.append_to_file("D:\测试0818.txt","ccc")

#json只有字典和列表两种格式，json在不同语言之间都是通用的。
# import json
# data=[{"name": "yi", "age1": 18}, {"name": "er", "age": 19}, {"name": "san", "age": 20}]
# json_str=json.dumps(data)                    #把python格式转化成json格式   json.dumps(data,ensure_ascii=False) 如果有中文的话要这么处理，否则乱码。
# print(json_str)
# l=json.loads(json_str)                        #把json格式转成python
# print(l)

# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts,LabelOpts
# line=Line()                     #Line属于类，故如此使用
# line.add_xaxis(["中国", "美国", "日本"])    #横坐标设置
# line.add_yaxis("GDP",[30, 20, 10],label_opts=LabelOpts(is_show=False))        #纵坐标设置,不在每个点处显示y值
# line.set_global_opts(                               #对图像整体设定一些参数如标题等
#     title_opts=TitleOpts(title="GDP展示",pos_left='center', pos_bottom='1%'),  #控制标题
#     legend_opts=LegendOpts(is_show=True),          #图例，就是上面那个GDP
#     toolbox_opts=ToolboxOpts(is_show=True),        #图片边上配一个工具箱
#     visualmap_opts=VisualMapOpts(is_show=True)     #图片颜色（没啥用）
# )
#
#
# line.render()


# from pyecharts.charts import Map
# from pyecharts.options import VisualMapOpts
# map=Map()
# data=[
#     ("北京市",110),        #这里要输全称，注意是[()]的形式
#     ("安徽省",92),
#     ("吉林省",3)
# ]
# map.add("测试地图", data, "china")
# map.set_global_opts(
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         pieces=[                                                      #设置不同数值区间的不同颜色
#             {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
#             {"min": 10, "max": 99,"label": "10-99", "color": "#FF6666"},
#             {"min": 100, "max": 999, "label": "100-999", "color": "#990033"}
#         ]
#     )
# )
# map.render()

# from pyecharts.charts import Bar,Timeline
# from pyecharts.options import *
# from pyecharts.globals import ThemeType
# bar1= Bar()
# bar1.add_xaxis(["中国", "美国", "日本"])
# bar1.add_yaxis("GDP", [2000, 1000, 500], label_opts=LabelOpts(position="right"))
# bar1.reversal_axis()
# #bar1.render("GDP对比.html")      柱状图的构建要手动在括号里加上html,折线图自动变html
#
# bar2= Bar()
# bar2.add_xaxis(["美国", "中国", "日本"])
# bar2.add_yaxis("GDP", [1100, 1000, 800], label_opts=LabelOpts(position="right"))
# bar2.reversal_axis()
#
# bar3= Bar()
# bar3.add_xaxis(["日本", "美国", "中国"])
# bar3.add_yaxis("GDP", [2100, 1800, 900], label_opts=LabelOpts(position="right"))
# bar3.reversal_axis()
#
# timeline=Timeline({"theme":ThemeType.LIGHT})
# timeline.add(bar1,"1900 GDP")
# timeline.add(bar2,"1940 GDP")
# timeline.add(bar3,"1950 GDP")
# timeline.add_schema(           #播放
#     play_interval=1000,    #时间间隔，毫秒
#     is_timeline_show=True,  #按时间线播放
#     is_auto_play=True,      #自动播放
#     is_loop_play=False       #循环
#
# )
# timeline.render("时间线.html")



#画动态柱状图 1960-2020GDP
# from pyecharts.charts import Bar,Timeline
# from pyecharts.options import *
# from pyecharts.globals import ThemeType
# f=open("D:/1960-2019GDP.txt", "r", encoding="UTF-8")
# data_lines=f.readlines()
# f.close()
# data_lines.pop(0)
# dict={}
# for x in data_lines:
#     year= int(x.split(",")[0])
#     country=str(x.split(",")[1])
#     gdp= float(x.split(",")[2])
#     try:
#         dict[year].append([country, gdp])
#     except KeyError:
#         dict[year]=[]  #这里注意要先定义空的，才能往里加东西
#         dict[year].append([country, gdp])
# sort_years=sorted(dict.keys())
# timeline= Timeline({"theme":ThemeType.LIGHT})
# for y in sort_years:
#     dict[y].sort(key=lambda ele: ele[1], reverse=True)  #针对嵌套列表，每个元素有好几个内容，按其中一个内容为标准来进行元素的排序
#     real_list= dict[y][0:8]
#     x_data=[]
#     y_data=[]
#     for z in real_list:
#         x_data.append(z[0])
#         y_data.append(z[1]/100000000)
#     x_data.reverse()
#     y_data.reverse()
#     bar=Bar()
#     bar.add_xaxis(x_data)
#     bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
#     bar.reversal_axis()
#     bar.set_global_opts(
#         title_opts=TitleOpts(title=f"{y}年全球前8GDP数据")
#     )
#     timeline.add(bar,f"{y} GDP")
# timeline.add_schema(           #播放
#     play_interval=500,    #时间间隔，毫秒
#     is_timeline_show=True,  #按时间线播放
#     is_auto_play=True,      #自动播放
#     is_loop_play=False       #循环
#
# )
# timeline.render("1960-2020 GDP.html")
#


#画疫情地图

# from pyecharts.charts import Map
# from pyecharts.options import *
#
# f=open("D:\地图数据\疫情.txt","r",encoding="UTF-8")
# data= f.read()
# f.close()
# data1=json.loads(data)                                #得把json换成python格式
# data2=data1["areaTree"][0]["children"]
# list=[]
# for x in data2:
#     list.append([x["name"]+"省", x["total"]["confirm"]])
# print(list)
# map=Map()
# map.add("测试地图", list, "china")
# map.set_global_opts(
#     title_opts=TitleOpts(title="全国疫情地图"),
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         pieces=[                                                      #设置不同数值区间的不同颜色
#             {"min": 1, "max": 99, "label": "1-9", "color": "#CCFFFF"},
#             {"min": 100, "max": 999,"label": "10-99", "color": "#FF6666"},
#             {"min": 1000, "max": 9999, "label": "100-999", "color": "#990033"}
#         ]
#     )
# )
# map.render("全国疫情地图.html")

# from pyecharts.charts import Map
# from pyecharts.options import *
#
# f=open("D:\地图数据\疫情.txt","r",encoding="UTF-8")
# data= f.read()
# f.close()
# data1=json.loads(data)                                #得把json换成python格式
# data2=data1["areaTree"][0]["children"][3]["children"]
# list=[]
# for x in data2:
#     list.append([x["name"]+"市", x["total"]["confirm"]])
# print(list)
# map=Map()
# map.add("地图", list, "河南")
# map.set_global_opts(
#     title_opts=TitleOpts(title="河南疫情地图"),
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         pieces=[                                                      #设置不同数值区间的不同颜色
#             {"min": 1, "max": 99, "label": "1-9", "color": "#CCFFFF"},
#             {"min": 100, "max": 999,"label": "10-99", "color": "#FF6666"},
#             {"min": 1000, "max": 9999, "label": "100-999", "color": "#990033"}
#         ]
#     )
# )
# map.render("河南疫情地图.html")



#画折线图
#
# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts,LabelOpts
# f=open("D:\折线图数据\美国.txt","r",encoding="UTF-8")
# data1=f.read()
# f.close()
# data2=data1.replace("jsonp_1629344292311_69436("," ")
# data3=data2[:-2]
# data4=data3.strip()
# data5=json.loads(data4)
# US_x_data=data5["data"][0]["trend"]["updateDate"][:314]
# US_y_data=data5["data"][0]["trend"]["list"][0]["data"][:314]
#
# f=open("D:\折线图数据\印度.txt","r",encoding="UTF-8")
# data1=f.read()
# f.close()
# data2=data1.replace("jsonp_1629350745930_63180("," ")
# data3=data2[:-2]
# data4=data3.strip()
# data5=json.loads(data4)
# IN_x_data=data5["data"][0]["trend"]["updateDate"][:314]
# IN_y_data=data5["data"][0]["trend"]["list"][0]["data"][:314]
#
#
# f=open("D:\折线图数据\日本.txt","r",encoding="UTF-8")
# data1=f.read()
# f.close()
# data2=data1.replace("jsonp_1629350871167_29498("," ")
# data3=data2[:-2]
# data4=data3.strip()
# data5=json.loads(data4)
# JP_x_data=data5["data"][0]["trend"]["updateDate"][:314]
# JP_y_data=data5["data"][0]["trend"]["list"][0]["data"][:314]
#
#
#
# line=Line()                     #Line属于类，故如此使用
# line.add_xaxis(US_x_data)    #横坐标设置
# line.add_yaxis("confirm",US_y_data,label_opts=LabelOpts(is_show=False))        #纵坐标设置,不在每个点处显示y值
# line.add_yaxis("confirm",JP_y_data,label_opts=LabelOpts(is_show=False))
# line.add_yaxis("confirm",IN_y_data,label_opts=LabelOpts(is_show=False))
# line.set_global_opts(                               #对图像整体设定一些参数如标题等
#     title_opts=TitleOpts(title="疫情",pos_left='center', pos_bottom='1%'),  #控制标题
#     legend_opts=LegendOpts(is_show=True),          #图例，就是上面那个GDP
#     toolbox_opts=ToolboxOpts(is_show=True),        #图片边上配一个工具箱
#     visualmap_opts=VisualMapOpts(is_show=True)     #图片颜色（没啥用）
# )
#
#
# line.render("三国疫情数据对比.html")


#类
# class ABC:
#     name=None#空变量，相当于Null
#     def hello(self,csy):                        #类里面的函数叫方法,不同点在于要传入个self，通过self.XXX 才能访问类内部的变量，调用的时候不用管self
#         print(f"hello,i am {self.name},{csy}")
# aabc=ABC()
# aabc.name="cao"
# print(aabc.name)
# aabc.hello("kk")


# class Clock:
#     id=None
#     price=None
#     def ring(self):
#         import winsound
#         winsound.Beep(500,1000)
# clock1=Clock()                        #面向对象clock1 编程
# clock1.id="001919"
# clock1.price=29
# print(clock1.id,clock1.price)
# clock1.ring()
#
# clock2=Clock()
# clock2.id="001920"
# clock2.price=19
# print(clock2.id,clock2.price)
# clock2.ring()


import pandas as pd
student = pd.read_excel("D:/csytest0908.xlsx")
print(student)
student.drop_duplicates(subset="Num",inplace=True)
print(student)















