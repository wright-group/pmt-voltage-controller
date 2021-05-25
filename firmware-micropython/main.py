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

# DAC ---------------------------------------------------------------------------------------------

spi = machine.SPI(pins=(l

void init_dac(int slave_select) {
  digitalWrite(slave_select, HIGH);
  delay(500);
  // software full reset
  digitalWrite(slave_select, LOW);
  delay(1);
  SPI.transfer(0b00001111);  // software full reset
  SPI.transfer(0x0);  // irrelevant
  SPI.transfer(0x0);  // irrelevant
  delay(1);
  digitalWrite(slave_select, HIGH);
  delay(1000);
  // write to control register
  digitalWrite(slave_select, LOW);
  delay(1);
  SPI.transfer(0b00000100);  // write to control register
  SPI.transfer(0b00000000);
  SPI.transfer(0b11000001);
  delay(1);
  digitalWrite(slave_select, HIGH);
}

void setDAC(int SSpin, float percent) {
  number = (long) percent * 655.35;
  number = number < 65536 ? number : 65535;  // clamp at 65535
  digitalWrite(SSpin, LOW);
  delay(1);
  SPI.transfer(0x03);  // write and update DAC register
  SPI.transfer16(number);
  delay(1);
  digitalWrite(SSpin, HIGH);
}
