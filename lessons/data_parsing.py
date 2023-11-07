"""Implement provided methods. You need to convert the class instance to JSON
or XML. When the user provides the command json to cli, the program should call
convert_to_json, when providing xml to cli program should convert the class
instance to xml string. And print it, or even better write it to a separate file.

You can use third parties libraries for this. If you use such a library please
add it to requirenment.txt"""
import json
import xml.etree.ElementTree as ET
import argparse


class Human:

    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year
        if arg == 'json':
            self.convert_to_json()
        elif arg == 'xml':
            self.convert_to_xml()
        else:
            print("choose json or xml")

    def convert_to_json(self):
        human_json = json.dumps(self.__dict__)
        with open(f'{self.name}_human.json', 'w') as f:
            f.write(human_json)

    def convert_to_xml(self):
        root = ET.Element('human')
        for i in self.__dict__.keys():
            title = ET.SubElement(root, i)
            title.text = self.__dict__.get(i)
        human_tree = ET.ElementTree(root)
        human_tree.write(f'{self.name}_human.xml')


parser = argparse.ArgumentParser('My parser')
parser.add_argument('--convert', required=True, help='Set type to convert class')
arg = parser.parse_args().convert

if __name__ == '__main__':
    anna = Human('Anna', '23', 'women', '2000')
    lisa = Human('Lisa', '20', 'women', '2003')
