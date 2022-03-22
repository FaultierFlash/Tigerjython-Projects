zahl = 16
field_x = zahl%8
if field_x == 0:
    field_x = 8
if zahl%8 == 0:
    field_y = (zahl//9)+1
else:
    field_y = (zahl//8)+1
print(field_x)
print(field_y)

