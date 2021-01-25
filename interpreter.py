__author__="Dhananjay(DJAY) Gurung"

import parser
import scanner
import math
import sys

space = {}


def delete(tree):
    if tree:
        delete(tree.leftchild)
        delete(tree.midchild)
        delete(tree.rightchild)
        tree.key = None


cnt = 0


def interpreter(tree):
    global cnt
    if tree.key is None:
        return
    if tree.key == "WHILE-LOOP" or tree.key == "IF-STATEMENT" or tree.key == "SKIP":
        temp = "".join(tree.key)
    else:
        temp = "".join(tree.key[0])
    if temp == ":=":
        val = findval(tree.rightchild)
        dict1 = {"".join(tree.leftchild.key[0]): val}
        space.update(dict1)
        if cnt == 0:
            delete(tree)
    if temp == "IF-STATEMENT":
        evaluateif(tree)
        if cnt == 0:
            delete(tree)
        return
    if temp == "WHILE-LOOP":
        evaluatewhile(tree)
        if cnt == 0:
            delete(tree)
        return
    if temp == "SKIP":
        delete(tree)
        return
    if tree.leftchild:
        interpreter(tree.leftchild)

    if tree.midchild:
        interpreter(tree.midchild)

    if tree.rightchild:
        interpreter(tree.rightchild)


def findval(tree):
    if tree.key is None:
        return
    val = 0
    temp = "".join(tree.key[0])
    if scanner.imp_lexer(temp)[0][1] == "NUMBER":
        return temp

    lefttemp = "".join(tree.leftchild.key[0])
    lefttemp = scanner.imp_lexer(lefttemp)[0][0]
    righttemp = "".join(tree.rightchild.key[0])
    righttemp = scanner.imp_lexer(righttemp)[0][0]
    if lefttemp == "+":
        n = findval(tree.leftchild)
        if scanner.imp_lexer(righttemp)[0][1] == "IDENTIFIER":
            val = n + int(space.get(righttemp))
        if scanner.imp_lexer(righttemp)[0][1] == "NUMBER":
            val = n + int(righttemp)
    if lefttemp == "-":
        n = findval(tree.leftchild)
        if scanner.imp_lexer(righttemp)[0][1] == "IDENTIFIER":
            val = n - int(space.get(righttemp))
        if scanner.imp_lexer(righttemp)[0][1] == "NUMBER":
            val = n - int(righttemp)
    if lefttemp == "*":
        n = findval(tree.leftchild)
        if scanner.imp_lexer(righttemp)[0][1] == "IDENTIFIER":
            val = n * int(space.get(righttemp))
        if scanner.imp_lexer(righttemp)[0][1] == "NUMBER":
            val = n * int(righttemp)

    if temp == "+":
        if scanner.imp_lexer(lefttemp)[0][1] == "NUMBER" and scanner.imp_lexer(righttemp)[0][1] == "NUMBER":
            val = int(lefttemp) + int(righttemp)
        elif scanner.imp_lexer(lefttemp)[0][1] == "IDENTIFIER" and scanner.imp_lexer(righttemp)[0][1] == "NUMBER":
            val = int(space.get(lefttemp)) + int(righttemp)
        elif scanner.imp_lexer(lefttemp)[0][1] == "NUMBER" and scanner.imp_lexer(righttemp)[0][1] == "IDENTIFIER":
            val = int(lefttemp) + int(space.get(righttemp))
        elif scanner.imp_lexer(lefttemp)[0][1] == "IDENTIFIER" and scanner.imp_lexer(righttemp)[0][1] == "IDENTIFIER":
            val = int(space.get(lefttemp)) + int(space.get(righttemp))
    if temp == "-":
        if scanner.imp_lexer(lefttemp)[0][1] == "NUMBER" and scanner.imp_lexer(righttemp)[0][1] == "NUMBER":
            val = int(lefttemp) - int(righttemp)
        elif scanner.imp_lexer(lefttemp)[0][1] == "IDENTIFIER" and scanner.imp_lexer(righttemp)[0][1] == "NUMBER":
            val = int(space.get(lefttemp)) - int(righttemp)
        elif scanner.imp_lexer(lefttemp)[0][1] == "NUMBER" and scanner.imp_lexer(righttemp)[0][1] == "IDENTIFIER":
            val = int(lefttemp) - int(space.get(righttemp))
        elif scanner.imp_lexer(lefttemp)[0][1] == "IDENTIFIER" and scanner.imp_lexer(righttemp)[0][1] == "IDENTIFIER":
            val = int(space.get(lefttemp)) - int(space.get(righttemp))
    if temp == "*":
        if scanner.imp_lexer(lefttemp)[0][1] == "NUMBER" and scanner.imp_lexer(righttemp)[0][1] == "NUMBER":
            val = int(lefttemp) * int(righttemp)
        elif scanner.imp_lexer(lefttemp)[0][1] == "IDENTIFIER" and scanner.imp_lexer(righttemp)[0][1] == "NUMBER":
            val = int(space.get(lefttemp)) * int(righttemp)
        elif scanner.imp_lexer(lefttemp)[0][1] == "NUMBER" and scanner.imp_lexer(righttemp)[0][1] == "IDENTIFIER":
            val = int(lefttemp) * int(space.get(righttemp))
        elif scanner.imp_lexer(lefttemp)[0][1] == "IDENTIFIER" and scanner.imp_lexer(righttemp)[0][1] == "IDENTIFIER":
            val = int(space.get(lefttemp)) * int(space.get(righttemp))
    if temp == "/":
        if scanner.imp_lexer(lefttemp)[0][1] == "NUMBER" and scanner.imp_lexer(righttemp)[0][1] == "NUMBER":
            val = math.floor(int(lefttemp) / int(righttemp))
        elif scanner.imp_lexer(lefttemp)[0][1] == "IDENTIFIER" and scanner.imp_lexer(righttemp)[0][1] == "NUMBER":
            val = math.floor(int(space.get(lefttemp)) / int(righttemp))
        elif scanner.imp_lexer(lefttemp)[0][1] == "NUMBER" and scanner.imp_lexer(righttemp)[0][1] == "IDENTIFIER":
            val = math.floor(int(lefttemp) / int(space.get(righttemp)))
        elif scanner.imp_lexer(lefttemp)[0][1] == "IDENTIFIER" and scanner.imp_lexer(righttemp)[0][1] == "IDENTIFIER":
            val = math.floor(int(space.get(lefttemp)) / int(space.get(righttemp)))
    if val < 0:
        val = 0
    return val


def evaluateif(tree):
    temp1 = tree.leftchild
    n = findval(temp1)
    if n > 0:
        interpreter(tree.midchild)
    if n == 0:
        interpreter(tree.rightchild)


def evaluatewhile(tree):
    global cnt
    cnt = 0
    n = 1
    temptree = tree
    if tree.leftchild:
        temptree.midchild = tree.leftchild.clonetree()
    if tree.rightchild:
        temptree.rightchild = tree.rightchild.clonetree()
        temptree.leftchild = tree.rightchild.clonetree()
    while n > 0:
        n = findval(temptree.midchild)
        if n > 0:
            cnt = 1
            interpreter(temptree.rightchild)
            cnt = 0
        if n == 0:
            return


def main():
    inputfilename = sys.argv[1]
    outputfilename = sys.argv[2]
    infile = open(inputfilename, "r")
    outfile = open(outputfilename, "w+")
    datafile = infile.read()
    tokens = scanner.imp_lexer(datafile)
    outfile.write("Tokens:\n")
    for j in range(len(tokens)):
        outfile.write(tokens[j][1] + " " + tokens[j][0] + "\n")
    outfile.write("\n\n\n")
    tree = parser.parser(outfile, tokens)
    outfile.write("\n\nAST:\n")
    tree.printt(outfile)
    interpreter(tree)
    outfile.write("\n\nOutput: \n")
    for key, val in space.items():
        print(key, "=", val)
        outfile.write(str(key) + " = " + str(val) + "\n")
    infile.close()
    outfile.close()


if __name__ == '__main__':
    main()
