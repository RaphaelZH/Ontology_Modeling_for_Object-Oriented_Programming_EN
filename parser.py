from owlready2 import *
from pyswip import Prolog
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

    class python_arglist_cls(python_parser):
        pass

    ### test
    python_arglist_cls("python_arglist_ind", specific_language=onto.python)

    class python_stmt(python_parser):
        pass

    class python_simple_stmt(python_stmt):
        pass

    class python_compound_stmt(python_stmt):
        pass

    class python_suite_cls(python_parser):
        pass

    ### test
    python_suite_cls("python_suite_ind", specific_language=onto.python)

    class python_suite_syn1(python_suite_cls):
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
        equivalent_to = [python_arglist_cls]

    class python_classdef_cls4(python_classdef_cls):
        equivalent_to = [onto.python_COLON]

    class python_classdef_cls5(python_classdef_cls):
        equivalent_to = [python_suite_cls]

    python_classdef_ind = python_classdef_cls(
        "python_classdef_ind", specific_language=onto.python
    )

    for i in range(1, len(list(python_classdef_cls.subclasses())) + 1):
        exec(
            f"python_classdef_ind{i} = python_classdef_cls{i}('python_classdef_ind{i}', \
                equivalent_to = python_classdef_cls{i}.equivalent_to[0].instances())"
        )

        exec(f"python_classdef_ind.syntax_container.append(python_classdef_ind{i})")

        if i == 1:
            exec(f"python_classdef_ind.syntactic_chain = [python_classdef_ind{i}]")
        else:
            exec(f"python_classdef_ind{i-1}.syntactic_chain = [python_classdef_ind{i}]")

    class python_funcdef(python_parser):
        pass


for ind in onto.individuals():
    if ind.equivalent_to != []:
        for prop in ind.equivalent_to[0].get_properties():
            exec(
                f"onto.{ind.name}.{prop.name} = onto.{ind.equivalent_to[0].name}.{prop.name}"
            )
        if ind.string_value is None:
            variable_text = "{" + ind.equivalent_to[0].name + "}"
            exec(f"onto.{ind.name}.string_value = '{variable_text}'")

onto.save(file="1. Ontology Files/Programming Language Parser.owl")

del onto

prolog = Prolog()
prolog.assertz("ancestor(A, D) :- parent(A, D)")
prolog.assertz("ancestor(A, D) :- parent(A, P), ancestor(P, D)")

onto = get_ontology("1. Ontology Files/Programming Language Parser.owl").load()

with onto:
    for individual in onto.individuals():
        if individual.name == "python_classdef_ind":
            prolog.assertz(
                f"parent({individual.name}, {individual.syntactic_chain[0].name})"
            )
            for ind in individual.syntax_container:
                if len(ind.syntactic_chain) > 0:
                    prolog.assertz(f"parent({ind.name}, {ind.syntactic_chain[0].name})")

    descendant_list = []
    for q in prolog.query("ancestor(python_classdef_ind, X)"):
        exec(f"descendant_list.append(onto.{q['X']}.string_value)")

    print(descendant_list)

    
