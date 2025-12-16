from owlready2 import *
import types

from DictionaryGenerator import python_dictionary_generator
from BasicClassGenerator import ontology_generator

keywords_dict, operators_dict, other_symbols_dict = python_dictionary_generator()

onto = ontology_generator()
with onto:

    class python(onto.programming_language):
        pass

    class python_lexer(onto.language_lexer):
        pass

    class python_parser(onto.language_parser):
        pass

    class python_keywords(python_lexer):
        pass

    class python_operators(python_lexer):
        pass

    class python_other_symbols(python_lexer):
        pass

    class python_stmt(python_parser):
        pass

    class python_simple_stmt(python_stmt):
        pass

    class python_compound_stmt(python_stmt):
        pass

    class python_classdef(python_parser):
        pass

    class python_funcdef(python_parser):
        pass

    class python_arguments(python_parser):
        pass

    class python_arglist(python_parser):
        pass

    class python_arguments_syntax1(python_arguments):
        pass

    class python_arguments_syntax1_element1(python_arguments_syntax1):
        pass

    class python_arguments_syntax1_element2(python_arguments_syntax1):
        pass

    class python_arguments_syntax1_element3(python_arguments_syntax1):
        pass

    class specific_language(ObjectProperty, FunctionalProperty):
        domain = [onto.language_grammar]
        range = [onto.programming_language]

    class has_element(ObjectProperty, FunctionalProperty):
        domain = [onto.language_parser]
        range = [onto.language_grammar, onto.variable]

    for key, value in keywords_dict.items():
        exec(f"types.new_class('python_{key}', tuple([python_keywords]))")
        exec(f"onto.python_{key}('{value}', specific_language=onto.python)")

    for key, value in operators_dict.items():
        exec(f"types.new_class('python_{key}', tuple([python_operators]))")
        exec(f"onto.python_{key}('{key.lower()}', specific_language=onto.python)")

    for key, value in other_symbols_dict.items():
        exec(f"types.new_class('python_{key}', tuple([python_other_symbols]))")
        exec(f"onto.python_{key}('{key.lower()}', specific_language=onto.python)")

onto.save(file="1. Ontology Files/Programming Language Parser.owl")
