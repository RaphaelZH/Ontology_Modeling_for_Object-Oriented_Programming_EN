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

        class syntax_container(ObjectProperty):
            domain = [language_parser]
            range = [language_parser]

        class syntactic_chain(ObjectProperty, TransitiveProperty):
            domain = [language_parser]
            range = [language_parser]

        class string_value(DataProperty, FunctionalProperty):
            domain = [language_grammar, variable]
            range = [str]

        class variable_name(variable):
            pass

        variable_name("var_name", string_value="{name}")

    return onto
