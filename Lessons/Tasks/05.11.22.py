# num1 = 0

# while True:
#     num1 += 1
#     print(num1)
#     if num1 ==5:
#         print("End")
#         break
# else:
#     print("cycle ended")
# print("some text")

num1 = 0
bool1 = True
while bool1:
    num1 += 1
    print(num1)
    if num1 ==5:
        print("End")
        bool1 = False
    elif num1 ==3:
        print("some text here")
        continue
    print("some ")
else:
     print("cycle ended")
print("some text")


