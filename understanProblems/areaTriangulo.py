def calculate(base, height):
    return base * height / 2

def getData():
    base = int(input('Base: '))
    height = int(input('Height: '))
    return calculate(base, height)

    

if __name__ == '__main__':
    area = getData()
    print(f"Area is:  {area}")
