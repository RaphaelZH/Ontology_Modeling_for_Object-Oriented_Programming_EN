import xml.etree.ElementTree as ET

from glob import glob

xml_dir = "Object-Oriented Instance.model"

xml_files = glob(f'Object-Oriented Instance.model')

print(xml_files)

tree = ET.parse("Object-Oriented Instance.model")
root = tree.getroot()
print(root)