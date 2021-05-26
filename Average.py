# Найти среднее арифметическое числовых значений в списке
list = [10, 15, 'green', '12.5', 38, 33.2, 'red', 'yellow']

def main():
    result = []
    for item in list:
        if type(item) in [int, float]:
            result.append(item)

    print(sum(result) / len(result))

main()