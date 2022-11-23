import time


def opt2():
    print()
    points = input("wie viele punkte hat der test:")
    sechs = int(points) / 6
    fuenf = sechs * 2
    vier = sechs * 3
    drei = sechs * 4
    zwei = sechs * 5
    eins = sechs * 6
    
    print("hier hast du alle noten und die passende punktzahl")
    print("note 1 endspricht", round(eins), "höchstens Punkten")
    print("note 2 endspricht", round(zwei), "höchstens Punkten")
    print("note 3 endspricht", round(drei), "höchstens Punkten")
    print("note 4 endspricht", round(vier), "höchstens Punkten")
    print("note 5 endspricht", round(fuenf), "höchstens Punkten")
    print("note 6 endspricht", round(sechs), "höchstens Punkten")
    

def opt1():
    print()
    points = input("wie viele punkte hat der test:")
    pro_note = int(points) / 6
    note = input("welche note willst du mindestens haben")
    fuenf = pro_note * 2
    vier = pro_note * 3
    drei = pro_note * 4
    zwei = pro_note * 5
    
    if note == "1":
        print("die punkte für note ", note, " entspricht mindestens", round(zwei), " Punkten!")
    elif note == "2":
        print("die punkte für note ", note, " entspricht mindestens", round(drei), " Punkten!")
    elif note == "3":
        print("die punkte für note ", note, " entspricht mindestens", round(vier), " Punkten!")
    elif note == "4":
        print("die punkte für note ", note, " entspricht mindestens", round(fuenf), " Punkten!")
    elif note == "5":
        print("die punkte für note ", note, " entspricht mindestens", round(sechs), " Punkten!")
    elif note == "6":
        print("die punkte für note ", note, " entspricht mindestens 0 Punkten!")
    else:
        print("deine eingabe endspricht keiner note")


print("willst du wissen wie viele punkte du für eine bestimmte note benötigst?")
print("schreibe opt1")
print("willst du alle noten und die dazugehörigen punkte wissen?")
print("schreibe opt2")


option = input()

if option == "opt1":
    opt1()
elif option == "opt2":
    opt2()
else:
    print("das ist eine falsche angabe")
