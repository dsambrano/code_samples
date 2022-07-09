#!/usr/bin/env python
import os
from expyriment import design, control, stimuli, io, misc
import bonus_payment
import calibrate

# #eyelink stuff
# from pylink import *
# from pylink import getEYELINK
# import gc


''' ######## TESTING VARIABLES ######### '''
TESTING = True  # Are you testing True or False
EYETRACK = False


''' ######## EYETRACKER SETUP/CALIBRATION ######### '''
if EYETRACK:
    tracker = calibrate.cal()


''' ######## NOTES AND CHANGES TO MAKE ######### '''
# NEED PRACTICE AND NEED TO CHANGE THE BLOCK NAME AND TRIAL ID

# Currently the probs of lottery is incorrect. It is displaying the probs
# of red as opposed to the probability of winning flat. That needs to be
# changed. #### DONE ####

# I want to add a section at the end of the experiment that has you type
# in the randomly selected trial number and and block number. #### DONE ####

# NEED TO ADD EYETRACKING and shock: See Linda's script for ideas and sample
# code.

# Finally make a copy practice and import that script in. Then make
# another copy for threat of shock. execfile('foo.py')

# Additionally, the ITI is not variable currently. Relatedly the pre- and
# post- block fixations are hard coded and should be altered. #### DONE ####

# I have some concerns with the randomization structure currently. After
# giving it some thought I think it might not be completely controlled
# such that each ($$) level gets each ambig and each risk level. I need
# to do some testing to confirm that it is correct. If not, that likely
# the MATLAB version is also incorrect. #### DONE ####  This can be
# checked with the following code:
# t = sorted(zip(win_color_vec,mon_vals_vec, risky_probs_vec, ambig_probs_vec))


''' ######## CHANGE DEFAULTS ######### '''


# Don't add time stamps to the data files
io.defaults.outputfile_time_stamp = False
# Developer mode
control.set_develop_mode(False)

# Create Experiment Name and handle and initialize it
exp = design.Experiment(name='First Experiment',
                        background_colour=(87, 87, 87))
control.initialize(exp)


# left and right arrow keys for responses
response_keys = [misc.constants.K_LEFT, misc.constants.K_RIGHT]
keys = io.Keyboard()
keys.set_quit_key(misc.constants.K_ESCAPE)  # with esc you can quit


''' ######## EXPERIMENTAL SETTINGS ######### '''


screen_h = exp.screen.size[1]
screen_w = exp.screen.size[0]

# Set up lotto rectangle and text position/size
rect_height = screen_h * .2
rect_width = screen_w * .1
lotto_height = 2 * rect_height
money_y_pos = rect_height + 30
lotto_types = ['risky', 'ambig']
lotto_side = ['right', 'left'][int(design.randomize.coin_flip())]

# Colors (these were tested to be luminance controlled)
lotto_colors = ['blue', 'red']
red_color = (155, 34, 102)
blue_color = (45, 84, 155)
ambig_color = (106, 78, 32)
background_color = (87, 87, 87)

# Experiment timing in miliseconds
lotto_dur = 4000
resp_dur = 1500
confirm_dur = 500

# Font and fixation size
font_size = 40
fix_size = (60, 60)
fix_width = 5
pre_post_fix_dur = 2000
IBI = 2000  # 2 seconds in between blocks
rest_dur = 15000  # 15 seconds of rest every ___ blocks
rest_freq = 2  # Rest every 2 blocks in this paradigm
fix_dur_type = [1750, 2000, 2250]


''' ######### EXPERIMENTAL PARAMETERS ######### '''


num_blocks = 4
num_block_trials = 30
num_trials = num_blocks * num_block_trials
monetary_vals = [5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 23, 26,
                 30, 34, 39, 44, 50, 57, 66]
risky_probs = [.75, .5, .25]
ambig_probs = [.74, .5, .24]

# Should sum to the same amount if you use these as indecies for monetary_vals
# sum([monetary_vals[i] for i in color_index2]) # Check that they sum to same amount
# color_index1 = [1, 2, 5, 6, 7, 11, 14, 16, 18, 20]  # Change indexies to python from MATLAB
# color_index2 = [3, 4, 8, 9, 10, 12, 13, 15, 17, 19]
color_index1 = [0, 1, 4, 5, 6, 10, 13, 15, 17, 19]
color_index2 = [2, 3, 7, 8, 9, 11, 12, 14, 16, 18]

# Create the vectors for the risk levels, ambig levels, and monetary values for each trial.
risky_probs_vec = risky_probs * len(monetary_vals) + [.5] * len(monetary_vals) * len(ambig_probs)
ambig_probs_vec = [0] * len(monetary_vals) * len(risky_probs) + ambig_probs * len(monetary_vals)
mon_vals_vec = monetary_vals * len(risky_probs) * len(lotto_types)

# Set up the winning color such that the winning amounts for each
# color sum to the same total (i.e., controlled for winning color/amount)
win_color_vec = []
rand_color_ind = int(design.randomize.coin_flip())
for i in range(len(monetary_vals)):
    if i in color_index1:
        color = lotto_colors[rand_color_ind]
    elif i in color_index2:
        color = lotto_colors[abs(rand_color_ind - 1)]
    win_color_vec += [color]

win_color_vec *= len(risky_probs) * len(lotto_types)

# Set the ITIs for each trial
fix_dur_vec = sorted(fix_dur_type * len(monetary_vals) * len(lotto_types))

# Speed everything up if you are just testing.
if TESTING:
    lotto_dur = 50
    resp_dur = 50
    confirm_dur = 50
    pre_post_fix_dur = 50
    fix_dur_vec = [50] * num_trials
    rest_dur = 2000
    IBI = 500

# Create a random shuffle of 1:len(num_trials) and apply that order to each of
# the unshuffled exp_params
rand_shuffle = [i for i in range(num_trials)]
design.randomize.shuffle_list(rand_shuffle)
ordered_shuffle = sorted(range(len(rand_shuffle)), key=rand_shuffle.__getitem__)

# Set up the experimental params as a dictionary to be used later
exp_params = {'win_color': [x for y, x in sorted(zip(ordered_shuffle, win_color_vec))],
              'ambig': [x for y, x in sorted(zip(ordered_shuffle, ambig_probs_vec))],
              'prob': [x for y, x in sorted(zip(ordered_shuffle, risky_probs_vec))],
              'val': [x for y, x in sorted(zip(ordered_shuffle, mon_vals_vec))],
              'ITI': [x for y, x in sorted(zip(ordered_shuffle, fix_dur_vec))],
              'randOrder': rand_shuffle}


# #### ERROR CHECK #### #
if not len(risky_probs_vec) == num_trials:
    print('Number trials and length of paramters not equal.')
    quit()


''' ######## FUNCTIONS ######### '''


def lottery(win_color='blue', win_prob=.5, ambig=.5):
    # val=0, win_color=0
    if win_color == 'blue':
        probs_blue = win_prob
        probs_red = (1 - probs_blue)
    elif win_color == 'red':
        probs_red = win_prob
        probs_blue = (1 - probs_red)

    # Colored Rect Info
    blue_height = lotto_height * probs_blue
    red_height = lotto_height - blue_height
    blue_y_pos = (blue_height / 2) - (rect_height - red_height)
    red_y_pos = -((red_height / 2) - (rect_height - blue_height))
    blue_chips = int((1 - probs_red - (ambig / 2)) * 100)
    red_chips = int((1 - probs_blue - (ambig / 2)) * 100)

    # Ambiguity Related Info
    ambig_width = screen_w * .11
    ambig_height = lotto_height * ambig + 5
    ambig_y_pos = red_y_pos + blue_y_pos
    text_adjust = .25 * ambig_height

    # Sets a canvas to place multiple stimuli
    canvas = stimuli.Canvas(size=(screen_h, screen_w))

    # Create the 3 rectangles that make up the lottery
    red_rect = stimuli.Rectangle((rect_width, red_height),
                                 colour=red_color, position=(0, red_y_pos))
    blue_rect = stimuli.Rectangle((rect_width, blue_height),
                                  colour=blue_color, position=(0, blue_y_pos))
    ambig_rect = stimuli.Rectangle((ambig_width, ambig_height),
                                   colour=ambig_color, position=(0, ambig_y_pos))

    # Create the text to inform the number of colored chips
    red_numb = stimuli.TextLine(text=str(red_chips), position=(0, red_y_pos - text_adjust))
    blue_numb = stimuli.TextLine(text=str(blue_chips), position=(0, blue_y_pos + text_adjust))

    # Plot everything to the canvas
    red_rect.plot(canvas)
    blue_rect.plot(canvas)
    ambig_rect.plot(canvas)
    red_numb.plot(canvas)
    blue_numb.plot(canvas)

    # Return the canvas
    return(canvas)


def money_text(val, win_color):
    if win_color == 'red':
        win_y_pos = money_y_pos
    elif win_color == 'blue':
        win_y_pos = - money_y_pos

    lose_y_pos = - win_y_pos

    win_money = stimuli.TextLine(text="$" + str(val), position=(0, win_y_pos), text_size=font_size)
    lose_money = stimuli.TextLine(text="$" + "0", position=(0, lose_y_pos), text_size=font_size)

    return(win_money, lose_money)


def choice_select(lotto_location):
    # Determine if the word lottery should be on the left or right
    if lotto_location == 'left':
        lot_loc = -(screen_w / 2) * .2
        ref_loc = -lot_loc
    elif lotto_location == 'right':
        lot_loc = (screen_w / 2) * .2
        ref_loc = -lot_loc
    else:
        print('No lotto locaiton selected')

    # Create a canvas for multiple stimuli
    canvas = stimuli.Canvas(size=(screen_h, screen_w))

    # Create the words and put them in the correct location
    lot_word = stimuli.TextLine(text="Lottery", position=(lot_loc, 0), text_size=font_size)
    ref_word = stimuli.TextLine(text="$5", position=(ref_loc, 0), text_size=font_size)

    # Put them in the canvas
    lot_word.plot(canvas)
    ref_word.plot(canvas)

    # Return the canvas
    return(canvas)


def participant_choice(lotto_side, key):
    if key == misc.constants.K_LEFT:
        if lotto_side == 'left':
            choice = 'Lottery'
        elif lotto_side == 'right':
            choice = 'Reference'
    elif key == misc.constants.K_RIGHT:
        if lotto_side == 'right':
            choice = 'Lottery'
        elif lotto_side == 'left':
            choice = 'Reference'
    else:
        choice = None

    return(choice)


def response_confirmation(lotto_location, key):
    # Create the word canvas and identify which arrow key was pressed
    canvas = choice_select(lotto_location)
    frame_dims = (200, 75)
    frame_width = 20
    frame_color = ambig_color
    if key == misc.constants.K_LEFT:
        y_pos = -(screen_w / 2) * .2
    elif key == misc.constants.K_RIGHT:
        y_pos = (screen_w / 2) * .2
    else:
        y_pos = 0
        frame_dims = (1, 1)
        frame_width = 1
        frame_color = background_color

    # Make the confrimation frame and add it to the canvas
    frame = stimuli.Rectangle(frame_dims, line_width=frame_width,
                              colour=frame_color, position=(y_pos, 0))
    frame.plot(canvas)

    # Return the canvas
    return(canvas)


def get_bag_numb(p, A, win_color):
    # Directly ported form MATLAB
    if win_color == 'blue':
        p = 1 - p

    if A > 0:
        if A == .24:
            bag_numb = 10
        elif A == .5:
            bag_numb = 11
        elif A == .74:
            bag_numb = 12
    elif A == 0:
        if p == .25:
            bag_numb = 3
        elif p == .5:
            bag_numb = 4
        elif p == .75:
            bag_numb = 5

    return(bag_numb)


'''####### DEFINING STIMULI AND EXPERIMENTAL STRUCTURE #######'''


# Define and preload standard stimuli
fixcross = stimuli.FixCross(size=fix_size, line_width=fix_width, colour=ambig_color)
fixcross.preload()

count = 0
for block_numb in range(num_blocks):
    block = design.Block(name=str(block_numb))
    for trial_numb in range(num_block_trials):
        trial = design.Trial()
        canvas = lottery(win_color=exp_params['win_color'][count],
                         win_prob=exp_params['prob'][count],
                         ambig=exp_params['ambig'][count])
        for key in exp_params.keys():
            # print('key: ', key, ', count: ', str(count))
            trial.set_factor(key, exp_params[key][count])
        trial.add_stimulus(canvas)
        canvas = choice_select(lotto_side)
        trial.add_stimulus(canvas)
        block.add_trial(trial)
        count += 1
    # block.shuffle_trials()
    exp.add_block(block)

print(exp.blocks[0].trials[0].factor_dict)

# Add Var names
exp.data_variable_names = ["ID", "Day", "Block", "Trial", "Key", "RT",
                           "Choice", "val", "prob", "ambig", "winColor",
                           "lottoSide", "ITI", "bag"]


'''####### Start the Experiment and Run #######'''


# Start the Exp
control.start()
str_id = ''.join('000' + str(exp.subject))[-3:]

# Ask for the randomly
day = io.TextInput(message="Experiment day? (1 or 2)",
                   ascii_filter=misc.constants.K_ALL_DIGITS)
day = int(day.get())
# io.OutputFile.rename(str_id + '_day_' + str(day))

# Eyelink
# if EYETRACK:
#     tracker = EyeLink("100.1.1.1")
#     getEYELINK().openDataFile(str_id + '_day_' + str(day) + '_ET.edf')
if EYETRACK:
    # tracker = EyeLink("100.1.1.1")
    # getEYELINK().openDataFile(SUBJ_CODE + '.EDF')  # Change this to by correcto
    # pylink.doTrackerSetup()
    tracker.log('start_time')
    tracker.start_recording()

count = 0
for i, block in enumerate(exp.blocks):
    if i % rest_freq == 0 and i:
        stimuli.TextLine(text='%s second Rest' % (rest_dur / 1000), text_size=font_size).present()
        exp.clock.wait(rest_dur)

    block_text = stimuli.TextLine(text="Block " + str(i + 1), text_size=font_size)
    block_text.preload()
    block_text.present()
    if not i:
        exp.keyboard.wait(keys=misc.constants.K_5)

    exp.clock.wait(IBI)
    if EYETRACK:
        tracker.log('start block ' + str(i))

    # Present fixation longer fixation at the beginning of each block
    fixcross.present()
    exp.clock.wait(pre_post_fix_dur)

    for trial in block.trials:
        # Get factors and prepare the text for the money amounts
        trial_dict = trial.factor_dict
        for key in trial_dict.keys():
            exec '%s = %r' % (key, trial_dict[key])

        win_money, lose_money = money_text(val, win_color)
        win_money.preload()
        lose_money.preload()

        # Present fixation for speficied length
        fixcross.present()
        if EYETRACK:
            tracker.log('trial ' + str(count) + ' fixation')
        exp.clock.wait(ITI)

        # Show the lottery (the first canvas) for appropriate time
        lotto = trial.stimuli[0]
        win_money.plot(lotto)
        lose_money.plot(lotto)
        lotto.present()
        if EYETRACK:
            tracker.log('trial ' + str(count) + ' lottery')
        exp.clock.wait(lotto_dur)

        # Finally present the choice screen (second canvas)
        trial.stimuli[1].present()
        if EYETRACK:
            tracker.log('trial ' + str(count) + ' choice')
        key, rt = exp.keyboard.wait(keys=response_keys, duration=resp_dur)
        if rt is not None:
            exp.clock.wait(resp_dur - rt)

        # Get the bag number
        bag_numb = get_bag_numb(prob, ambig, win_color)

        # Add the trial data to the data file
        choice = participant_choice(lotto_side, key)
        exp.data.add([str_id, day, block.name, trial.id, key, rt, choice, val,
                      prob, ambig, win_color, lotto_side, ITI, bag_numb])

        # Show confimation screen
        frame = response_confirmation(lotto_side, key)
        frame.present()
        if EYETRACK:
            tracker.log('trial ' + str(count) + ' confirmation')
        exp.clock.wait(confirm_dur)
        count += 1

    # Present fixation longer fixation at the end of each block also
    fixcross.present()
    exp.clock.wait(pre_post_fix_dur)

# Show End Screen, turn off eyetracker, and do bonus info
thanks = stimuli.TextScreen("", "This is the end of the experiment.\n" \
                                "Please inform the researcher.\n" \
                                "You will now randomly select a trial to implement your bonus.",
                            text_size=font_size)
thanks.present()
exp.data.rename('LotteryTask_' + str_id + '_day' + str(day) + '.xpd')

# Eyelink [END RECORDING]
if EYETRACK:
    # getEYELINK().sendMessage("END_TIME")
    # endRealTimeMode()
    # pumpDelay(100)
    # getEYELINK().stopRecording()
    # gc.enable()
    # getEYELINK().setOfflineMode()
    # getEYELINK().closeDataFile()
    # getEYELINK().receiveDataFile(os.path.join(str_id + '.edf', 'data/' + str_id + '_day' + str(day) + '_run1.edf'))
    # getEYELINK().close()
    tracker.log('end_time')
    tracker.close()


# misc.data_preprocessing.write_concatenated_data(os.path.join(os.getcwd(),'data'),str_id + '_day_' + str(day))

exp.keyboard.wait(keys=misc.constants.K_5)

# Ask for the random block and trial number for bonus information
bonus_block = io.TextInput(message="(RESEARCHER ONLY) Randomly selected BLOCK for bonus payment.",
                           ascii_filter=misc.constants.K_ALL_DIGITS)
bonus_block = int(bonus_block.get()) - 1  # minus 1 because python indicies

bonus_trial = io.TextInput(message="(RESEARCHER ONLY) Randomly selected TRIAL for bonus payment.",
                           ascii_filter=misc.constants.K_ALL_DIGITS)
bonus_trial = int(bonus_trial.get()) - 1  # minus 1 because python indicies

# Get the bonus info and display it on the screen.
exp_info = {'block_num': bonus_block, 'trial_num': bonus_trial, 'f_name': exp.data.filename,
            'num_blocks': num_blocks, 'num_block_trials': num_block_trials}
bonus_info = bonus_payment.bonus(**exp_info)

bonus_text = stimuli.TextLine(text=str(bonus_info), text_size=font_size)
bonus_text.present()
exp.keyboard.wait(keys=misc.constants.K_5)

# Print it to the console just in case you forget.
print(bonus_info)

# End Experiment
control.end()

# Now that the experiment is complete move the data to a subject format data org structure


subj_dir = os.path.join(exp.data.directory, str_id)
if not os.path.exists(subj_dir):
    os.makedirs(subj_dir)

print(subj_dir)
print(os.path.join(subj_dir, exp.data.filename))
# Move the behavior and pupil data file to inside a subject folder
os.rename(exp.data.fullpath, os.path.join(subj_dir, exp.data.filename))
os.rename(calibrate.log_file + '.edf', os.path.join(subj_dir, calibrate.log_file + '.edf'))
