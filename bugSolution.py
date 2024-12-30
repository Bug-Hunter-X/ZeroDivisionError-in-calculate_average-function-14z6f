def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list gracefully
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = []
result = calculate_average(my_numbers)
print(f"Average: {result}")

my_numbers = [10, 20, 30]
result = calculate_average(my_numbers)
print(f"Average: {result}") # Added test with non-empty list