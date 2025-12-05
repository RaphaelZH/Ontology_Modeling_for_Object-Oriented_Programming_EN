from owlready2 import *

import re

onto = get_ontology("OO.owx").load()
file_content_1, file_content_2, file_content_3 = "", "", ""

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
            class_content_2 = f"class {cls.name}({supercls.name}):\n"
            if not prop_list:
                class_content_2 += "\tpass\n\n".expandtabs(4)
            else:
                args = ", ".join(prop_list)
                class_content_2 += f"\n\tdef __init__(self, {args}):\n\t\tsuper().__init__()\n".expandtabs(4)
                for prop_name in prop_list:
                    class_content_2 += f"\t\tself.{prop_name} = {prop_name}\n".expandtabs(4)
                class_content_2 += "\n"
            file_content_2 += class_content_2
        else:
            class_content_1 = f"class {cls.name}:\n"
            if not prop_list:
                class_content_1 += "\tpass\n\n".expandtabs(4)
            else:
                args = ", ".join(prop_list)
                class_content_1 += f"\n\tdef __init__(self, {args}):\n".expandtabs(4)
                for prop_name in prop_list:
                    class_content_1 += f"\t\tself.{prop_name} = {prop_name}\n".expandtabs(4)
                class_content_1 += "\n"
            file_content_1 += class_content_1

for cls in onto.classes():
    for i in cls.instances():
        if i.get_properties() == []:
            instance_content = f"{i.name} = {cls.name}()\n"
        else:
            instance_content = f"{i.name} = {cls.name}("
            for prop in i.get_properties():
                instance_content += f"{prop.name}="
                values = prop[i]
                if len(values) == 1:
                    value = values[0]
                    instance_content += f'"{value}", ' if isinstance(value, str) else f"{value}, "
                else:
                    values = ", ".join([f'"{v}"' if isinstance(v, str) else str(v) for v in values])
                    print(values)
                    instance_content += values
            instance_content = instance_content + ")\n"
            file_content_3 += instance_content

file_content = file_content_1 + "\n" + file_content_2 + "\n" + file_content_3

with open("Python_OOP.py", "w") as file:
    file.write(file_content)