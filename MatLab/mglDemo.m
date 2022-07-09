

%%0Int
addpath(genpath('~/Drive/CodeSamples/MatLab/ToolBoxes/'))
close all; clear all; clc
if mglSystemCheck ~= 1
    disp 'WARNING ASSUMPTIONS ARE NOT MET'
    pause
end

%%

% Open the screen, 0 specifies to draw in a window. 
  % 1 would be full screen in the main display
  % 2 would be full screen in a secondary display, etc... 
  mglOpen(0);
  
  % Select the coordinate frame for drawing
  % (e.g. for a monitor 57 cm away, which has width and height of 16 and 12 cm). 
  mglVisualAngleCoordinates(57,[16 12]);
 
  % Draw the text in the center (i.e. at 0,0)
  mglTextDraw('Hello World!',[0 0]);
 
  % The above is drawn on the back-buffer of the double-buffered display
  % To make it show up you flush the display.
  % This function will wait till the end of the screen refresh
  mglFlush;
  
  pause 
  
  mglClose;
