from owlready2 import *
import types

from DictionaryGenerator import python_dictionary_generator

keywords_dict, operators_dict = python_dictionary_generator()

onto = get_ontology("http://www.haozhang.me/Programming_Language_Parser.owl#")


with onto:

    class python_grammar(Thing):
        pass

    class python_lexer(python_grammar):
        pass

    class python_keywords(python_lexer):
        pass

    for key, value in keywords_dict.items():
        exec(f"cls_{key} = types.new_class('{key}', tuple([python_keywords]))")
        exec(f"indiv_{value} = cls_{key}('{value}')")

    class python_parser(python_grammar):
        pass

    class python_operators(python_parser):
        pass

    for key, value in operators_dict.items():
        exec(f"cls_{key} = types.new_class('{key}', tuple([python_operators]))")
        exec(f"indiv_{key.lower()} = cls_{key}('{key.lower()}')")

onto.save(file="1. Ontology Files/Programming Language Parser.owl")
