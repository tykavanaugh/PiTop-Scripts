#LED Display Test
from ptoled import PTOLEDDisplay
from ptbuttons import PTUpButton, PTDownButton, PTSelectButton, PTCancelButton
from time import sleep
miniScreen = PTOLEDDisplay()
miniScreen.set_max_fps(1) #FPS
canvas = miniScreen.canvas
canvas.set_font_size(20) #Font Size
up = PTUpButton()
up.when_pressed = up_act
down = PTDownButton()
down.when_pressed = down_act
select = PTSelectButton()
select.when_pressed = select_act
cancel = PTCancelButton()
cancel.when_pressed = cancel_act

#button effect
def up_act():
    pass
def down_act():
    pass
def select_act():
    pass
def cancel_act():
    pass


#Output
canvas.clear()
canvas.multiline_text(canvas.top_left(), 'Hello world')
miniScreen.draw()
sleep(5)
canvas.clear()
miniScreen.draw()
