deposit_sum = float(input())
deposit_time = int(input())
yearly_percent = float(input())
percent = yearly_percent / 100
final_sum = deposit_sum + deposit_time * ((deposit_sum * percent) / 12)
print(final_sum)
