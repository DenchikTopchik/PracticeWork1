# Открыть файл
with open('nums.txt', 'r') as f:
   # Прочитать содержимое файла
   nums = f.read().split(' ')
   # Преобразовать строки в числа
   nums = list(map(int, nums))
   # Подсчитать и вывести общую сумму чисел
   print(sum(nums))