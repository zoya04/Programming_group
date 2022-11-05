
def math1(num1,num2,operation1):
    if operation1 == "+":
        result1 = num1+ num2
        print(result1)
    elif operation1 == "-":
        result1 = num1 - num2
        print(result1)
    elif operation1 == "*":
        result1 = num1 * num2
        print(result1)
    elif operation1 == "/":
        result1 = num1 / num2
        print(result1)
    else:
        print("Unknown operation") 

print("Enter number one")
user_num1 = float(input())

print("Enter number two")
user_num2 = float(input())

print("Enter operation")
user_operation = input()

math1(user_num1, user_num2, user_operation)


# user_math1 = int(input("Enter math 1 num:"))
# user_math2 = int(input("Enter math 2 num:"))
# user_math3 = int(input("Enter math 3 num:"))
# user_math4 = int(input("Enter math 4 num:"))

# current_thread(user_math1)
# current_thread(user_math2)
# current_thread(user_math3)
# current_thread(user_math4) 


# user_num1 = int(input("Enter num 1:"))
# user_num2 = int(input("Enter num 2 number:"))
# user_num3 = int(input("Enter num 3 number:"))
# user_num4 = int(input("Enter month 4 number:"))

# current_season(user_num1)
# current_season(user_num2)
# current_season(user_num3)
# current_season(user_num4)