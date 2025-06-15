def calculate_average(numbers: list[float]) -> int | None:
    if not numbers:
        return None
    result = sum(numbers) / len(numbers)
    average = round(result)
    print("Tested by Denis Korablev")
    return average
