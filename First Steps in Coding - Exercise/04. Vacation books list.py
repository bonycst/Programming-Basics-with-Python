import math

book_pages = int(input())
pages_per_hour = int(input())
days = int(input())

hours_per_all_book = book_pages/pages_per_hour
hours_per_day = hours_per_all_book/days

print(math.floor(hours_per_day))