from owlready2 import *

import re

onto = get_ontology("OO.owx").load()

for cls in onto.classes():
    prop_list = []
    for prop in onto.properties():
        if cls in prop.domain:
            if re.match("is_*", prop.name):
                pass
            elif re.match("has_*", prop.name):
                prop_list.append(prop.name[4:])
            else:
                prop_list.append(prop.name)
    for supercls in cls.is_a:
        if supercls != Thing:
            class_content = f"class {cls.name}({supercls.name}):\n"
        else:
            class_content = f"class {cls.name}:\n"
            if not prop_list:
                class_content += "\tpass\n\n".expandtabs(4)
            else:
                args = ", ".join(prop_list)
                class_content += f"\n\tdef __init__(self, {args}):\n".expandtabs(4)
                for prop_name in prop_list:
                    class_content += f"\t\tself.{prop_name} = {prop_name}\n".expandtabs(4)
                class_content += "\n"
            print(class_content)
            # print(cls.properties)#if cls != Thing:
            #    print(cls.get_properties())


    # for range_ in prop.range:
    #    print(f"  Range: {range_.name}")

    # print(f"  Superclasses: {[supercls.name for supercls in cls.is_a]}")
    # for prop in cls.get_properties():
    #    print(f"  Property: {prop.name}")
    #    for value in prop[cls]:
    #        print(f"    Value: {value}")


# with open("Python_OOP.python", "w") as file:
#    file.write(file_content)
