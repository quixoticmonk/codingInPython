
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i, x) in enumerate(color) if i not in (0, 2, 5)]
color2 = [x + x for x in color]
print(color)
print(color2)
