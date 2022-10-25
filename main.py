import IntegerManipulator

# Wolałbym zrobić listę, ale nie wolno :<

num_1 = 110
num_2 = 270
num_3 = 330

myNumbers = IntegerManipulator.Manipulator(num_1, num_2, num_3)
print(f"Największym dzielnikiem liczb {num_1}, {num_2} i {num_3} jest: {myNumbers.nwd()}")
