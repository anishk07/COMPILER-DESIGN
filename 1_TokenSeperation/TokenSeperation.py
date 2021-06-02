# -*- coding: utf-8 -*-
"""
Created on JUNE 2 2021

@author: ANISHK YADAV
"""
# For RegEx
import re

# For Storing Tokens
tokens = []

# Splitting Source Code Into Tokens
input_code = 'if ( a > b ) { i = j + 2 ; else j = k - 2 ; }'.split()

# Loop Through Each Token From Source Code
for word in input_code:

    # Check For Datatype
    if word in ["str", "int", "bool", "float", "double", "char", "long"]:
        tokens.append(['DATATYPE', word])

    # Check For Keywords
    if word in ["auto", "break", "case", "catch", "word", "class", "const", "continue", "delete", "do", "if", "else", "enum", "false", "for", "goto", "#include", "namespace", "not", "or", "private", "protected", "public", "return", "short", "signed", "sizeof", "static", "struct", "switch", "true", "try", "unsigned", "void", "while", ]:
        tokens.append(['KEYWORD', word])

    # Check For Identifier
    elif re.match("[a-z]", word) or re.match("[A-Z]", word):
        tokens.append(['IDENTIFIER', word])

    # Check For Non-Identifier
    elif word in ['_', '`', '~', '!', '@', '#', '$', '^', '&', '"', ':', ';', '<', '>', '?']:
        tokens.append(['NON-IDENTIFIER', word])

    # Check For Operator
    elif word in ["+", "-", "*", "/", "%", "+=", "-=", "*=", "/=", "++", "--", "|", "&&", ]:
        tokens.append(['OPERATOR', word])

    # Check For Delimiter
    elif word in ["\t", "\n", "(", ")", "[", "]", "{", "}", "=", ":", ",", ";", "<<", ">>", ]:
        tokens.append(['DELIMITER', word])

    # Check For Numerals
    elif word in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        tokens.append(["NUMERAL", word])

    # Check For Integer Numbers
    elif re.match(".[0-9]", word):
        if word[len(word) - 1] == ';':
            tokens.append(["INTEGER", word[:-1]])
            tokens.append(['END_STATEMENT', ';'])
        else:
            tokens.append(["INTEGER", word])

# Output
for tkn in tokens:
    print(tkn)
