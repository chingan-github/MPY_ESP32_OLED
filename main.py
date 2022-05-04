from machine import Pin, SoftI2C
from time import sleep
import ssd1306

def Show_To_OLED():
    oled.text('Hello, World 1!', 0, 0)
    oled.text('Hello, Chingan!', 0, 10)
    oled.text('Hello, World A!', 0, 20)
   #oled.text('Hello, World 4!', 0, 30)
   #oled.text('Hello, World 5!', 0, 40)
   #oled.text('Hello, World 6!', 0, 50)   
    oled.show()

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。    
    print(f'Hi, {name}, 目前執行 main.py')  # 按 Ctrl+F8 切换断点。

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm , Edit by Chingan')
    
#====================================================================================
print("Hello MicroPython on PyCharm")
print('青安 ' , __name__) 
print_hi('青安') 
led = Pin(2, Pin.OUT)
#
#Init_OLED()
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
#
O_Show_Sta = True
Show_To_OLED()
#oled.text('Hello, World 1!', 0, 0)
#oled.text('Hello, World 2!', 0, 10)
#oled.text('Hello, World 3!', 0, 20)
#oled.show()

while True:
    led.value(not led.value())
    oled.invert(O_Show_Sta)
    O_Show_Sta = not O_Show_Sta
    sleep(1) #Delay 1 秒
    
