import IntegerManipulator

# Wolałbym zrobić listę, ale nie wolno :<

num1 = 110
num2 = 270
num3 = 330

myNumbers = IntegerManipulator.Manipulator(num1, num2, num3)
print(f"Największym dzielnikiem liczb {num1}, {num2} i {num3} jest: {myNumbers.nwd()}")
