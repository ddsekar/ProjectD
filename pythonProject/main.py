def area(base, height, shape="triangle"):
    if(shape == "triangle"):
        area = (1 / 2) * base * height
    else:
        area = base * height
    return area

print(area(2,3, "rectangle"))