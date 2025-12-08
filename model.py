from glob import glob
from owlready2 import *
from termcolor import cprint
import xml.etree.ElementTree as ET

input_dir = "1. Inputs"
model_dir = "1. Input Models"
model_files = glob(f"{input_dir}/{model_dir}/*.model")

onto_dir = "2. Input Ontology"
onto = get_ontology(f"{input_dir}/{onto_dir}/Programming Language Generation Path.owl").load()

language = "Python"
for individual in onto.individuals():
    for cls in onto.classes():
        if cls.name == language and cls in individual.is_a:
            if individual.name == f"{language.lower()}_class_initializer_head":
                class_initializer_head = individual.code
            elif individual.name == f"{language.lower()}_class_initializer_body":
                class_initializer_body = individual.code
            elif individual.name == f"{language.lower()}_attribute_getting":
                attribute_getting = individual.code
            elif individual.name == f"{language.lower()}_attribute_settings":
                attribute_settings = individual.code
            elif individual.name == f"{language.lower()}_class_initializer_tail":
                class_initializer_tail = individual.code

for model_file in model_files:
    model_tree = ET.parse(model_file)
    model_root = model_tree.getroot()
    cprint(
        f"Root: {model_root.tag} {model_root.attrib}", "red", attrs=["dark"], end="\n"
    )
    cprint(
        f"- Package name: {model_root.attrib.get('name')}".expandtabs(4),
        "red",
        attrs=["dark"],
        end="\n",
    )

    for content in model_root.iter("contents"):
        cprint(
            f"\tContent: {content.tag} {content.attrib}".expandtabs(4),
            "red",
            attrs=["bold"],
            end="\n",
        )
        cprint(
            f"\t- Class name: {content.attrib.get('name')}".expandtabs(4),
            "red",
            attrs=["bold"],
            end="\n",
        )

        for feature in content.iter("features"):
            cprint(
                f"\t\tFeature: {feature.tag} {feature.attrib}".expandtabs(4),
                "red",
                attrs=["blink"],
                end="\n",
            )
            cprint(
                f"\t\t- Attribute name: {feature.attrib.get('name')}".expandtabs(4),
                "red",
                attrs=["blink"],
                end="\n",
            )
