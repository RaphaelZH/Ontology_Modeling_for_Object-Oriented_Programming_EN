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

    class python_suite_synt1(python_suite):
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

    class python_classdef(python_parser):
        onto.syntax_chain = [onto.python_CLASS]

    class python_classdef_cls1(python_classdef):
        onto.equivalent_to = [onto.python_CLASS]

    python_classdef_indv1 = python_classdef_cls1(
        "python_classdef_indv1",
        equivalent_to=[onto.python_class],
    )

    class python_classdef_element2(python_classdef):
        equivalent_to = [onto.variable_name]

    class python_classdef_element3(python_classdef):
        equivalent_to = [python_arglist]

    class python_classdef_element4(python_classdef):
        equivalent_to = [onto.python_COLON]

    class python_classdef_element5(python_classdef):
        pass

    class python_funcdef(python_parser):
        pass


for indv in onto.individuals():
    if indv.equivalent_to != []:
        for prop in indv.equivalent_to[0].get_properties():
            exec(
                f"onto.{indv.name}.{prop.name} = onto.{indv.equivalent_to[0].name}.{prop.name}"
            )


onto.save(file="1. Ontology Files/Programming Language Parser.owl")
