#!/usr/bin/env python
import os
from expyriment import design, control, stimuli, io, misc

#eyelink stuff
from pylink import *
from pylink import getEYELINK
import gc

eyetrack = True

# Create Experiment Name and handle and initialize it
exp = design.Experiment(name='First Experiment',
                        background_colour=(87, 87, 87))
control.initialize(exp)

if eyetrack:
    tracker = EyeLink("100.1.1.1")
    getEYELINK().openDataFile(exp.subject+'.edf')
    pylink.doTrackerSetup()
    getEYELINK().sendMessage("START_TIME")
    getEYELINK().startRecording(1, 1, 1, 1)
    gc.disable()
    beginRealTimeMode(100)
    wait(2000)    

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

control.start()
if eyetrack:
    tracker = EyeLink("100.1.1.1")
    getEYELINK().openDataFile(+'.edf')

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
    getEYELINK().receiveDataFile(exp.subject+'.EDF', os.path.join('data',exp.subject+'_day1_run1.EDF'))
    getEYELINK().close()