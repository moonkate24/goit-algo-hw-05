import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'(?<= )\d+\.\d+(?= )'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    return sum(func(text))

# Example usage:
text = "Employee's total income consists of several parts: 1000.01 as basic income, supplemented with additional earnings of 27.45 and 324.00 dollars."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")
