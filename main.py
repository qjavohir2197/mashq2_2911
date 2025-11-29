#2-misol
docs = input("Hujjat topshirilganmi? (ha/yo'q): ").lower()
interview = input("Suhbatdan o'tdingizmi? (ha/yo'q): ").lower()
test = input("Testdan o'tdingizmi? (ha/yo'q): ").lower()

if docs == "ha" and interview == "ha" and test == "ha":
    print("Siz ishga qabul qilindingiz!")
elif docs != "ha":
    print("Avvalo hujjatlaringizni topshiring.")
elif interview != "ha":
    print("Suhbatdan o'tmagansiz.")
elif test != "ha":
    print("Test natijalari yetarli emas.")
else:
    print("Jarayon davom etmoqda.")
