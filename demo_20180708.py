"""
Following are the topics we will cover today.

1)  Know how – Python Absolute Path
2)  File Parsing with “With”
3)  File Parsing with Generator
4)  File parsing with Pandas Library
5)  Parse JSON file
6)  Parse XML file
7)  Inheritance

"""
from os import path

# #############################################################################
# 1) Python Absolute Path
# #############################################################################


# Current absolute path

# file_path = r"c:\repos\Library"
current_file_path = path.abspath(__file__)
print(current_file_path)

# Get current directory
current_directory = path.dirname(path.abspath(__file__))

# Concat file paths

json_file_path = path.join(
    current_file_path, 'test_demo', 'json_file', 'parse_json_data.json'
)

# #############################################################################
# 2)  File Parsing with “With”
# #############################################################################

# def parse_using_with(file_path):
#     with open(file_path, 'r') as _file:
#         return _file.readlines()


# #############################################################################
# 3)  File Parsing with Generator
# #############################################################################


# def generator_file_parser(file_path):
#     with open(file_path, 'r') as _file:
#         for line in _file.readlines():
#             if line:
#                 _file.close()
#                 yield line
#
#
# for g in generator_file_parser('demo_20180609.py'):
#     print(g)


# #############################################################################
# 4)  File parsing with Pandas Library
# #############################################################################


# import pandas
# data = pd.read_csv('demo_20180609.py', sep=" ", header=None)
# data.columns = ["a", "b", "c", "etc."]


# #############################################################################
# 5)  Parse JSON file
# #############################################################################


# from json import load
# data = ''
# with open('parse_json_data.json', 'r') as _file:
#     data = load(_file)
#


# #############################################################################
# 6)  Parse XML file
# #############################################################################

# from xml.dom import minidom
# xmldoc = minidom.parse('parse_xml_data.xml')
# itemlist = xmldoc.getElementsByTagName('item')
# print(len(itemlist))
# print(itemlist[0].attributes['name'].value)
# for s in itemlist:
#     print(s.attributes['name'].value)

# from bs4 import BeautifulSoup
#
# with open('parse_xml_data.xml', 'r') as _file:
#     data = _file.readlines()
#
# y = BeautifulSoup(data)
# y.data.items.findAll("item")


# #############################################################################
# 7)  Inheritance
# #############################################################################

# class ClassA(object):
#     def where_i_am(self):
#         print("you are in ClassA")
#
# class ClassB(ClassA):
#     def where_i_am(self):
#         print("you are in ClassB")
#
# class ClassC(A):
#     def where_i_am(self):
#         print("you are in ClassC")
#
# class ClassD(ClassB,ClassC):
#     def where_i_am(self):
#         print("You are in ClassD")
#
# ClassD().where_i_am()
