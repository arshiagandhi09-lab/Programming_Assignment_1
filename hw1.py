"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data
import math


# Part 1: vowel_count
def vowel_count(text: str) -> int:
    # Purpose: count the vowels (a, e, i, o, u) in a string, ignoring case
    # Input: text
    # Output: the number of vowel characters in text
    count = 0
    for character in text:
        if character.lower() in 'aeiou':
            count += 1
    return count


# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    # Purpose: keep only the nested lists that contain exactly two values
    # Input: items
    # Output: a new list holding the nested lists of length 2 in their original order
    result = []
    for nested in items:
        if len(nested) == 2:
            result.append(nested)
    return result


# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    # Purpose: put the values of every two-element nested list in non-descending order
    # Input: items
    # Output: a new list in the same outer order where each length-2 nested list is sorted ascending
    result = []
    for nested in items:
        if len(nested) == 2 and nested[0] > nested[1]:
            result.append([nested[1], nested[0]])
        else:
            result.append(list(nested))
    return result


# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    # Purpose: add two prices, carrying excess cents into dollars
    # Input: first and second
    # Output: a new Price equal to the sum, with cents between 0 and 99
    total_cents = first.cents + second.cents
    dollars = first.dollars + second.dollars + total_cents // 100
    return data.Price(dollars, total_cents % 100)
 
 
# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # Purpose: compute the area of rectangle
    # Input: rectangle
    # Output: the area
    width = rectangle.bottom_right.x - rectangle.top_left.x
    height = rectangle.top_left.y - rectangle.bottom_right.y
    return width * height
 
 
# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # Purpose: find all books that list a given author
    # Input: author and books
    # Output: a new list of the books whose authors include author
    result = []
    for book in books:
        if author in book.authors:
            result.append(book)
    return result
 
 
# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # Purpose: find the smallest circle that encloses a rectangle
    # Input: rectangle
    # Output: a new Circle centered at the rectangle's center whose radius is the distance from that center to a corner
    top_left = rectangle.top_left
    bottom_right = rectangle.bottom_right
    center_x = (top_left.x + bottom_right.x) / 2
    center_y = (top_left.y + bottom_right.y) / 2
    radius = math.hypot(top_left.x - center_x, top_left.y - center_y)
    return data.Circle(data.Point(center_x, center_y), radius)
 
 
# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # Purpose: find the employees paid strictly less than the average pay
    # Input: employees
    # Output: a list of the names of employees whose pay_rate is below the average pay_rate
    if len(employees) == 0:
        return []
    average = sum(employee.pay_rate for employee in employees) / len(employees)
    result = []
    for employee in employees:
        if employee.pay_rate < average:
            result.append(employee.name)
    return result
