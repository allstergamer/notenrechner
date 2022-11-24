import time

def opt2():

    class colors:

        reset = '\033[0m'
        bold = '\033[01m'
        disable = '\033[02m'
        underline = '\033[04m'
        reverse = '\033[07m'
        strikethrough = '\033[09m'
        invisible = '\033[08m'

        class fg:
            red = '\033[31m'
            green = '\033[32m'
            orange = '\033[33m'
            cyan = '\033[36m'
            lightred = '\033[91m'
            lightgreen = '\033[92m'
            yellow = '\033[93m'

    print()
    points = input("wie viele Punkte hat der test: ")
    sechs = int(points) / 6
    fuenf = sechs * 2
    vier = sechs * 3
    drei = sechs * 4
    zwei = sechs * 5
    eins = sechs * 6
    
    print("hier hast du alle noten und die passende punktzahl")
    print(colors.fg.lightgreen, "note 1 endspricht höchstens ", round(eins), " Punkten und mindestens ", round(zwei + 1))
    print(colors.fg.green, "note 2 endspricht höchstens ", round(zwei), " Punkten und mindestens ", round(drei + 1))
    print(colors.fg.cyan, "note 3 endspricht höchstens ", round(drei), " Punkten und mindestens ", round(vier + 1))
    print(colors.fg.yellow, "note 4 endspricht höchstens ", round(vier), " Punkten und mindestens ", round(fuenf + 1))
    print(colors.fg.red, "note 5 endspricht höchstens ", round(fuenf), " Punkten und mindestens ", round(sechs + 1))
    print(colors.fg.lightred, "note 6 endspricht höchstens ", round(sechs), " Punkten und mindestens 0")
    

def opt1():
    print()
    points = input("wie viele Punkte hat der test: ")
    pro_note = int(points) / 6
    note = input("welche note willst du mindestens haben ")
    fuenf = pro_note * 2
    vier = pro_note * 3
    drei = pro_note * 4
    zwei = pro_note * 5
    
    if note == "1":
        print("die Punkte für note ", note, " entspricht mindestens", round(zwei + 1), " Punkten!")
    elif note == "2":
        print("die Punkte für note ", note, " entspricht mindestens", round(drei + 1), " Punkten!")
    elif note == "3":
        print("die Punkte für note ", note, " entspricht mindestens", round(vier + 1), " Punkten!")
    elif note == "4":
        print("die Punkte für note ", note, " entspricht mindestens", round(fuenf + 1), " Punkten!")
    elif note == "5":
        print("die Punkte für note ", note, " entspricht mindestens", round(pro_note + 1), " Punkten!")
    elif note == "6":
        print("die Punkte für note ", note, " entspricht mindestens 0 Punkten!")
    else:
        print("deine eingabe endspricht keiner note")


print("willst du wissen wie viele Punkte du für eine bestimmte note benötigst?")
print("schreibe opt1")
print("willst du alle noten und die dazugehörigen Punkte wissen?")
print("schreibe opt2")


option = input()

if option == "opt1" or option == "op1" or option == "o1" or option == "1":
    opt1()
elif option == "opt2" or option == "op2" or option == "o2" or option == "2":
    opt2()
else:
    print("das ist eine falsche Angabe")
