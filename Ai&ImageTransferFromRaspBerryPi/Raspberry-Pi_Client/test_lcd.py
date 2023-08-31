from lcd import EggCounterLcd, lcd
from time import sleep


def test_lcd():
    my_lcd = lcd()
    my_lcd.lcd_display_string("Hello world", 1)
    sleep(3)
    my_lcd.lcd_clear()


def test_eggcounterlcd():
    eggcounter = EggCounterLcd()
    eggcounter.egg_count = 4
    eggcounter.show_egg_count()
    sleep(4)
    eggcounter.lcd_clear()


test_lcd()
sleep(3)
test_eggcounterlcd()

