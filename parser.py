from owlready2 import *
import types

onto = get_ontology("http://www.haozhang.me/Programming_Language_Parser.owl#")

keywords_dict = dict(
    DEF = "def",
    RETURN = "return",
    RAISE = "raise",
    FROM = "from",
    IMPORT = "import",
    NONLOCAL = "nonlocal",
    AS = "as",
    GLOBAL = "global",
    ASSERT = "assert",
    IF = "if",
    ELIF = "elif",
    ELSE = "else",
    WHILE = "while",
    FOR = "for",
    IN = "in",
    TRY = "try",
    NONE = "None",
    FINALLY = "finally",
    WITH = "with",
    EXCEPT = "except",
    LAMBDA = "lambda",
    OR = "or",
    AND = "and",
    NOT = "not",
    IS = "is",
    CLASS = "class",
    YIELD = "yield",
    DEL = "del",
    PASS = "pass",
    CONTINUE = "continue",
    BREAK = "break",
    ASYNC = "async",
    AWAIT = "await",
    PRINT = "print",
    EXEC = "exec",
    TRUE = "True",
    FALSE = "False",
)

with onto:

    class python_grammar(Thing):
        pass

    class python_lexer(python_grammar):
        pass

    class keywords(python_lexer):
        pass

    class python_parser(python_grammar):
        pass


print(keywords_dict)


onto.save(file="1. Ontology Files/Programming Language Parser.owl")
