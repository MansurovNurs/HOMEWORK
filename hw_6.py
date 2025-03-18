
# bubble_sort  принимающую в качестве входящего параметра не отсортированный список.

n = 8
numbers = [6, 7, 4, 3, 9, 8, 2,5]
counter = 0
for i in range(n - 1):
    for num in range(n - 1 - i):
        if numbers[num] > numbers[num + 1]:
            counter += 1
            numbers[num],numbers[num + 1] = numbers[num + 1],numbers[num]

print(numbers)
print(counter)


#selection_sort, принимающую в качестве входящего параметра не отсортированный список.



def selection_sort(numbers):
    for num in range(0, len(numbers) - 1):
        min_value = num
        for i in range(num + 1, len(numbers)):
            if numbers[i] < numbers[min_value]:
                min_value = i

        numbers[num], numbers[min_value] = numbers[min_value], numbers[num]



numbers = [7, 5, 4, 8, 3, 9, 2]
selection_sort(numbers)
print(numbers)

# """""" Написать функцию binary_search, принимающую в качестве входящего параметра элемент для поиска и список в котором необходимо искать.

# 5. Алгоритм должен искать с помощью двоичного поиска, изображенного на блок-схеме презентации.

# 6. Функция в итоге должна распечатать результат. Применить 1 раз эту функцию"""""""

def binary_search(self, A, value):
    N = 5000
    resultOK = False
    pos = -1
    first = 0
    last = N - 1

    while first <= last:
        middle = (first + last) // 2

        if value == A[middle]:
            resultOK = True
            pos = middle
            break
        elif value > A[middle]:
            first = middle + 1
        else:
            last = middle - 1

    if resultOK:
        print("Элемент найден в позиции", pos)
    else:
        print("Элемент не найден")

    return pos
