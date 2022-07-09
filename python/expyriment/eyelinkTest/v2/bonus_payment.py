#!/usr/bin/env python
#  /Users/deshawnsambrano/anaconda/envs/expy/bin/python  # example
import numpy as np
import os
from expyriment import misc

def bonus(block_num, trial_num, f_name, num_blocks, num_block_trials):
    bonus_keys = ['Choice', 'val', 'winColor', 'bag']
    data = misc.data_preprocessing.read_datafile(os.path.join('data', f_name))
    block_vec = np.array([x for x in range(num_blocks)])
    trial_vec = np.array([x for x in range(num_block_trials)])
    trial_ind = block_vec[block_num] * len(trial_vec) + trial_num
    temp_dict = dict(zip(data[1],data[0][trial_ind]))
    bonus_dict = {}
    for key in bonus_keys:
        bonus_dict.update({key: temp_dict[key]})

    return(bonus_dict)