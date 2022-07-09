# MAIN
DUMMYMODE = False
part_id = str(input("Participant ID: "))
part_id = ''.join('000' + str(part_id))[-3:]
day = str(input("day: "))
LOGFILENAME = part_id + '_day' + day
LOGFILE = LOGFILENAME[:]

# DISPLAY
DISPTYPE = 'pygame'
DISPSIZE = (1280, 1024)
SCREENSIZE = (37.7, 30)

# EYETRACKER
TRACKERTYPE = 'eyelink'
SACCVELTHRESH = 35
SACCACCTHRESH = 9500

BGC = (125, 125, 125, 255)

FGC = (0, 0, 0, 255)  # foreground colour

SCREENNR = 0
