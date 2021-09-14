from gfxhat import lcd, fonts
from PIL import Image, ImageFont, ImageDraw
from click import getchar

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 15)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()

# Task 1:
def program1():
    displayText('Etch a Sketch', lcd, 0, 20)
    x = 0
    y = 0
    lcd.set_pixel(x, y, 1)
    lcd.show()
    i = 1
    while i < 2:
        button = getchar()
        if button == '\x1b[A':
            y = y - 1
        elif button == '\x1b[B':
            y = y + 1
        elif button == '\x1b[C':
            x = x + 1
        elif button == '\x1b[D':
            x = x - 1
        elif button == 's':
            clearScreen(lcd)
            displayText('Etch a Sketch', lcd, 0, 20)
            x = 0
            y = 0
        elif button == 'q':
            break
        if x > 127:
            x = 0
        elif x < 0:
            x = 127
        if y > 63:
            y = 0
        elif y < 0:
            y = 63
        lcd.set_pixel(x, y, 1)
        lcd.show()

# Task 2:
def program2():
    displayText('Your Object', lcd, 0, 40)
    f1 = [[1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1], [0,1,1,1,1,1,1,0], [1,0,1,1,1,1,0,1], [1,0,0,1,1,0,0,1], [1,0,0,1,1,0,0,1], [0,0,0,1,1,0,0,0], [0,0,0,0,0,0,0,0] ]
    pm = [[0,0,0,1,1,1,1,1,0,0,0], [0,0,1,1,1,1,1,1,1,0,0], [0,1,1,1,1,1,1,1,1,1,0], [1,1,1,1,1,1,1,1,0,0,0], [1,1,1,1,1,1,1,0,0,0,0], [1,1,1,1,1,1,0,0,0,0,0], [1,1,1,1,1,1,0,0,0,0,0], [1,1,1,1,1,1,1,0,0,0,0], [1,1,1,1,1,1,1,1,0,0,0], [0,1,1,1,1,1,1,1,1,1,0], [0,0,1,1,1,1,1,1,1,0,0], [0,0,0,1,1,1,1,1,0,0,0]]
    def displayObject(obj, x, y):
        for list in obj:
            for i in list:
                lcd.set_pixel(x, y, i)
                x = x + 1
            x = users_x
            y = y + 1
        lcd.show()
    users_obj = input('To view the first object, enter A; to view the second object, enter B: ')
    users_x = int(input('Enter x-coordinate: '))
    users_y = int(input('Enter y-coordinate: '))
    if users_obj == 'A':
        displayObject(f1, users_x, users_y)
    elif users_obj == 'B':
        displayObject(pm, users_x, users_y)

# Choose which Lab task to show:
run_program = input('To run the Etch a Sketch program, enter 1; to run the object-display program, enter 2: ')
if run_program == '1':
    program1()
elif run_program == '2':
    program2()

