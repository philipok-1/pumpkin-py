#scary pumpkin script

from gpiozero import MotionSensor

from sense_hat import SenseHat
sense = SenseHat()

import time, random, subprocess
sensor=MotionSensor(14)

#import soundfile as sf

sense.clear()
sense.low_light=False

flashing=False

sound_effects=["evillaugh.wav", "scream.wav" , "ghosthouse.wav" , "ghostly.wav" , "laugh.wav" , "maniclaugh.wav" ]

def random_sound():

    sound=random.choice(sound_effects)

#    f=sf.SoundFile('/home/pi/Scripts/pumpkin//'+sound)
 #   seconds=(len(f)/f.samplerate)

    return "/home/pi/Scripts/pumpkin/"+sound

def rgb():

    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    return r,g,b

def react():
    
    global flashing
    flashing=True
    sequence=0
    subprocess.Popen(["aplay "+random_sound()], shell=True)    

    while sequence<600:

        sense.clear(rgb())

        sequence+=1
    sequence=0
    sense.clear(255,0,0)
    time.sleep(5)
    flashing=False
    sense.clear()

while True:

    print ("flashing  "+str(flashing)+"   sensor  "+str(sensor.motion_detected))

    if sensor.motion_detected and not flashing:
        react()
    else:    
        time.sleep(1)
