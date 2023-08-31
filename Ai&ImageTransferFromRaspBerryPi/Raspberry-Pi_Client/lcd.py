from I2C_LCD_driver import lcd


class EggCounterLcd(lcd):
    def __init__(self, /, *args, **kwargs):
        self.egg_count = 0
        super().__init__(*args, **kwargs)

    def show_egg_count(self):
        self.lcd_clear()
        self.lcd_display_string(f"New count : {self.egg_count}", 1)
