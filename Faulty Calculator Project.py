#Coding Projects
#                                                                  Assignment - Faulty Calculator:

# Question: Solve given problem:

# Design a calculator which will correctly solve all the problems except
# The following ones:
# 45 * 3 = 555, 56 + 9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result:

print("Enter your first number:")
num1 = int(input())
print("Enter your second number:")
num2 = int(input())
print("Tell what you want: +,-,*,/, % ")
num3 = input()

if num1 == 45 and num2 == 3 and  num3 == "*":
    print(555)
elif num1 == 56 and num2 == 9 and num3 == "+":
    print(77)
elif num1 == 56 and num2 == 6 and num3 == "/":
    print(4)
elif num3 == "+":
    print("Your Answer is", num1 + num2,)
elif num3 == "-":
    print("Your Answer is", num1 - num2)
elif num3 == "*":
    print("Your Answer is", num1 * num2)
elif num3 == "/":
    print("Your Answer is", num1 / num2)
elif num3 == "%":
    print("Your Answer is", num2 % num1)
else:
    print("You had enterd invalid number")
                # THE END
