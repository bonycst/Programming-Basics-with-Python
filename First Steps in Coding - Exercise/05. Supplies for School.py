count_pens = int(input())
count_markers = int(input())
liters_cleaning_agent = int(input())
percent_discount = int(input())

PRICE_PENS = 5.80
PRICE_MARKERS = 7.20
PRICE_CLEANING_AGENT = 1.20

total_sum = (count_pens*PRICE_PENS + count_markers*PRICE_MARKERS + liters_cleaning_agent*PRICE_CLEANING_AGENT) \
            *(1-percent_discount/100)

print(total_sum)
