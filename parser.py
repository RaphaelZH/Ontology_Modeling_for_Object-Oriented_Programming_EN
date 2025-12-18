import textwrap
from owlready2 import *
import types

from DictionaryGenerator import python_dictionary_generator
from BasicClassGenerator import ontology_generator

keywords_dict, operators_dict, other_symbols_dict = python_dictionary_generator()

onto = ontology_generator()
with onto:

    class specific_language(ObjectProperty, FunctionalProperty):
        domain = [onto.language_grammar]
        range = [onto.programming_language]

    class has_element(ObjectProperty, FunctionalProperty):
        domain = [onto.language_parser]
        range = [onto.language_grammar, onto.variable]

    class python(onto.programming_language):
        pass

    class python_lexer(onto.language_lexer):
        pass

    class python_keywords(python_lexer):
        pass

    class python_operators(python_lexer):
        pass

    class python_other_symbols(python_lexer):
        pass

    for key, value in keywords_dict.items():
        exec(
            f"types.new_class('python_{key}', \
                tuple([python_keywords]))"
        )
        exec(
            f"onto.python_{key}('python_{key.lower()}', \
                specific_language=onto.python, \
                    string_value='{value}')"
        )

    for key, value in operators_dict.items():
        exec(
            f"types.new_class('python_{key}', \
                tuple([python_operators]))"
        )
        exec(
            f"onto.python_{key}('python_{key.lower()}', \
                specific_language=onto.python, \
                    string_value='{value}')"
        )

    for key, value in other_symbols_dict.items():
        exec(
            f"types.new_class('python_{key}', \
                tuple([python_other_symbols]))"
        )
        exec(
            f"onto.python_{key}('python_{key.lower()}', \
                specific_language=onto.python, \
                    string_value='{value}')"
        )

    class python_parser(onto.language_parser):
        pass

    class python_arguments(python_parser):
        pass

    class python_arglist(python_parser):
        pass

    class python_stmt(python_parser):
        pass

    class python_simple_stmt(python_stmt):
        pass

    class python_compound_stmt(python_stmt):
        pass

    class python_suite(python_parser):
        pass

    class python_suite_syn1(python_suite):
        equivalent_to = [python_simple_stmt]

    """
    class python_suite_syntax2(python_suite):
        equivalent_to = [
            onto.python_LINE_BREAK,
            onto.python_INDENT,
            python_stmt,
            onto.python_DEDENT,
        ]
    """

    class python_classdef_cls(python_parser):
        pass

    class python_classdef_cls1(python_classdef_cls):
        equivalent_to = [onto.python_CLASS]

    class python_classdef_cls2(python_classdef_cls):
        equivalent_to = [onto.variable_name]

    class python_classdef_cls3(python_classdef_cls):
        equivalent_to = [python_arglist]

    class python_classdef_cls4(python_classdef_cls):
        equivalent_to = [onto.python_COLON]

    class python_classdef_cls5(python_classdef_cls):
        equivalent_to = [python_suite]

    class python_funcdef(python_parser):
        pass

    python_classdef_ind = python_classdef_cls("python_classdef_ind")

    for i in range(1, len(list(python_classdef_cls.subclasses())) + 1):
        exec(
            f"python_classdef_ind{i} = python_classdef_cls{i}('python_classdef_ind{i}', \
                equivalent_to = python_classdef_cls{i}.equivalent_to[0].instances())"
        )
        if i == 1:
            exec(f"python_classdef_ind.syntactic_chain = [python_classdef_ind{i}]")
        else:
            exec(f"python_classdef_ind{i-1}.syntactic_chain = [python_classdef_ind{i}]")


for indv in onto.individuals():
    if indv.equivalent_to != []:
        for prop in indv.equivalent_to[0].get_properties():
            exec(
                f"onto.{indv.name}.{prop.name} = onto.{indv.equivalent_to[0].name}.{prop.name}"
            )


onto.save(file="1. Ontology Files/Programming Language Parser.owl")
