# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:37:47 2018

@author: lindadevoogd
"""

# Import libraries
import expyriment

# SET BEFORE THE EXPERIMENT [only vars in capital letters can be changed]
#------------------------------------------------------------------------------
SUBJ_CODE = "FCWML132"
TESTING = 0 # 1 or 0
REFRESH_RATE = 60  # In Hz


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
        name= SUBJ_CODE + " - Practice N-Back",
        background_colour = (125,125,125))  #background color
expyriment.control.initialize(task)
task.add_data_variable_names(["Logevent","Onset","Key","RT","Dur_Dig","Dur_Fix"])

# Screen
frame = 1000 / REFRESH_RATE

# Port setting
port_shock = [100,200] #code and duration
port_biopack = 1 #code
if portconnected == 1:
    port = expyriment.io.ParallelPort(0xC020) #python 2 without quotation marks "0xC020" vs 0xC020    

# Keys, Clock
keys = expyriment.io.Keyboard()
keys.set_quit_key(expyriment.misc.constants.K_ESCAPE) #with esc you can quit
responsekey=expyriment.misc.constants.K_SPACE
experimenterkey=expyriment.misc.constants.K_5 #so pp cannot accidently press space bar and continue

# Instructions
instructions1 = " \n \
We will first test the recording equipment .\n \
\n \
Wait for the instructions of the experimenter. \n \
\n \
"
instructions2 = " \n \
We will now set up the shock level.\n \
\n \
During this experiment you will receive electrical shocks.\n \
We will calibrate the shock level for you so that it is unpleasant, \n \
but not painful. \n \
You will receive 5 shocks in total and for each shock we will ask you \n \
to rate how unpleasant the shock was with [0] no sensation and [9] very high \n \
intentity or painful.  \n \
\n \
Wait for the instructions of the experimenter. \n \
\n \
"

instructions3 = " \n \
EXPERIMENT \n \
In this experiment you will see two pictures. One of the pictures \n \
is paired with an electrical shock. The other picture is NEVER paired \n \
with an electrical shock. Your task is to pay attention and figure out \n \
which one is paired with the electrical shock. \n \
\n \
The picture is not always paired with an electrical shock, \n \
so it may happen that for a period of time you do not receive a shock. \n \
\n \
"

instructions4 = " \n \
DIGIT TASK \n \
Additionally, it may happen that you have to perform a digit task.\n \
\n \
It this happens, you will see digits on the screen that are being \n \
presented one after the other. Your task is to press \n \
the spacebar each time the current digit is the same as a \n \
digit presented 2 digits back. \n \
To clarify, when the current digit is the same as the one before the \n \
previous one. \n \
In this example: [2 3 4 3 5] press the key with second [3]. \n \
If this is not clear, please ask the experimenter for a clarification.\n \
\n \
Note that this digit task may (or may not) appear at moments \n \
during the experiment. The digits do not in anyway predict the electrical \n \
shocks you will receive in the experiment \n \
\n \
When this happens it is your task to perform \n \
the task as well as you can. You will now first practice the task.\n \
\n \
PRESS SPACE BAR WHEN READY"

instructions5 = " \n \
DIGIT TASK \n \
Additionally, it may happen that you have to perform a digit task.\n \
\n \
It this happens, you will see digits on the screen that are being \n \
presented one after the other. Your task is to press \n \
the spacebar each time the current digit is the same as a \n \
digit presented 1 digit back. \n \
To clarify, when the current digit is the same as the previous one. \n \
\n \
In this example: [2 3 3 4 5] press the key with second [3]. \n \
If this is not clear, please ask the experimenter for a clarification.\n \
\n \
Note that this digit task may (or may not) appear at moments \n \
during the experiment. The digits do not in anyway predict the electrical \n \
shocks you will receive in the experiment \n \
\n \
When this happens it is your task to perform \n \
the task as well as you can. You will now first practice the task.\n \
\n \
PRESS SPACE BAR WHEN READY"

# STIMULUS SETTINGS
#------------------------------------------------------------------------------

#n-back
n_blocks = 5
n_dig = 10
dur_dig = 1100
dur_digfix = 400
dur_fix = (dur_dig + dur_digfix) * n_dig
    
# DESIGN [experiment/task, blocks, trials, stimuli]
#------------------------------------------------------------------------------
# Create design (blocks and trials)
# Create stimuli (and put them into trials)
# Create input/output devices (like button boxes etc.)

# One block so no loop
block = expyriment.design.Block("Block")

# Create Design, Loop over trials
for c_trials in range(n_blocks):
    
    # Trial [define properties]
    trial =  expyriment.design.Trial()
    trial.set_factor("nBlock",n_blocks)
    
    # Add stim to trial and trial to block
    block.add_trial(trial)

# Add block to task
task.add_block(block)

# Create digit
stim_dig = []
n_seq = [1,2,3,4,5]
for c_dig in n_seq:
    dig = expyriment.stimuli.TextLine(text="{0}".format(c_dig),
                                      text_size=50,
                                      text_colour=[60,60,255])
    #dig.preload()
    stim_dig.append(dig)
rnd=expyriment.design.randomize.rand_element

# Other stimuli
fixcross = expyriment.stimuli.FixCross(colour=(60,60,255))                      # default fixation cross
fixcross.preload()
blank = expyriment.stimuli.BlankScreen()                                        # blackscreen
blank.preload()

 # Function waits for a duration while logging key presses
def wait(dur):
    task.keyboard.clear()
    task.clock.reset_stopwatch()
    while task.clock.stopwatch_time < int(frame * int(round((dur) / frame, 5))) - 2:
        task.keyboard.check(keys=responsekey)
        
        
# RUN
#------------------------------------------------------------------------------

# Start experiment
expyriment.control.start(subject_id=int(SUBJ_CODE[-3:]))
port.send(0)
# Recording
expyriment.stimuli.TextScreen("", instructions1, 
                              text_colour=[0,0,0]).present()
task.keyboard.wait(experimenterkey)

# Shock work up
if portconnected == 1:
    port.send(0) # to make sure it is off!
expyriment.stimuli.TextScreen("", instructions2, 
                              text_colour=[0,0,0]).present()
task.keyboard.wait(experimenterkey)


# Conditioning instructions
expyriment.stimuli.TextScreen("", instructions3, 
                              text_colour=[0,0,0]).present()
task.keyboard.wait(experimenterkey)


# N-Back instructions
expyriment.stimuli.TextScreen("", instructions4, 
                              text_colour=[0,0,0]).present()
task.keyboard.wait(responsekey)

# Loop over trials/blocks
for trial in task.blocks[0].trials:

    # ITI present
    fixcross.present()
    task.data.add(["fixonset_0",task.clock.time,"None","None","None","None"])
    wait(5000/speedup)
    
    # prepare block
    two_back = 0
    one_back = 0    
    
    #loop over random digits
    for d in range(n_dig):
        
        # Prepare trial
        task.keyboard.clear()
        responses = []
        
        # Draw random digit [in ~25% the case it is a 2-back]
        if two_back == 0:
            p_dig=rnd(stim_dig)
            t_nback="digonset_"
        elif rnd([1,2,3,4]) == 1:
            p_dig=stim_dig[two_back-1]
            t_nback="twoback_"
        else:
            temp_stim_dig=stim_dig[:] #copy list not variable otherwise changes are applied to original variable
            temp_stim_dig.pop(two_back-1) #remove nback
            p_dig=rnd(temp_stim_dig)
            t_nback="digonset_"
        
        #update counters
        two_back=one_back
        one_back=int(p_dig.text)
        
        #present and log
        p_dig.present() 
        dig_onset = task.clock.time
        task.data.add([t_nback+p_dig.text,dig_onset,"None","None","None","None"])
        
        # Reset stopwatch each trial
        task.clock.reset_stopwatch()
        
        # Wait and log responses        
        while task.clock.stopwatch_time < int(frame * int(round((dur_dig/speedup) / frame, 5))) - 2:
            key = task.keyboard.check(keys=responsekey)
            if key is not None:
                responses.append((key, task.clock.stopwatch_time))
        
        # Present black screen
        blank.present() 
        dig_time = task.clock.time - dig_onset
        dig_fix_onset = task.clock.time
        
        # Wait and log responses        
        while task.clock.stopwatch_time < int(frame * int(round(((dur_dig+dur_digfix)/speedup) / frame, 5))) - 2:
            key = task.keyboard.check(keys=responsekey)
            if key is not None:
                responses.append((key, task.clock.stopwatch_time))  

        # Log first response        
        try:
            keypressed, RT = responses[0]
        except:
            RT = keypressed = None

        dig_fix_time = task.clock.time - dig_fix_onset
        
        #collect data
        task.data.add(["response_"+p_dig.text,task.clock.time,keypressed,RT,dig_time,dig_fix_time]) #LOG 
        

# End
expyriment.control.end(goodbye_text="This is the end of the practice block!",
             goodbye_delay=2000)

