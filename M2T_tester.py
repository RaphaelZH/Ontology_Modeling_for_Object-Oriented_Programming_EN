from glob import glob
from owlready2 import *
from termcolor import cprint
import xml.etree.ElementTree as ET

input_dir = "1. Inputs"
model_dir = "1. Input Models"
model_files = glob(f"{input_dir}/{model_dir}/*.model")

onto_dir = "2. Input Ontology"
onto = get_ontology(
    f"{input_dir}/{onto_dir}/Programming Language Generation Path.owl"
).load()

output_dir = "2. Outputs"
language = "python"
language_list = ["Python", "Java", "Cpp"]
language_dir = f"{language_list.index(language.capitalize()) + 1}. {language.capitalize()} Files"

for individual in onto.individuals():
    for cls in onto.classes():
        if cls.name == language and cls in individual.is_a:
            if individual.name == f"{language.lower()}_file_header":
                file_header = individual.code
            elif individual.name == f"{language.lower()}_class_initializer_head":
                class_initializer_head = individual.code
            elif individual.name == f"{language.lower()}_class_initializer_body":
                class_initializer_body = individual.code
            elif individual.name == f"{language.lower()}_attribute_getting":
                attribute_getting = individual.code
            elif individual.name == f"{language.lower()}_attribute_settings":
                attribute_settings = individual.code
            elif individual.name == f"{language.lower()}_class_initializer_tail":
                class_initializer_tail = individual.code

package_code = file_header[0].format(n="\n", t="\t").expandtabs(4)
for model_file in model_files:
    model_tree = ET.parse(model_file)
    model_root = model_tree.getroot()
    package_name = model_root.attrib.get("name")

    for content in model_root.iter("contents"):
        class_name = content.attrib.get("name")
        class_code = f"{class_initializer_head[0]}".format(
            class_name=class_name, n="\n", t="\t"
        ).expandtabs(4)

        for feature in content.iter("features"):
            attribute_name = feature.attrib.get("name")
            class_code += f"{class_initializer_body[0]}".format(
                class_name=class_name, attribute_name=attribute_name, n="\n", t="\t"
            ).expandtabs(4)
        class_code += "\n"

        for feature in content.iter("features"):
            attribute_name = feature.attrib.get("name")
            class_code += f"{attribute_getting[0]}".format(
                class_name=class_name, attribute_name=attribute_name, n="\n", t="\t"
            ).expandtabs(4)

        for feature in content.iter("features"):
            attribute_name = feature.attrib.get("name")
            class_code += f"{attribute_settings[0]}".format(
                class_name=class_name, attribute_name=attribute_name, n="\n", t="\t"
            ).expandtabs(4)

        class_code += f"{class_initializer_tail[0]}".format(
            class_name=class_name, n="\n", t="\t"
        ).expandtabs(4)

        package_code += class_code

    if language.capitalize() == "Python":
        file_format = "py"
    with open(f"{output_dir}/{language_dir}/{package_name.lower()}.{file_format}", "w") as file:
        file.write(package_code)
