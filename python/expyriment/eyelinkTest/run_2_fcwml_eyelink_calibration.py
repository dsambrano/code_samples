# -*- coding: utf-8 -*-
"""
Created on Fri May 11 08:54:45 2018

@author: lindadevoogd
"""


# Import libraries
import expyriment

#eyelink stuff
from pylink import *
from pylink import getEYELINK
import gc

# SET BEFORE THE EXPERIMENT [only vars in capital letters can be changed]
#------------------------------------------------------------------------------
SUBJ_CODE = "FCWML132"
TESTING = 0 # 1 or 0
REFRESH_RATE = 60  # In Hz
WINDOW_SIZE = 1280,1040
eyelinkconnected=1

# TESTING
#------------------------------------------------------------------------------

# When testing
if TESTING == 1:
    expyriment.control.set_develop_mode() #create small screen
    speedup = 1 # if set at 1 it is normal duration
    portconnected = 0 #no port connected
else:
    speedup = 1 #normal speed
    portconnected = 1 #port connected
    
    
# TASK SETTINGS
#------------------------------------------------------------------------------

# Create experimental task
task = expyriment.design.Experiment(
        name= SUBJ_CODE + " - Calibration",
        background_colour = (125,125,125))  #background color
expyriment.control.initialize(task)
task.add_data_variable_names(["Logevent","Onset","Key","RT","Dur_Dig","Dur_Fix"])

# Screen
expyriment.control.defaults.window_size = (WINDOW_SIZE)
frame = 1000 / REFRESH_RATE

# Port setting
port_shock = [100,200] #code and duration
port_biopack = 1 #code
if portconnected == 1:
    port = expyriment.io.ParallelPort(0xC020)

# Eyelink
if eyelinkconnected == 1:
    tracker = EyeLink("100.1.1.2")
    getEYELINK().openDataFile(SUBJ_CODE+'.EDF')
        
# Keys, Clock
keys = expyriment.io.Keyboard()
keys.set_quit_key(expyriment.misc.constants.K_ESCAPE) #with esc you can quit
responsekey=expyriment.misc.constants.K_SPACE
experimenterkey=expyriment.misc.constants.K_5 #so pp cannot accidently press space bar and continue


# Instructions
instructions = " \n \
Please follow the dot.\n \
\n \
Press space to start. \n \
\n \
"

# DESIGN [experiment/task, blocks, trials, stimuli]
#------------------------------------------------------------------------------
# Create design (blocks and trials)
# Create stimuli (and put them into trials)
# Create input/output devices (like button boxes etc.)

# One block so no loop
block = expyriment.design.Block("Block")

# Create Design, Loop over trials
posx=[(WINDOW_SIZE[0]/2)*-.8, 0, (WINDOW_SIZE[0]/2)*.8]
posy=[(WINDOW_SIZE[1]/2)*.8, 0, (WINDOW_SIZE[1]/2)*-.8]

for c_y in range(3):
    for c_x in range(3):

        # Trial [define properties]
        trial =  expyriment.design.Trial()
        trial.set_factor("X",c_x)
        trial.set_factor("Y",c_y)
        
        # Load Circle
        stim = expyriment.stimuli.Circle(radius=25,colour=(60,60,255),
                                         position=(posx[c_x],posy[c_y]))
        stim.preload()
        
        # Add stim to trial and trial to block
        trial.add_stimulus(stim)
        block.add_trial(trial)

# Add block to task
task.add_block(block)

# Other stimuli
startdot = expyriment.stimuli.Circle(radius=25,colour=(60,60,255),
                                         position=(0,0))
blank = expyriment.stimuli.BlankScreen()                                        # blackscreen
blank.preload()

def wait(dur):
    task.keyboard.clear()
    task.clock.reset_stopwatch()
    while task.clock.stopwatch_time < int(frame * int(round((dur) / frame, 5))) - 2:
        task.keyboard.check(keys=responsekey)

# RUN
#------------------------------------------------------------------------------

# Eyelink
if eyelinkconnected == 1:
    getEYELINK().startRecording(1, 1, 1, 1)
    getEYELINK().sendMessage("START_TIME")
    gc.disable()
    beginRealTimeMode(100)

# Start
expyriment.control.start(subject_id=int(SUBJ_CODE[-3:]))

# Instruction
expyriment.stimuli.TextScreen("", instructions, 
                              text_colour=[0,0,0]).present()
task.keyboard.wait(responsekey)

# Start fixation
startdot.present()
wait(2000)

# Loop over trials/blocks
for trial in task.blocks[0].trials:
    
    # Blank screen
    blank.present()
    wait(1000)    
    
    # Dot 
    trial.stimuli[0].present()
    getEYELINK().sendMessage("DOT_ONSET")
    task.keyboard.wait(responsekey)

    
# End
expyriment.control.end(goodbye_text="This is the end of the calibration!",
             goodbye_delay=2000)

# Eyelink
if eyelinkconnected == 1:
    getEYELINK().sendMessage("END_TIME")
    endRealTimeMode()
    pumpDelay(100)
    getEYELINK().stopRecording()
    gc.enable()
    getEYELINK().setOfflineMode()
    getEYELINK().closeDataFile()
    getEYELINK().receiveDataFile(SUBJ_CODE+'.EDF', 'data/'+SUBJ_CODE+'_calibration.EDF')
    getEYELINK().close()
