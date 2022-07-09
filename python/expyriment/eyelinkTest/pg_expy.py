from expyriment import design, control, stimuli, misc,io
import constants
from pygaze import libscreen, eyetracker, libgazecon
import pygame

disp        =   libscreen.Display(disptype=constants.DISPTYPE, dispsize=constants.DISPSIZE, fgc=constants.FGC, bgc=constants.BGC, screennr=constants.SCREENNR)
tracker     =   eyetracker.EyeTracker(disp, trackertype=constants.TRACKERTYPE, resolution=constants.DISPSIZE, saccvelthres=constants.SACCVELTHRESH, saccaccthresh=constants.SACCACCTHRESH)

tracker.calibrate() # <--Calibration is executed here

disp.close()

expName="Encoding"
exp         =   design.Experiment(name=expName, filename_suffix=expName)
control.initialize(exp)

control.start()
tracker.log('Start Experiment')
tracker.start_recording()
instro = stimuli.BlankScreen()
stimuli.TextLine(u'Calibration necessary.', position = (0, 100), text_size = 40, text_bold = False).plot(instro)
stimuli.TextLine(u'Continue with "space bar"', position = (0, 50 - exp.screen.size[1]/2), text_size = 25, text_bold = False).plot(instro)
instro.present(clear = False)
exp.keyboard.wait(misc.constants.K_SPACE) # Wait for space
tracker.stop_recording()

# exp.keyboard.wait()

control.end()
tracker.close()
