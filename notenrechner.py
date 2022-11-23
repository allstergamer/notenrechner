

def opt2():
    print()
    points = input("wie viele Punkte hat der Test?:")
    sechs = int(points) / 6
    fuenf = sechs * 2
    vier = sechs * 3
    drei = sechs * 4
    zwei = sechs * 5
    eins = sechs * 6
    
    print("hier hast du alle Noten und die passende Punktzahl")
    print("note 1 endspricht höchstens ", round(eins), " Punkten")
    print("note 2 endspricht höchstens ", round(zwei), " Punkten")
    print("note 3 endspricht höchstens ", round(drei), " Punkten")
    print("note 4 endspricht höchstens ", round(vier), " Punkten")
    print("note 5 endspricht höchstens ", round(fuenf), " Punkten")
    print("note 6 endspricht höchstens ", round(sechs), " Punkten")
    

def opt1():
    print()
    points = input("wie viele Punkte hat der Test:")
    pro_note = int(points) / 6
    note = input("welche Note willst du wissen")
    fuenf = pro_note * 2
    vier = pro_note * 3
    drei = pro_note * 4
    zwei = pro_note * 5
    
    if note == "1":
        print("die Punkte für note ", note, " entspricht mindestens", round(zwei), " Punkten!")
    elif note == "2":
        print("die Punkte für note ", note, " entspricht mindestens", round(drei), " Punkten!")
    elif note == "3":
        print("die Punkte für note ", note, " entspricht mindestens", round(vier), " Punkten!")
    elif note == "4":
        print("die Punkte für note ", note, " entspricht mindestens", round(fuenf), " Punkten!")
    elif note == "5":
        print("die Punkte für note ", note, " entspricht mindestens", round(sechs), " Punkten!")
    elif note == "6":
        print("die Punkte für note ", note, " entspricht mindestens 0 Punkten!")
    else:
        print("deine Eingabe endspricht keiner Note")


print("willst du wissen wie viele Punkte du für eine bestimmte Note benötigst?")
print("schreibe opt1")
print("willst du alle Noten und die dazugehörigen Punkte wissen?")
option = input("schreibe opt2    ")

if option == "opt1":
    opt1()
elif option == "opt2":
    opt2()
else:
    print("das ist eine falsche Angabe")
