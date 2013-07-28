#calculator challenge from Arpad
from math import sqrt
arpad=1
print "Welcome to my fucking calculator"
while arpad == 1:
    ask_op = raw_input("Type +,-,*,/,sqrt")
    if ask_op == "+"or "-" or "*" or "/" or "sqrt":

        #addition
        if ask_op == "+":
            plus1 = raw_input("First Number:")
            plus2 = raw_input("Second Number: ")
            int(plus1)
            int(plus2)
            print (int(plus1) + int(plus2))

        #subtraction
        if ask_op == "-":
            min1 = raw_input("First Number:")
            min2 = raw_input("Second Number:")
            int(min1)
            int(min2)
            print (int(min1))-(int(min2))

        #multiplication
        if ask_op == "*":
            times1 = raw_input("First Number:")
            times2 = raw_input("Second Number:")
            int(times1)
            int(times2)
            print (int(min1))*(int(min2))
        
        #division MAKE THIS SHOW REMAINDER!!!
        if ask_op == "/":
            div1 = raw_input("First Number:")
            div2 = raw_input("Second Number:")
            int(div1)
            int(div2)
            print (int(div1))/(int(div2)),
            print "and",
            print (int(div1))%(int(div2)),
            print "is remainder",

        #square root this bitch
        if ask_op == "sqrt":
            sq1 = raw_input("Square Root of:")
            int(sq1)
            print sqrt(int(sq1))
    else:
        print "ERROR: Give me an operation to compute!"

