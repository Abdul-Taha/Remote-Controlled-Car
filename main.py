import RPi.GPIO as GPIO
import pygame
from time import sleep

# Initialize GPIO pins
in1 = 24
in2 = 23
ena = 25

in3 = 17
in4 = 27
enb = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup([in1, in2, ena, in3, in4, enb], GPIO.OUT)

# PWM setup
pa = GPIO.PWM(ena, 1000)
pb = GPIO.PWM(enb, 1000)
pa.start(100)
pb.start(100)

# Motor control functions
def reverse():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)

def forward():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)

def right():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)

def left():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)

def stop():
    GPIO.output([in1, in2, in3, in4], GPIO.LOW)

# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((100, 100))

# Dictionary to track keys pressed
keys_pressed = {pygame.K_w: False, pygame.K_s: False, pygame.K_a: False, pygame.K_d: False}

# Main loop
try:
    while True:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in keys_pressed:
                    keys_pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                if event.key in keys_pressed:
                    keys_pressed[event.key] = False

        # Check for simultaneous key presses
        if keys_pressed[pygame.K_w]:
            if keys_pressed[pygame.K_s]:
                stop()
            elif keys_pressed[pygame.K_a]:
                left()
            elif keys_pressed[pygame.K_d]:
                right()
            else:
                forward()
        elif keys_pressed[pygame.K_s]:
            if keys_pressed[pygame.K_a]:
                left()
            elif keys_pressed[pygame.K_d]:
                right()
            else:
                reverse()
        elif keys_pressed[pygame.K_a]:
            if keys_pressed[pygame.K_d]:
                stop()
            else:
                left()
        elif keys_pressed[pygame.K_d]:
            right()
        else:
            stop()

        sleep(0.001)
except KeyboardInterrupt:
    GPIO.cleanup()
