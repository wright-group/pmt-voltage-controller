import machine
import utime as time

# 7seg --------------------------------------------------------------------------------------------

i2c = machine.I2C(0, scl=machine.Pin(5), sda=machine.Pin(4), freq=400_000)

def write_7seg(i):
    assert i < 10_000
    assert i >= 0
    i2c.writeto(0x71, b"\x76")  # clear display
    for c in "{:04d}".format(i):
        i2c.writeto(0x71, c.encode())



# DAC -------------------------------------------------------------------------------------------


from machine import Pin, Timer

led = Pin(25, Pin.OUT)
tim = Timer()
def tick(timer):
    global led
    led.toggle()

tim.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)


i = 0
while True:
    i += 1
    write_7seg(i)
    time.sleep(1)
