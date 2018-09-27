import module_3_1

with open("fahrenheit.txt", 'r') as t1:
    read1 = [i.rstrip('\n') for i in t1.readlines()]


l1 = []
for i in read1:
    l1.append(module_3_1.fahr_cel(float(i)))


with open("celcjusz.txt", 'r') as t2:
    read2 = [float(i2.rstrip('\n')) for i2 in t2.readlines()]

for i in range(len(l1)):
    d = read2[i] - l1[i]
    d = round(d, 4)
    if d == 0:
       pass
    else:
        print("Incorrect")
print("Correct")