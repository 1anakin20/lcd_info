from typing import List
import rpi_lcd

class LCD:
    def __init__(self, address=39, bus=1, width=20, rows=4, backlight=True):
        self.__lcd = rpi_lcd.LCD(address, bus, width, rows, backlight)
        self.__lines = []

    def new_screen(self, lines: List[str] = []):

        if lines != self.__lines:
            self.__lines = lines
            self.__lcd.clear()
            for line in range(len(self.__lines)):
                self.__lcd.text(lines[line], line + 1)
