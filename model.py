from glob import glob
from owlready2 import *
from termcolor import cprint
import xml.etree.ElementTree as ET

input_dir = "1. Inputs"
model_dir = "1. Input Models"
model_files = glob(f"{input_dir}/{model_dir}/*.model")

onto = get_ontology("Programming Language Generation Path.owl").load()
print(onto)

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
