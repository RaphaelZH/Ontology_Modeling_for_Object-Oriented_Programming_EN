from owlready2 import *

onto = get_ontology("http://www.haozhang.me/Programming_Language_Parser.owl#")


def ontology_generator():
    with onto:

        class programming_language(Thing):
            pass

        class language_grammar(Thing):
            pass

        class language_lexer(language_grammar):
            pass

        class language_parser(language_grammar):
            pass

        class variable(Thing):
            pass

    return onto
