# Лабораторная работа № 4. Вариант 8: «Удаление»
# Удаление из одномерного массива элементов, равных x, со сдвигом влево

def main() -> None:
    # Ввод размера массива и его элементов с клавиатуры
    n: int = int(input("Введите количество элементов массива: "))
    arr: list[int] = []
    for i in range(n):
        val: int = int(input(f"Элемент [{i}]: "))
        arr.append(val)

    x: int = int(input("Введите значение x для удаления: "))
    print(f"\nИсходный массив: {arr}")

    # Удаление элементов, равных x, со сдвигом оставшихся элементов влево
    write_idx: int = 0
    removed_count: int = 0
    for read_idx in range(n):
        if arr[read_idx] != x:
            arr[write_idx] = arr[read_idx]
            write_idx += 1
        else:
            removed_count += 1

    # Обрезка массива до новой фактической длины без выхода за границы
    arr = arr[:write_idx]

    # Вывод результатов в читаемом виде с пояснениями
    print("--- Результаты обработки массива ---")
    print(f"Удалено элементов (равных {x}): {removed_count}")
    print(f"Итоговый массив после сдвига: {arr}")
    print(f"Новая длина массива: {len(arr)}")


if __name__ == "__main__":
    main()
