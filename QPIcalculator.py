gradeequivalents = {"A": str(4), "B+": str(3.5), "B": str(3), "C+": str(2.5), "C": str(2), "D": str(1.5), "F": str(1)}
print(gradeequivalents)
print()
print("type x in \"Grade\" to exit the code!")

QPI = 0
units = 0
sum2 = 0
units1 = 0
qpiequivalent = 0
leave = "n"

print("")
while leave.upper() == "N":
    grade = str(input("Grade: ")).upper()
    if grade == "A":
        qpiequivalent = 4
    elif grade == "B+":
        qpiequivalent = float(3.5)
    elif grade == "B":
        qpiequivalent = 3
    elif grade == "C+":
        qpiequivalent = float(2.5)
    elif grade == "C":
        qpiequivalent = 2
    elif grade == "D":
        qpiequivalent = float(1.5)
    elif grade == "F":
        qpiequivalent = 0
    elif grade == "X":
        print("Final qpi = {:.2f}".format(QPI))
        break
    else:
        print("Invalid input")
        break


    units = int(input("Units: "))
    if int(units) == str:
        print("Invalid input")
        break
    else:
        sum1 = qpiequivalent * units
        units1 += units
        sum2 += sum1
        QPI = sum2 / units1
        print("QPI: {:.2f}".format(QPI))
        print("")
