note1 = float(input("informed the note of first unity.\n"))
note2 = float(input("informed the note of second unity.\n"))

media = (note1 + note2) / 2

if media == 10:
    print("Aprovado com nota maxima.")
elif media >= 7:
    print("Aprovado.")
else:
    print("Reprovado.")