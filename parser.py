from owlready2 import *
import types

from dictionary_creator import dictionaries_creator

keywords_dict, operators_dict = dictionaries_creator()

onto = get_ontology("http://www.haozhang.me/Programming_Language_Parser.owl#")


with onto:

    class python_grammar(Thing):
        pass

    class python_lexer(python_grammar):
        pass

    class keywords(python_lexer):
        pass

    class python_parser(python_grammar):
        pass


print(keywords_dict, operators_dict)


onto.save(file="1. Ontology Files/Programming Language Parser.owl")
