#config:utf-8
import os
import configparser

#root_dir = os.path.dirname(os.path.abspath('.'))#获取当前文件所在目录的上一级目录，即项目所在目录
root_dir = os.path.abspath('.')#获取当前目录
print("ddddd")
print(root_dir)
cf = configparser.ConfigParser()
cf.read(root_dir + "/config.ini")
print("wwwwww")
print(root_dir + "/config.ini")

secs = cf.sections() #获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，每个section由[]包裹，即[section]),并以列表的形式返回
print("ssss")
print(secs)

options = cf.options("DATABASE")#获取某个section名为DATABASE所对应得键
print(options)

items = cf.items("DATABASE")#获取section名为DATABASE所对应得全部键值对
print(items)
