neobhodim_nailon = (float(input()) + 2) * 1.50
neohodima_boq = float(input())
boq = (neohodima_boq + (neohodima_boq * 0.10)) * 14.50
razreditel = float(input()) * 5
hours = int(input())
bag = float(0.40)
materials_sum = neobhodim_nailon + boq + razreditel + bag
workers_sum = (materials_sum * 0.30) * hours
final_price = materials_sum + workers_sum
print(final_price)