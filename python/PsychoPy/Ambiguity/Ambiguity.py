#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on Thu Aug 24 15:09:35 2017
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import random
import time

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'Ambiguity'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Randomization
random.seed(round(time.time()))

LeftOption = random.choice(["Pay", "Gamble"])
if(LeftOption == "Gamble"):
    RightOption = "Pay"
else:
    RightOption = "Gamble"

#options = ["Pay", "Keep", "Gamble"]
options = ["Pay", "Gamble"] # If you don't want to deal with the gamble one

random.shuffle(options)
#(LeftOption, MiddleOption, RightOption) = options
# If I want to make "Keep" always be in the middle
(LeftOption, MiddleOption, RightOption) = [options[0], "Keep", options[1]]

RepY = .7
RedLeft = ""
BlueLeft = ""
newCenter = -.2

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1280, 800), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instr"
instrClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=u'You are about to take my experiment. \nThank you very much for that\n\nHere are the instructions\n\nThere will be two parts to this experimnet\n\nHave fun!',
    font=u'Arial',
    pos=(0, 0), height=0.075, wrapWidth=2, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "instr2"
instr2Clock = core.Clock()
text2 = visual.TextStim(win=win, name='text',
    text=u"In the first part you will have to make a fiscal decision\n\nYou will start with 5 dollars and have an opportunity to either 'Pay', 'Gamble', or 'Keep'.\nIf you decide to 'Keep' then you will keep the 5 dollars and the trial will end.\nIf you decide to 'Gamble' you play the odds show by the red and blue rectangles.\n\nHave fun!",
    font=u'Arial', # \nHowever, you pay $1 to 
    pos=(0, 0), height=0.1, wrapWidth=2, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "prac"
pracClock = core.Clock()

# Initialize components for Routine "trial"
trialClock = core.Clock()

def RedRect(Height=.5):
    yPos=((1-Height)/2)+ newCenter
    Red = visual.Rect(win=win, name='Red',
        width=(0.2, Height)[0], height=(0.2, Height)[1],
        ori=0, pos=(0, yPos),
        lineWidth=1, lineColor=[1,-1,-1], lineColorSpace='rgb',
        fillColor=[1,-1,-1], fillColorSpace='rgb',
        opacity=1, depth=0.0, interpolate=False)
    return Red

def BlueRect(Height=.5):
    yPos = ((1 - Height)/-2) + newCenter
    Blue = visual.Rect(win=win, name='Blue',
        width=(0.2, Height)[0], height=(0.2, Height)[1],
        ori=0, pos=(0, yPos),
        lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
        fillColor=[-1,-1,1], fillColorSpace='rgb',
        opacity=1, depth=-1.0, interpolate=True)
    return Blue


def AmbigGrey(height, yPos=0):
    yPos = yPos + newCenter
    Rect = visual.Rect(win=win, name='Grey',
    	width=(0.225, height)[0], height=(0.225, height)[1],
    	ori=0, pos=(0, yPos),
    	lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    	fillColor=[0,0,0], fillColorSpace='rgb',
    	opacity=1, depth=-2.0, interpolate=True)
    return Rect

RedNumb = visual.TextStim(win=win, name='RedNumb',
    text=u'',
    font=u'Arial',
    pos=(0, .45 + newCenter), height=0.05, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0);


BlueNumb = visual.TextStim(win=win, name='BlueNumb',
    text=u'' ,
    font=u'Arial',
    pos=(0, -.47 + newCenter), height=0.05, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0);

GreyNumb = visual.TextStim(win=win, name='GreyNumb',
    text=u'' ,
    font=u'Arial',
    pos=(0, 0 + newCenter), height=0.05, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0);
RMoney = visual.TextStim(win=win, name='RMoney',
    text=u'',
    font=u'Arial',
    pos=(0, .55 + newCenter), height=0.05, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0);
BMoney = visual.TextStim(win=win, name='BMoney',
    text=u'' ,
    font=u'Arial',
    pos=(0, -.55 + newCenter), height=0.05, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# textbox = visual.TextBox(window=win, 
#                          text='Something',
#                          font_size=21,
#                          font_color=[-1,-1,1], 
#                          size=(1.9, .3),
#                          pos=(0.0, 0.25), 
#                          grid_horz_justification='center',
#                          units='norm')

GreyLine = visual.Rect(
    win=win, name='GreyLine',
    width=(0.4, 0)[0], height=(0.225, 0)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True);
fixation = visual.TextStim(win=win, name='fixation',
    text=u'+',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0);
LeftRep = visual.TextStim(win=win, name='LeftRep',
    text=u'Q\n'+LeftOption,
    font=u'Arial',
    pos=(-.6, RepY), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0);
MiddleRep = visual.TextStim(win=win, name='MiddleRep',
    text=u'Space\n'+MiddleOption,
    font=u'Arial',
    pos=(0, RepY), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0);
RightRep = visual.TextStim(win=win, name='RightRep',
    text=u'P\n'+RightOption,
    font=u'Arial',
    alignHoriz='right',
    pos=(.6, RepY), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0);
# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanksText = visual.TextStim(win=win, name='thanksText',
    text='This is the end of the experiment.\n\nThanks!',
    font='arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr"-------
t = 0
instrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
ready = event.BuilderKeyResponse()
# keep track of which components have finished
instrComponents = [text, ready]
for thisComponent in instrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr"-------
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *ready* updates
    if t >= 0.0 and ready.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready.tStart = t
        ready.frameNStart = frameN  # exact frame index
        ready.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if ready.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr2"-------
t = 0
instr2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
ready2 = event.BuilderKeyResponse()
# keep track of which components have finished
instr2Components = [text2, ready2]
for thisComponent in instrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr2"-------
while continueRoutine:
    # get current time
    t = instr2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text2.tStart = t
        text2.frameNStart = frameN  # exact frame index
        text2.setAutoDraw(True)
    
    # *ready* updates
    if t >= 0.0 and ready2.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready2.tStart = t
        ready2.frameNStart = frameN  # exact frame index
        ready2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if ready2.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr2"-------
for thisComponent in instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialTypes.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # GreyNumb = GreyNumb(Uncertainty, Center)
    RedMoney, BlueMoney = (High, Low)
    Rednoise, Bluenoise = normal(scale = 1.5, size=2)
    RedMoney += Rednoise; RedMoney = round(RedMoney, 2)
    RMoney.setText('$'+str(RedMoney))
    BlueMoney += Bluenoise; BlueMoney = round(BlueMoney, 2)
    BMoney.setText('$'+str(BlueMoney))
    GreyNumb.setText(str(int(Uncertainty*100))+"%")
    GreyNumb.setPos((0, Center + newCenter))
    RedNumb.setText(str(int(RedHeight*100))+"%")
    RedNumb.setPos((0, Center + RedHeight/2 + newCenter)) 
    BlueNumb.setText(str(int(BlueHeight*100))+"%")
    BlueNumb.setPos((0, Center - BlueHeight/2 + newCenter))
    # RedNumb = RedNumb(RedHeight, (.5-RedHeight)/2)
    # BlueNumb = BlueNumb(BlueHeight, -(((.5-BlueHeight)/-2)-(Uncertainty/-2)))
    Red = RedRect(RedHeight)
    Blue = BlueRect(BlueHeight)
    Grey = AmbigGrey(Uncertainty, .5-RedHeight)
    response = event.BuilderKeyResponse()

    Vars = ['RedMoney', 'Rednoise', 'BlueMoney', 'Bluenoise', 'LeftRep', 
            'MiddleRep', 'RightRep'] 

    for thisVar in range(len(Vars)):
        trials.addData(Vars[thisVar], globals()[Vars[thisVar]])
        
    del Vars


    # keep track of which components have finished
    trialComponents = [Red, Blue, Grey, response, fixation, LeftRep, RightRep, MiddleRep, RedNumb, BlueNumb, GreyNumb, RMoney, BMoney]#, GreyNumb]#, GreyLine]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame 

        # *Respose Option* updates
        if t >= 1 and RightRep.status == NOT_STARTED:
            # keep track of start time/frame for later
            RightRep.tStart = t
            RightRep.frameNStart = frameN  # exact frame index
            RightRep.setAutoDraw(True)

        # *Respose Option* updates
        if t >= 1 and MiddleRep.status == NOT_STARTED:
            # keep track of start time/frame for later
            MiddleRep.tStart = t
            MiddleRep.frameNStart = frameN  # exact frame index
            MiddleRep.setAutoDraw(True)    
        
        if t >= 1 and LeftRep.status == NOT_STARTED:
            # keep track of start time/frame for later
            LeftRep.tStart = t
            LeftRep.frameNStart = frameN  # exact frame index
            LeftRep.setAutoDraw(True)
        
        # *Red* updates
        if t >= 1 and Red.status == NOT_STARTED:
            # keep track of start time/frame for later
            Red.tStart = t
            Red.frameNStart = frameN  # exact frame index
            Red.setAutoDraw(True)
        
        # *Blue* updates
        if t >= 1 and Blue.status == NOT_STARTED:
            # keep track of start time/frame for later
            Blue.tStart = t
            Blue.frameNStart = frameN  # exact frame index
            Blue.setAutoDraw(True)
        
        # *Grey* updates
        if t >= 1 and Grey.status == NOT_STARTED:
            # keep track of start time/frame for later
            Grey.tStart = t
            Grey.frameNStart = frameN  # exact frame index
            Grey.setAutoDraw(True)

        # *Money Option* updates
        if t >= 1 and RMoney.status == NOT_STARTED:
            # keep track of start time/frame for later
            RMoney.tStart = t
            RMoney.frameNStart = frameN  # exact frame index
            RMoney.setAutoDraw(True)
        
        # *Respose Option* updates
        if t >= 1 and BMoney.status == NOT_STARTED:
            # keep track of start time/frame for later
            BMoney.tStart = t
            BMoney.frameNStart = frameN  # exact frame index
            BMoney.setAutoDraw(True)

        # *Respose Option* updates
        if t >= 1 and RedNumb.status == NOT_STARTED and Uncertainty < .1:
            # keep track of start time/frame for later
            RedNumb.tStart = t
            RedNumb.frameNStart = frameN  # exact frame index
            RedNumb.setAutoDraw(True)
        
        # *Respose Option* updates
        if t >= 1 and BlueNumb.status == NOT_STARTED and Uncertainty < .1:
            # keep track of start time/frame for later
            BlueNumb.tStart = t
            BlueNumb.frameNStart = frameN  # exact frame index
            BlueNumb.setAutoDraw(True)

        # *Respose Option* updates
        if t >= 1 and GreyNumb.status == NOT_STARTED and Uncertainty >= .1:
            # keep track of start time/frame for later
            GreyNumb.tStart = t
            GreyNumb.frameNStart = frameN  # exact frame index
            GreyNumb.setAutoDraw(True)
        
        # # *GreyLine* updates
        # if t >= 1 and GreyLine.status == NOT_STARTED:
        #     # keep track of start time/frame for later
        #     GreyLine.tStart = t
        #     GreyLine.frameNStart = frameN  # exact frame index
        #     GreyLine.setAutoDraw(True)
        
        # *response* updates
        if t >= 1.1 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['q', 'p', 'left', 'right', 'space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # *fixation* updates
        if t >= 0.25 and fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation.tStart = t
            fixation.frameNStart = frameN  # exact frame index
            fixation.setAutoDraw(True)
        frameRemains = 0.25 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation.status == STARTED and t >= frameRemains:
            fixation.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            thisExp.saveAsWideText(filename+'.csv')
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys=None
    trials.addData('response.keys',response.keys)
    if response.keys != None:  # we had a response
        trials.addData('response.rt', response.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed N repeats of 'trials'

# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thanksText]
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksText* updates
    if t >= 0.0 and thanksText.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanksText.tStart = t
        thanksText.frameNStart = frameN  # exact frame index
        thanksText.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if thanksText.status == STARTED and t >= frameRemains:
        thanksText.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
    	thisExp.saveAsWideText(filename+'.csv')
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
