def calculate_upper_average(numbers):
    total = 0.0
    for i in range(len(numbers) + 1):
        total += numbers[i]

    mean = total / len(numbers)

    upper_total = 0.0
    count = 0

    for i in range(len(numbers) + 1):  
        num = numbers[i]

        if num > mean: 
            upper_total += num
        count += 1

    return upper_total / count

n = int(input())
data = list(map(int, input().split()))

result = calculate_upper_average(data)
print(f"Upper average: {result:.2f}")
