import colorgram

# Extract colors from an image
colors = colorgram.extract('hirst painting.jpg', 10)  # 10 = number of colors to extract

# Convert colors to RGB tuples
rgb_colors = []
for color in colors:
    rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
    rgb_colors.append(rgb)

print(rgb_colors)