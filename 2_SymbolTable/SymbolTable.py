"""@author : ANISHK YADAV"""
# Create Two Empty Lists To Store The Tokens And Identifiers
tokens = [' ']
iden = []

# Lists To Check For Keywords, Opeartors, Punctuation
key_words = ["int", "str", "char", "float", "double",
             "bool", "long", "short", "do", "if", "else", "class", "static", "void", "main", "args", "String"]
operators = ["+", "-", "*", "/", "=", "<", ">", "%",
             "+=", "-=", "*=", "/=", "++", "--", "|", "&&"]
punct = ["(", ")", "{", "}", "[", "]", ",", ";", ":"]

# Open The Input Code File
with open(r".\sym.txt") as t:
    reader = t.readlines()
    for t in reader:
        # Split The Tokens From The Input Code
        tokens = tokens + (t.split(" "))

# Header For Symbol Table
print("ID        Data_Types              Value            Return_Type           N_Parameter            T_Parameter")

# Loop Through The Tokens List
for pos, t in enumerate(tokens):
    for word in key_words:
        if(t == word):
            iden.append(tokens[pos + 1])

            if(tokens[pos + 2] == ','):
                print(tokens[pos + 1] + " " + tokens[pos] + "      " + "NULL")
                tokens.insert(pos + 3, tokens[pos])

            elif (tokens[pos + 2] == '('):
                end = tokens.index(')')
                para = tokens[pos + 3:end]
                key_count = 0
                pt = []
                for key in key_words:
                    key_count = key_count + para.count(key)
                    i = 0
                    while(i < para.count(key)):
                        pt.append(key)
                        i = i + 1
                    print(tokens[pos + 1] + "              " + tokens[pos] +
                          "         " + str(key_count) + "          " + str(pt))

            elif (tokens[pos + 1] == '('):
                continue

            else:
                print(tokens[pos + 1] + "               " +
                      tokens[pos] + "                " + tokens[pos + 3])
