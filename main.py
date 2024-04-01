import colorgram as cg

colorsExtracted = []
colors = cg.extract('image.jpg', 10)
print(colors[0].rgb)


for i in range(len(colors)):
    Append = colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b
    colorsExtracted.append(Append)

print(colorsExtracted)