lines = open("modules.txt", "r")
values = lines.readlines()
values = list(map(int, values))
fuelTotal=0
length = len(values)
i=0
for length in values:
    fuel = values[i] / 3 - 2
    fuelTotal=fuelTotal+fuel
    while fuel>1:
        fuel = fuel /3-2
        if fuel>0:
            fuelTotal=fuelTotal+fuel
    i=i+1
print("fuel total", fuelTotal)
