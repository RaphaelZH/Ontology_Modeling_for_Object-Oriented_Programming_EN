from owlready2 import *

import re

onto = get_ontology("OO.owx").load()

for cls in onto.classes():
    print(f"Class: {cls.name}")
    prop_list = []
    for prop in onto.properties():
        if cls in prop.domain:
            if re.match("has_*", prop.name):
                print(prop.equivalent_to)
            prop_list.append(prop.name)
        print(prop_list)
    for supercls in cls.is_a:
        if supercls != Thing:
            class_content = f"class {cls.name}({supercls.name}):\n    pass\n\n"
        else:
            class_content = f"class {cls.name}:\n    pass\n\n"
            #print(cls.properties)#if cls != Thing:
            #    print(cls.get_properties())
        
for prop in onto.properties():
    print(f"Property: {prop.name}")
    for domain in prop.domain:
        print(f"  Domain: {domain.name}")
    #for range_ in prop.range:
    #    print(f"  Range: {range_.name}")

        
    #print(f"  Superclasses: {[supercls.name for supercls in cls.is_a]}")
    #for prop in cls.get_properties():
    #    print(f"  Property: {prop.name}")
    #    for value in prop[cls]:
    #        print(f"    Value: {value}")


        
#with open("Python_OOP.python", "w") as file:
#    file.write(file_content)