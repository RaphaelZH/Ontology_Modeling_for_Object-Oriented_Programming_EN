from owlready2 import *
import types

from DictionaryGenerator import python_dictionary_generator

keywords_dict, operators_dict = python_dictionary_generator()

onto = get_ontology("http://www.haozhang.me/Programming_Language_Parser.owl#")

with onto:
    try:
        instance = programming_language()
    except NameError:

        class programming_language(Thing):
            pass

    class python(programming_language):
        pass

    class language_grammar(Thing):
        pass

    class python_grammar(language_grammar):
        pass

    class specific_language(ObjectProperty, FunctionalProperty):
        domain = [language_grammar]
        range = [programming_language]

    class python_lexer(python_grammar):
        pass

    class python_keywords(python_lexer):
        pass

    for key, value in keywords_dict.items():
        exec(f"cls_{key} = types.new_class('python_{key}', tuple([python_keywords]))")
        exec(f"indiv_{value} = cls_{key}('{value}', specific_language=onto.python)")

    class python_parser(python_grammar):
        pass

    class python_operators(python_parser):
        pass

    for key, value in operators_dict.items():
        exec(f"cls_{key} = types.new_class('python_{key}', tuple([python_operators]))")
        exec(
            f"indiv_{key.lower()} = cls_{key}('{key.lower()}', specific_language=onto.python)"
        )

onto.save(file="1. Ontology Files/Programming Language Parser.owl")
