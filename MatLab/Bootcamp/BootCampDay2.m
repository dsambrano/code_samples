%Get into the habit of writing a header paragraph at the beggining of your
%scrip. It should contain the following information: 
%1. What this script is supposed to do? In this case: Make some figures to
%illustrate basic MATLAB functionality
%2. Assumptions and dependencies: For instances, data that is needed, other
%files that need to be run before, directories. In this case: None
%3. Version history. In this case: V1 - 08/29/2017 The full script.%4.
%Contact information: Who is responsible for this and how do I reach them?

%% Double percent signs without space in between, sets up what is called a %"code section" 
% Organize into sections where each section does one thing. Helpfully

%% Initialization
% After the header, each script should have an init section. In this
% section, we do two thinkgs: Create a "blank slate" (or as blank as we
% want it) and set constants that will be used thorughout the code. That
% way you dont have to search them. 


% Init proper
clear all % clears any potential things 
close all % close all figures.
clc %Clears command window


% Flags and constants
stepSize = .1;
sinCycles = 5;
lineThick = 3;
lineC = 'k';
fontS = 18;
echo off;

%% Basic Plotting
%This section illustrates basic plotting funtionality
figure % Open a new figure
x = 0:stepSize:sinCycles*2*pi; % Creates X
y = sin(x);
h = plot(x,y);
shg %Show graph (sometimes figure comes behind the screen)
xlim([min(x) max(x)]) % Change the plotting range
xlabel 'Time in Seconds'
yHand = ylabel('Voltage in microVolt')
tHandle = title('Voltage over Time')



%% Taking full control of the 
% There is a hierarchy of graphical elements.
% At the top is the screen, or roo (or 0).
% The screen has children. Those are the figure (1 to n)
% Each figure has axes. In this case 1, but can be more
% Each axes has objects. 
% Each of these have properties
get(0) % Get the properties of the screen
scrSz = get(0, 'ScreenSize'); %This gets the dimensions of the screen
%set(gcf, 'Position', scrSz); % Make it full screen.
% Position is a four element vector the first two values are the x and y
% bottom left vertext, then the width in pixels, then the height.
% in general, propoersal at obtained with get and set with set
% General syntax: Which object ot manipultate and tehn proper in quotes and
% then the value

% Making the line the correct way
set(h, 'LineWidth', lineThick) % Set Line Thickness
set(h, 'Color', lineC) % Set Line Color
% To change the font of the entire axes, wee nee to address
set(gca, 'FontSize', fontS) % Properties of the current axes can be gottnen with get(gca)
set(gca, 'FontAngle', 'italic') % set 
box off
set(tHandle, 'FontAngle', 'normal')
set(gcf, 'Color', 'w') %Make figure backgournd white
yHand.Color = [255/255 140/255 0/255]
h.LineStyle = '--';

% Get a list fo figures on the screen
screenProp = get(0)
screenProp.Children
axesProp = get(gca) % Get current axes properties field on the left and 
% with a dot and either get or assign a value on the right


%% Adding a 2nd Line to the same Plot
z = cos(x); % now add cosine of x

hold on % Keeps old plot there

h2 = plot(x,z, 'color', 'r') % Red cosine
h2.LineWidth = lineThick; %Use dot notation not set


% Adding a legend
legend([h,h2], 'Condition1', 'Condition2', 'Location', 'NorthEastOutside')



%% Let's make a new, multi-panel figure
fakeX = 0:.5:sinCycles*2*pi;
fakeY = sin(fakeX);
fakeZ = cos(fakeX);
f2 = figure % Make a new fiture with a new figure handle
set(f2, 'color', [.85 .85 .85])
pan1 = subplot(2,1,1)
h3 = plot(x,y)
h3.LineStyle = '-';
hold on
h5 = plot(fakeX, fakeY, '.')
h5.MarkerEdgeColor = [.5 0 1]
h5.MarkerSize = 12;
pan2 = subplot(2,1,2)
h4 = plot(x,z)
h4.LineStyle = '-';
h4.MarkerEdgeColor = [0 1 0]
h4.MarkerSize = 12;
hold on
h6 = plot(fakeX, fakeZ, '.')
h6.MarkerEdgeColor = [.5 0 1]
h6.MarkerSize = 12;



%% Illustrating Subplot
% First argument is number of row,
% Second is number of columns
% Third where in subplot, it is row wise ordering.
f3 = figure 
subplot(3,2,1)
plot(x,x)
title '1'
subplot(3,2,2)
plot(x,x)
title '2'
subplot(3,2,3)
plot(x,y)
title '3'
subplot(3,2,4)
plot(y,y)
title '4'
subplot(3,2,5)
plot(y,z)
title '5'
% We expected a circle but got an ellipse
% We need to fix the aspect ratio
axis square
subplot(3,2,6)
plot(z,z)
title '6'

f3.Children % New figure has six axes


%% HISTOGRAMS! 9Frequenceies per bin)
%We discretize a continous variable intor bins. And we count how often a
%values falls into any given bin. And just count them, then plot that. Each
%Bin is a bucket

SATA = randn(1e3,1); % Make 1 million numbers 
nBins = 20; % Cut the continous dist into 100 pieces
% There are two ways on doing this: one ancient and one modern
subplot(1,2,1);
hHand = hist(SATA,nBins); % Make a histogram the old way
%Giving a handle yields the values, but doesnt plot it
hist(SATA,nBins); % Need to plot it again
xlim([-5 5]);
subplot(1,2,2);
hHand2 = histogram(SATA,nBins); % Histogram the new way
%Giving a handle yields the handle and plots it
hHand2.FaceColor = 'r'; %Red Bins
hHand2.FaceAlpha = .4; %Opacity/transparency
xlim([-5 5]);

shg

%We are getting slightly different results because the two functions are
%using two slightly different binning practices.


%% Bar Graphs and error bars
%Bar graphs are for discrete conditions
numbCond = 4; % Number of conditions
x = 1:numbCond;
y = 1:numbCond; 
z = ones(1,4) .*.75; % variability (error)

figure
subplot(1,2,1) % Just bar graph
LinkT = bar(x,y)
set(LinkT, 'FaceColor', [.85 .85 .85]); % A light shade of gray
subplot(1,2,2) % To go with the times and represent variablity
% You could just plot the error bars. But most want error or bar
Deshawn = bar(x,y);
set(Deshawn, 'FaceColor', [.85 .85 .85]); % A light shade of gray

% now we need to super impose error
hold on
%TinaDina = errorbar(x,y,z); % These are symetric
TinaDina = errorbar(x,y, zeros(1,4),z, 'CapSize', 20); % These only go up
TinaDina.LineStyle = 'none';
TinaDina.Color = 'g';
TinaDina.LineWidth = 3;

%Putting both subplots on the same access
yMax1 = max(Deshawn.YData)
yMax2 = max(Deshawn.YData)+ max(TinaDina.YPositiveDelta)
yMax = max(yMax1, yMax2)
subplot(1,2,1)
ylim([0,yMax])
subplot(1,2,2)
ylim([0,yMax])



%% So far, we only made 2d plots. Lets make a 3d plots.
% They are nice for making covers for jounals

% The key functino is meshgrid
% It is going to be the first function we used that has two ouput arguments
% We need  to caputure that set with square brakcets

% What is a meshgrid is doing is to creat two gradient (ramps,

% This is a bit abstract , so lets just show what it looks like - and it is
% very powerful

[X,Y]  = meshgrid(-3:.01:3 -3:.01:3);

% Visualizing what is creates
figure
subplot(1,2,1)
imagesc(X) % Imagesc creates a scaled image of matrix (max value is max color)
subplot(1,2,2)
imagesc(Y)
colorbar

%Since 2014b, they changed default color from jet to perula
colormap('jet')

%We can  now use 2 inputs to our plottin function, both x and y.
% So far we did everythin with x only
Z = X.^2 + Y.^2;  % Z is linear combo of X and Y and eat point in mesh grid

pf = figure
parab = surf(X,Y,Z); % 3d plot
parab.LineStyle = 'none'; % Take off gridlines
parab.FaceColor = 'interp'; %Interpolate colors
colormap('jet') % 
colorbar % Show legend



%% Saving figures
% Very hairy topic. No exiting routine is good.
print('parab.png', '-dpng')



%% To understan what meshgrid does lets understand what imagesc does
figure
PascalTriangle = pascal(5) %Pascal's triangle
imagesc(PascalTriangle) % Image c makes the larges value the brightes color in the color map





%% Open a specific figure with specific properties
% f1 = figure % f1 is a veriable that serves as a figure handle
% set (f1, 'Position', [300, 300, 300, 300])
% If you don't assign a handle ot a figure or a plot, it will still plot,
% but you won't have a handle on it. It is the handle that allows you to
% change properties programmatically.





