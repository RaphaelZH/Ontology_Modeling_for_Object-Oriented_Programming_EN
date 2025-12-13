from glob import glob
from owlready2 import *
from termcolor import cprint
import xml.etree.ElementTree as ET
from pyswip import Prolog

input_dir = "1. Inputs"
model_dir = "1. Input Models"
model_files = glob(f"{input_dir}/{model_dir}/*.model")

onto_dir = "2. Input Ontology"
onto = get_ontology(
    f"{input_dir}/{onto_dir}/Programming Language Generation Path.owl"
).load()

output_dir = "2. Outputs"
language = "Python".replace("+", "p")
language_list = ["Python", "Java", "Cpp"]
language_dir = (
    f"{language_list.index(language.capitalize()) + 1}. {language.capitalize()} Files"
)


prolog = Prolog()

prolog.assertz("ancestor(A, D) :- parent(A, D)")
prolog.assertz("ancestor(A, D) :- parent(A, P), ancestor(P, D)")

for prop in onto.properties():
    if prop.name == "has_child":
        for individual in prop.get_relations():
            print(prop.name, "->", individual[0].name, "->", individual[1].name)
            print(individual[0].name, "->", individual[1].name)
            prolog.assertz(f"parent({individual[0].name}, {individual[1].name})")
    else:
        pass

for q in prolog.query("ancestor(bbb, X)"):
    print("bbb is ancestor of", q["X"])

"""
prolog.assertz("father(michael,john)")
prolog.assertz("father(michael,gina)")
list(prolog.query("father(michael,X)")) == [{'X': 'john'}, {'X': 'gina'}]
for soln in prolog.query("father(X,Y)"):
    print(soln["X"], "is the father of", soln["Y"])
"""