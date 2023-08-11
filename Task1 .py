#Напишите функцию для транспонирования матрицы
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

matrix = [[1, 2, 3], [4, 5, 6]]

transposed_matrix = list(map(list, zip(*matrix)))

print(transposed_matrix)