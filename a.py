import xml.etree.ElementTree as ET

from glob import glob

input_dir = "1. Inputs"
model_dir = "1. Input Models"

model_files = glob(f"{input_dir}/{model_dir}/*.model")
# Registration Form.model

for model_file in model_files:
    model_tree = ET.parse(model_file)
    model_root = model_tree.getroot()
    
    for contents in model_root.iter("contents"):
        print(contents.tag, contents.attrib)
        
    
    """
    for elem in model_root.iter("{OO}Package"):
        class_name = elem.get("name")
        print(class_name)
        
        
        for attr in elem.iter("Attribute"):
            attr_name = attr.get("name")
            attr_type = attr.get("type")
            print(f" - {attr_name}: {attr_type}")
        """