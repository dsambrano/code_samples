# Experiment pygaze

EYETRACK = True

# Calibrate
if EYETRACK:
    import calibrate
    import pygaze
    tracker = calibrate.cal()


# Start
if EYETRACK:
    tracker.log('start_time')
    tracker.start_recording()

# Log messages/events
if EYETRACK:
    tracker.log('ID {} type {} block {} trial {} shock {} event confirmation'.format(str_id, block_type, i, count, shock_trial))


# Stop recording
if EYETRACK:
    tracker.log('end_time')
    tracker.stop_recording()
    tracker.close()