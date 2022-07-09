#!/usr/bin/env osascript

set das_inputzen to system attribute "TM_SELECTED_TEXT"
if das_inputzen is equal to "" then
	set das_inputzen to system attribute "TM_CURRENT_LINE"
end
set mt to missing value

tell application "Terminal"
	repeat with w in every window
		repeat with t from 1 to (count tabs of w)
			set processList to processes of item t of tabs of w
			if processList contains "MATLAB_maci64" then
				set mw to id of w
				set mt to t
			end if
		end repeat
	end repeat
	if mt is not equal to missing value then
		set mytext to "yay!"
	else
		set mytext to "Sadness"
	end if
	-- display dialog mytext
	
    if mt is not equal to missing value then
        do script das_inputzen in tab mt of window id mw
    end if
end tell

if mt is equal to missing value then
    return "No running instances of MATLAB found."
else
    return
end if