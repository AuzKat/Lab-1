n = int(input("ввод кол слов:")) #вводим количество слов
result = " " #переменная с результатом
for i in range(n): #цикл в количестве n от первой строки
    w = input(f"ввод слов {i+1}:") #переменная которая принимает, значение
    result += w + " " #прибавляем ко второй строке значение строки w
print("результат:", result.strip() ) #выводим результат