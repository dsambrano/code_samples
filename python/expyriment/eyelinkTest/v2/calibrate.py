import constants
from pygaze import libscreen, eyetracker


def cal():
    disp = libscreen.Display(disptype=constants.DISPTYPE, dispsize=constants.DISPSIZE,
                             fgc=constants.FGC, bgc=constants.BGC, screennr=constants.SCREENNR)
    tracker = eyetracker.EyeTracker(disp, trackertype=constants.TRACKERTYPE, resolution=constants.DISPSIZE,
                                    saccvelthres=constants.SACCVELTHRESH, saccaccthresh=constants.SACCACCTHRESH)

    tracker.calibrate()  # <--Calibration is executed here
    disp.close()
    return(tracker)


log_file = constants.LOGFILENAME
