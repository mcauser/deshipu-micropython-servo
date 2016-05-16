from machine import PWM
import math


class Servo:
    def __init__(self, pin, freq=50, min_pos=600, max_pos=2400, angle=180):
        self.min_pos = min_pos
        self.max_pos = max_pos
        self.us = 0
        self.freq = freq
        self.angle = angle
        self.pwm = PWM(pin, freq=freq, duty=0)

    def write_us(self, us):
        if us == 0:
            self.pwm.duty(0)
            return
        us = min(self.max_pos, max(self.min_pos, us))
        duty = us * 1024 * self.freq // 1000000
        self.pwm.duty(duty)

    def write_angle(self, degrees=None, radians=None):
        if degrees is None:
            degrees = math.degrees(radians)
        degrees = degrees % 360
        total_range = self.max_pos - self.min_pos
        us = self.min_pos + total_range * degrees // self.angle
        self.write_us(us)
