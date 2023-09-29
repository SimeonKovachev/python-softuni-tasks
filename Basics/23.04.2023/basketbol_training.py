#taksa za 1 godina = input
#kecovete = price - (price * 0.40)
#ekip = kecovete - kecovete * 0.20
# topka =  ekip * 0.25
# aksesoari = topka * 0.20

yearly_tax = int(input())
sneakers = yearly_tax - (yearly_tax * 0.40)
ekip = sneakers - (sneakers * 0.20)
ball = ekip * 0.25
acsesories = ball * 0.20
final_sum = yearly_tax + sneakers + ekip + ball + acsesories
print(final_sum)