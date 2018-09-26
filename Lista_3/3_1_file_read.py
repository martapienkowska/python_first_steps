import module_3_1
with open('celcjusz.txt', 'r') as t:
    read = [i.rstrip('\n') for i in t]

fahrenheit = open("fahrenheit.txt", 'w')
for i in read:
    l = []
    d = module_3_1.cel_fahr(int(i))
    fahrenheit.write(str(d)+"\n")
fahrenheit.close()

