#!/usr/bin/env python
import os
from expyriment import design, control, stimuli, io, misc

#eyelink stuff
import pylink
from pylink import *
from pylink import getEYELINK
import gc

eyetrack = True

# Create Experiment Name and handle and initialize it
exp = design.Experiment(name='First Experiment',
                        background_colour=(87, 87, 87))
control.initialize(exp)

sp = (exp.screen.size[0], exp.screen.size[1])

# left and right arrow keys for responses
response_keys = [misc.constants.K_LEFT, misc.constants.K_RIGHT]
keys = io.Keyboard()
keys.set_quit_key(misc.constants.K_ESCAPE)  # with esc you can quit

block_one = design.Block(name="A name for the first block")
trial_one = design.Trial()
stim = stimuli.TextLine(text="I am a stimulus in Block 1, Trial 1")
stim.preload()
trial_one.add_stimulus(stim)
trial_two = design.Trial()
stim = stimuli.TextLine(text="I am a stimulus in Block 1, Trial 2")
trial_two.add_stimulus(stim)
block_one.add_trial(trial_one)
block_one.add_trial(trial_two)
exp.add_block(block_one)

block_two = design.Block(name="A name for the second block")
trial_one = design.Trial()
stim = stimuli.TextLine(text="I am a stimulus in Block 2, Trial 1")
stim.preload()
trial_one.add_stimulus(stim)
trial_two = design.Trial()
stim = stimuli.TextLine(text="I am a stimulus in Block 2, Trial 2")
trial_two.add_stimulus(stim)
block_two.add_trial(trial_one)
block_two.add_trial(trial_two)
exp.add_block(block_two)

def eyeTrkInit (sp):
    el = pylink.EyeLink("100.1.1.1")
    el.sendCommand("screen_pixel_coords = 0 0 %d %d" %sp)
    el.sendMessage("DISPLAY_COORDS  0 0 %d %d" %sp)
    el.sendCommand("select_parser_configuration 0")
    el.sendCommand("scene_camera_gazemap = NO")
    el.sendCommand("pupil_size_diameter = %s"%("YES"))
    return(el)

def eyeTrkCalib (el,sp,cd):
    pylink.openGraphics(sp,cd)
    pylink.setCalibrationColors((255,255,255),(0,0,0))
    pylink.setTargetSize(int(sp[0]/70), int(sp[1]/300)) 
    pylink.setCalibrationSounds("","","")
    pylink.setDriftCorrectSounds("","off","off")
    el.doTrackerSetup()
    pylink.closeGraphics()
    #el.setOfflineMode()


control.start()

if eyetrack: 
    el = pylink.EyeLink("100.1.1.1")
    el.sendCommand("screen_pixel_coords = 0 0 %d %d" %sp)
    el.sendMessage("DISPLAY_COORDS  0 0 %d %d" %sp)
    el.sendCommand("select_parser_configuration 0")
    el.sendCommand("scene_camera_gazemap = NO")
    el.sendCommand("pupil_size_diameter = %s"%("YES"))
    pylink.openGraphics(sp,cd)
    pylink.setCalibrationColors((255,255,255),(0,0,0))
    pylink.setTargetSize(int(sp[0]/70), int(sp[1]/300)) 
    pylink.setCalibrationSounds("","","")
    pylink.setDriftCorrectSounds("","off","off")
    el.doTrackerSetup()
    pylink.closeGraphics()

if eyetrack and False:
    tracker = EyeLink("100.1.1.1")
    pylink.setCalibrationColors(exp.foreground_colour, exp.background_colour)
    pylink.setTargetSize(sp[0] /70, sp[0] /300);
    pylink.setCalibrationSounds('','','')
    pylink.setDriftCorrectSounds('','off','off')
    getEYELINK().openDataFile('001' + '.edf')
    tracker.doTrackerSetup()
    # getEYELINK().doTrackerSetup()
    getEYELINK().sendMessage("START_TIME")
    getEYELINK().startRecording(1, 1, 1, 1)
    gc.disable()
    beginRealTimeMode(100)
    exp.clock.wait(2000)    

for block in exp.blocks:
    for trial in block.trials:
        trial.stimuli[0].present()
        key, rt = exp.keyboard.wait([misc.constants.K_LEFT,
                                     misc.constants.K_RIGHT])
        exp.data.add([block.name, trial.id, key, rt])

control.end()

# Eyelink [END RECORDING]
if eyetrack:
    getEYELINK().sendMessage("END_TIME")
    endRealTimeMode()
    pumpDelay(100)
    getEYELINK().stopRecording()
    gc.enable()
    getEYELINK().setOfflineMode()
    getEYELINK().closeDataFile()
    getEYELINK().receiveDataFile('001' + '.edf', os.path.join('data','001' +'_day1_run1.edf'))
    getEYELINK().close()
