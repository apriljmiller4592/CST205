#I finished this lab by comparing the rgb values to each other. The highest value is the most
#dominant color in the tuple. For the mustard color, it is most dominantly red. The blue is
#(obviously) most dominantly blue. You can change the values inside of the tuples and the
#correct description of the color will be displayed.

mustard = (252, 186, 3)
color = (2, 55, 100)
print(mustard)

#Mustard color
if mustard[0] > mustard [1] and mustard[0] > mustard[2]:
    print("The color is reddish")
elif mustard[1] > mustard[0] and mustard [1] > mustard[2]:
    print("The color is greenish")
elif mustard[0] == mustard[1] == mustard[2]:
    print("RGB values are equal")
elif mustard[0] == mustard[1]:
    print("The color is a shade of yellow")
elif mustard[0] == mustard[2]:
    print("The color is a shade of magenta")
elif mustard[1] == mustard[2]:
    print("The color is a shade of cyan")
else:
    print("The color is blueish")


#Blueish color
if color[0] > color[1] and color[0] > color[2]:
    print("The color is reddish")
elif color[1] > color[0] and color[1] > color[2]:
    print("The color is greenish")
elif color[0] == color[1] == color[2]:
    print("RGB values are equal")
elif color[0] == color[1]:
    print("The color is a shade of yellow")
elif color[0] == color[2]:
    print("The color is a shade of magenta")
elif color[1] == color[2]:
    print("The color is a shade of cyan")
else:
    print("The color is blueish")