colors = ('красный', 'синий', 'желтый')
c1 = input()
c2 = input()
if c1 in colors and c2 in colors:
    if c1 != c2:
        if (c1 in ("красный", "синий")) and (c2 in ("красный", "синий")):
         print("фиолетовый")
     elif (c1 in ("желтый", "красный")) and (c2 in ("желтый", "красный")):
         print("оранжевый")
     elif (c1 in ("синий", "желтый")) and (c2 in ("синий", "желтый")):
        print("зеленый")
    else:
        print(c1)
else:
    print("ошибка цвета")
