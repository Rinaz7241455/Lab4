# Контрольный пример (Фотография 2)
# Исходный массив [4, 2, 7, 2, 9, 5], удаление x = 2

arr = [4, 2, 7, 2, 9, 5]
x = 2
print(f"Исходный массив: {arr}")

write_idx = 0
removed_count = 0
for read_idx in range(len(arr)):
    if arr[read_idx] != x:
        arr[write_idx] = arr[read_idx]
        write_idx += 1
    else:
        removed_count += 1

arr = arr[:write_idx]

print("--- Результаты обработки массива ---")
print(f"Удалено элементов (равных {x}): {removed_count}")
print(f"Итоговый массив после сдвига: {arr}")
print(f"Новая длина массива: {len(arr)}")
