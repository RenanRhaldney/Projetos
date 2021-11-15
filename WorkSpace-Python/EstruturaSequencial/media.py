# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

note1 = int(input("Informed the three grades of student.\n"))
note2 = int(input())
note3 = int(input())
note4 = int(input())
average = int((note1 + note2 + note3 + note4) / 4)
print("The average is {}.".format(average))