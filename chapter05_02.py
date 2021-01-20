# Chapter 05-02 : Input
# 파이썬 사용자 입력
# Input 사용법
# 기본 타입(str)

# 예제 1
name = input("Enter Your Name : ")
grade = input("Enter Your Grade : ")
company = input("Enter Your Company name : ")

print(name, grade, company)

# 예제 2
number = input("Enter number : ")
name = input("Enter name : ")

print("Type of number :", type(number), number * 3)
print("Type of name :", type(name))

# 예제 3 (계산)
first_number = int(input("Enter number 1 : "))
second_number = int(input("Enter number 2 : "))

total = first_number + second_number
print("first_number + second_number =", total)


# 예제 4
float_number = float(input("Enter a float number : "))
print("input float : ", float_number * 1.1231)
print("input type : ", type(float_number))


# 예제 5
print("FirstName - {0}, LastName - {1}".format(input("Enter first name : "), input("Enter second name : ")))
