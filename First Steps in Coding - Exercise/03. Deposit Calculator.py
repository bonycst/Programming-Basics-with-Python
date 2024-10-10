deposit_sum = float(input())
deposit_period = int(input())
yearly_percent = float(input())

total_sum = deposit_sum + deposit_period*((deposit_sum*(yearly_percent/100)/12))

print(total_sum)