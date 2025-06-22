def calculate_average(numbers: list[float]) -> int | None:
    """Возвращает округлённое в меньшую сторону среднее арифметическое."""
    if not numbers:
        return None
    average = sum(numbers) / len(numbers)
    result = int(average)
    print("Tested by Denis Korablev")
    return result
