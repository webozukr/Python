from datetime import datetime
now = int(input("Введіть номер дня тижня: "))

match now:
    case 0:
        print("Сьогодні у нас понеділок")
    case 1:
        print("Сьогодні у нас вівторок")
    case 2:
        print("Сьогодні у нас середа")
    case 3:
        print("Сьогодні у нас четвер")
    case 4:
        print("Сьогодні у нас п'ятниця")
    case 5:
        print("Сьогодні у нас субота")
    case 6:
        print("Сьогодні у нас п'неділя")
    