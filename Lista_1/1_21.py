import turtle


length = eval(input("Podaj długość boku: "))
n_sides = 4 # ilość boków

turtle.speed(2) # ustal prędkość żółwia

# powtórz n_sides razy
for i in range(n_sides):
    turtle.forward(length) # narysuj linię o danej długości
    turtle.right(90)       # obróć się w prawo o dany kąt


# trojkat
length_triangle = float(input("Podaj długość boku: "))
n_sides = 3

turtle.speed(2)

for i2 in range(n_sides):
    turtle.forward(length_triangle)
    turtle.right(120)



#wielokat foremny
length_polygon = eval(input("Podaj długość boku: "))
n_sides = int(input("Podaj ilość boków: "))
angle = 180 - (((n_sides - 2)*180) / n_sides)

turtle.speed(2)

for i3 in range(n_sides):
    turtle.forward(length_polygon)
    turtle.right(angle)

turtle.clear()

# wielokat foremny + obrót
length_polygon = eval(input("Podaj długość boku: "))
n_sides = int(input("Podaj ilość boków: "))
angle = 180 - (((n_sides - 2) * 180) / n_sides)
n_polygons = int(input("Podaj ilość wielokątów: "))
angle_n_polygons = 360/n_polygons

turtle.speed(20)
for i4 in range(n_polygons):
    turtle.right(angle_n_polygons)
    for i5 in range(n_sides):
        turtle.forward(length_polygon)
        turtle.right(angle)

turtle.mainloop()
