"""
Following are the topics we will cover today.

1)  Know how – Python Absolute Path + write file
2)  File Parsing with “With”
3)  File Parsing with Generator
4)  File parsing with Pandas Library
5)  Parse JSON file
6)  Parse XML file
7)  Inheritance

"""
from os import path, makedirs, mkdir

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
    current_directory, 'test_demo', 'json_file', 'parse_json_data.json'
)

# if path.exists(json_file_path):
#     print("hello JSON")
#
xml_file_path = path.join(
    current_directory, 'test_demo', 'xml_file', 'parse_xml_data.xml'
)
#
# if path.exists(xml_file_path):
#     print("hello XML")

text_file_path = path.join(
    current_directory, 'test_demo', 'text_file', 'parse_text.txt'
)

csv_file_path = path.join(
    current_directory, 'test_demo', 'csv_file', 'parse_csv.csv'
)


#
# if not path.exists(path.dirname(text_file_path)):
#     makedirs(path.dirname(text_file_path))
#
# text_data = "This is my text file and i want to write anything in this file.\n"
# text_data += "You could not stop me whatever I want to do i will do it.\n"
# text_data += "That's it."
#
# with open(text_file_path, 'w') as text_file:
#     text_file.writelines(text_data)


# #############################################################################
# 2)  File Parsing with “With”
# #############################################################################

def parse_using_with(file_path):
    with open(file_path, 'r') as _file:
        return _file.readlines()


# print(parse_using_with(json_file_path))

# #############################################################################
# 3)  File Parsing with Generator
# #############################################################################


# def generator_file_parser(file_path):
#     with open(file_path, 'r') as _file:
#         for line in _file.readlines():
#             if line:
#                 yield line
#             else:
#                 _file.close()
#
#
# for g in generator_file_parser(text_file_path):
#     print(g)


# #############################################################################
# 4)  File parsing with Pandas Library
# #############################################################################

#
# import pandas as pd
#
# data = pd.read_csv(csv_file_path, sep=",", header=0)
# # x = data.columns = ["a", "b", "c"]
# print(data)

# #############################################################################
# 5)  Parse JSON file
# #############################################################################

#
# from json import load
#
# # data = ''
# with open(json_file_path, 'r') as _file:
#     data = load(_file)
#
# from pprint import pprint
# print(type(data))
#
# pprint(data.get('maps')[1].get('id'))


# #############################################################################
# 6)  Parse XML file
# #############################################################################

# from xml.dom import minidom
# xmldoc = minidom.parse(xml_file_path)
# itemlist = xmldoc.getElementsByTagName('item')
# print(len(itemlist))
#
# for s in itemlist:
#     print(s.attributes['name'].value)

# from bs4 import BeautifulSoup
#
# with open(xml_file_path, 'r') as _file:
#     data = _file.readlines()
#
# y = BeautifulSoup(str(data))
# print(y.data.items.findAll("type"))


# #############################################################################
# 7)  Inheritance
# #############################################################################

class ClassA(object):
    member_variable = None

    def __init__(self):
        self.instance_variable = None
        self.method = None
        self.table = None

    def where_i_am(self):
        print("you are in ClassA")

    def __del__(self):
        """

        :return:
        """

    def __str__(self):
        return "{}-{}".format(self.method, self.table)


class ClassB(ClassA):
    def where_i_am(self):
        print("you are in ClassB")


class ClassC(ClassA):
    def where_i_am(self):
        print("you are in ClassC")


class ClassD(ClassC, ClassB): pass


# def where_i_am(self):
#     print("You are in ClassD")


ClassD().where_i_am()
