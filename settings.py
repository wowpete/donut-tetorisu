from pygame.locals import *
import random  # temporary
from perfect_clear_info import *

# change colours in display_info.py (scroll until it says # color schemes)

# can get key codes from https://docs.w3cub.com/pygame/ref/key.html or similar website
key_soft_drop = K_DOWN
key_move_left = K_LEFT
key_move_right = K_RIGHT
key_hard_drop = K_SPACE
key_90_clockwise = K_d
key_90_anticlockwise = K_a
key_180 = K_s
key_hold = K_BACKSLASH
key_hold2 = K_LSHIFT
key_printboard = K_b
key_changeCustomBag = K_n  # to input your own queue
key_changePreset = K_m  # to input a board based on presets.py
key_resetboard = K_F4  # window loses focus when you do this (but only once?)
key_retryqueue = K_4  # does the same as resetboard but with the same queue (useful for retrying pc solutions)

# donut controls changed in donut_transformations.py


setFPS = 60

tekoFontVisible = True  # change this to False if there is lots of text overlapping

softDropInterval = -1  # default = 50 - set to -1 for instant, hard-drop-like soft drop
defaultGravityInterval = 10000  # default = 670 - milliseconds between gravity movement,
# this is scaled up as you clear lines- this is limited at 1 movement per frame (i.e 17 tiles per second)
# put this really high to turn off gravity

# DAS defines how long (in milliseconds) the key must be held before repeatedly moving/"DASing"
# ARR defines how fast it moves, i.e how many milliseconds between every automatic movement.
# newPieceDASDelay: when a piece is locked, DAS movement is paused for this amount of time
# newPieceHardDropDelay: when a piece locks by itself (gravity), hard drop is disabled for this time to prevent
# accidental hard drops
# lockDelay: when a piece is on the ground, it is automatically placed/locked after this amount of milliseconds
# lockDelayCancelLimit: when a piece is moved/rotated while on the ground, the lock delay is reset. this is the maximum
# amount of times this can be done
ARR = -1  # 50
DAS = 110  # 160
newPieceDASDelay = 10  # 33
newPieceHardDropDelay = 50
lockDelay = 150000000  # 500
lockDelayCancelLimit = 12  # 12


# things for practicing pcs and things
# everything here controls what happens with you press F4 (the restart button)
# preset and bag/queue can be changed ingame (by default using N or M)
piecesToStartWith = 7  # default 7 - changes how many pieces in the starting bag
presetMap = "blank"
customBag = ""  # e.g "iosz"
shuffleCustomBag = False
allowInfiniteHolds = True
putPieceInHold = True
randomlyMirrorBag = False

useVeryCustomBag = False  # if you want to customise queue more, setting this to true will give the bag generated by the
# fuction below


def create_very_custom_queue():
    # [["j", "s", "z", "l"], ["i", "s", "z", "o"], ["j", "o", "i", "l"]][random.randint(0, 2)]
    # while True:
    #    seven_bag = ['i', 'o', 't', 's', 'z', 'j', 'l']
    #    random.shuffle(seven_bag)
    #    extra_pieces = random.randint(1, 6)
    #    if extra_pieces_to_pc_num(extra_pieces - 1, 5) % 7 <= 3:
    #        continue
    #    print(f"extra_pieces: {extra_pieces - 1}  nth pc: {extra_pieces_to_pc_num(extra_pieces - 1, 5)}")
    #    for i in range(7-extra_pieces):
    #        seven_bag.pop()
    #    return seven_bag
    
    bagOne = ["s", "j", "l"]
    bagTwo = ["t", "o", "i", "z"]
    random.shuffle(bagOne)
    random.shuffle(bagTwo)
    q = ["t"]
    q.extend(bagOne)
    q.extend(bagTwo)
    return q


customBag = list(customBag.lower())  # (ignore this) this is to convert "iosz" to ["i", "o", "s", "z"]
