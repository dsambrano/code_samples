%This script illustrates stimulus generation and presentation
%We also will do a brief descent into randomness
%Randomness is usually your friend in stimulus presentation
%Who did it and when and how to get a hold of them?

%% 0 Init
clear all
close all
clc

%% 1 Text stimuli - perhaps the simplest stimulus material 
figure
g = text(0.5, 0.5, 'Hello world') %Our first text output
%Let's center the text and make it bigger
g.HorizontalAlignment = 'center'; %Make it centered
g.FontSize = 20; %Bigger

%%
%Let's create a stimulus display of 20 o's and place them randomly
figure
numStim = 20; 
stimToDisplay = 'o';
stimPos = rand(numStim,2); %20 rows and 2 columns of random coordinates (x and y)
outputDisplay = text(stimPos(:,1),stimPos(:,2),stimToDisplay);
set(outputDisplay, 'color', 'g') %Very old school

%Fixes: Make backgound black, make the text bigger, remove the axis, bold
%the text
axis off
set(gcf,'color','k')
set(outputDisplay,'Fontsize',20); set (outputDisplay, 'Fontweight', 'bold')
set(gcf,'DockControls','off')
set(gcf,'ToolBar','none')

%Adding a target
TargetToDisplay = 'x';
TargetPos = rand(1,2); %20 rows and 2 columns of random coordinates (x and y)
TargetDisplay = text(TargetPos(:,1),TargetPos(:,2),TargetToDisplay);
set(TargetDisplay, 'color', 'g') %Very old school
set(TargetDisplay,'Fontsize',20); set (TargetDisplay, 'Fontweight', 'bold')

%% In principle - how to handle and display unicode characters
%Say we want to present 20 random unicod characters
figure
for ii = 1:numStim
    strD = char(round(rand(1,1).*10000)) ;%This yields a random unicode character from 0 to 10000
    %When trying to understand what a line of code does, go from the inside
    %out (start with the deepest parantheses level. Here: Create a random
    %number from 0 to 1, multiply by 10,000, then round to get integers and
    %interpret that as a unicode character. You could do all of this with
    %randi instead. 
    stimPos = rand(1,2); %These will be x and y coordinates
    textToDisplay = text(stimPos(1,1),stimPos(1,2),strD);
    set(textToDisplay,'FontSize',40); set(textToDisplay,'Fontweight','bold');
end

%% Simple graphical objects - circles and rectangles 
fNew = figure; %New figure with handle 
%A rectangle - by virtue of being a rectangle - can be defined with but a
%few parameters. There really are only 4 degrees of freedom: Width and Height, and a starting position
h1 = rectangle('Position',[50, 27.5, 25, 25])
xlim([0 100])
ylim([0 100])
%With the rectangle object, you can actually generate a lot more objects
%than just rectangles. It has more properties that position. For instance,
%curvature
h1.Curvature = [1 1]
%From the perspective of Matlab, a circle is just a rounded rectangle
axis square %Now the circle looks like a circle. This is an aspect ratio thing

%Transforming a rectangle gradually into an ellipsoid, by progressively
%beveling the edges
figure
h2 = rectangle('Position',[50, 27.5, 25, 25])
xlim([0 100])
ylim([0 100])
stepSize = 0.01;
for ii = 0:stepSize:1
    h2.Curvature = [ii ii];
    title(['Curvature = ', num2str(ii)])
    pause(0.1)
    shg %To make sure the figure is always on top
end

%% Make flashing colored rectangles and circles
f3 = figure %Open a new figure
h3 = rectangle('Position', [0.3 0.6 0.3 0.3]) 
h3.EdgeColor = 'w'; %Start out with a invisible (white on white) rectangle
pause(1) %Time before flash starts
h3.FaceColor = [1 0 0.5]; %Purple fill 
h3.LineWidth = 5; %Thicker width
h3.EdgeColor = [1 0.5 0]; %Orange edges
xlim([0 1])
ylim([0 1])
pause(0.1) %Flash duration
h3.FaceColor = 'w'; %Go back to an invisible (white on white) rectangle
h3.EdgeColor = 'w'; %Go back to an invisible (white on white) rectangle

%% Redo this code, but flash at a random location for a random duration with a random curvature and random colors
f4 = figure %Open a new figure
axis off
while 5 ~= 0
h4 = rectangle('Position', rand(1,4)) 
h4.EdgeColor = [0.94 0.94 0.94]; %Start out with a invisible (white on white) rectangle
pause(rand(1,1)) %Time before flash starts
h4.FaceColor = rand(1,3); %Purple fill 
h4.LineWidth = rand(1,1)*5; %Thicker width
h4.EdgeColor = rand(1,3); %Orange edges
h4.Curvature = rand(1,2);
xlim([0 2])
ylim([0 2])
pause(rand(1,1)) %Flash duration
h4.FaceColor = [0.94 0.94 0.94]; %Go back to an invisible (white on white) rectangle
h4.EdgeColor = [0.94 0.94 0.94]; %Go back to an invisible (white on white) rectangle
end

%% As we are leaning heavily on randomness, it is worth talking a bit about creating random numbers in Matlab

%First thing: Are the numbers coming out of the random number generator
%random? NO! They are 100% deterministic, but we can't distinguish it from
%randomness, so we call it pseudorandom. 
%To get truly random numbers you have to buy a hardware random number
%generator that works off a natural process that we believe to be random,
%e.g. radioactive decay, or diode noise. 
%There are many ways to generate random numbers, and you can specify them
%in Matlab. 
%Intuition: Think of an irrational number like pi. All you need it the
%digits of pi (although in practice, most people use Mersenne prime
%numbers), and a starting position. 
%The starting position is called the "seed". In practice, most people get
%the seed from the system clock. 

clock
seedMostPeopleUse = round(sum(clock)); %Gives you one round number
%Problem with this: There is "seed aliasing". Seconds and Minutes go from 0
%to 59 and hours to go from to 23, so the entire range of this is 0 to 141
%plus whatever comes from month and year and day. So from day, we get
%another 31. So the range is 172. There are only 172 unique seeds if you do
%this. 
%A better way:
%aBetterSeed = round((now*1e6)) %As per Deshawn
temp = clock;
aBetterSeed = round(sum(temp(6)*1e6)) %More precision


%Illustrating how seeding the random number generator works and also why
%the help if your friend (Matlab changes the names of functions sometimes)
seed = RandStream('mt19937ar', 'seed', aBetterSeed); %Initalize the rng
RandStream.setGlobalStream(seed); %That's the global stream where the rns come from
rand(10,1)' %This should yield 10 random numbers, but everyone should have different ones

%% Illustrating how using the same seed works and how seemingly consecutive
%seeds really yield different results
seed = RandStream('mt19937ar', 'seed', 2); %Initalize the rng
RandStream.setGlobalStream(seed); %That's the global stream where the rns come from
rand(10,1)' %This should yield 10 random numbers, but everyone should have different ones

%Lessons: 
%1 Always initialize the seed of the rng. Matlab does use the system clock
%by default. But you might share that with other people and you don't know
%the seed. 
%2 If you want a unique seed, make sure it is likely unique (not the silly
%one we first described)
%3 If you do want the same numbers or want to recreate your stimulus or
%want to reuse the numbers, make sure to note what the seed is. 

%% So far, we have covered drawing with replacement. How about drawing numbers without replacement?

%Permutations!

%Drawing with replacement, explicitly:
%Say we want to draw random integers from 1 to 100 to assign trial orders
dwr = randi(100,[100,1])' %Drawing 100 numbers from 1 to 100
unique(dwr) %There are duplicates!

%Drawing without replacement: 
dwor = randperm(100) %Putting 100 numbers into random order
%unique(dwor)

%Just like all other randomization functions, randperm works off the same
%seed as well. 

%% Images and image handling in Matlab (visual stimuli)

%The first thing to understand is how Matlab represents images in the first
%place. 
%Every pixel (picture element) on the screen is made up of 3 transistors (LEDs) 
%You can turn the voltage of each on and off. They correspond to 3 primary
%colors: R(ed), G(reen), B(lue). With those, you can make any light. Each
%can take 256 values (2^8) - 8 bit. ~Represent about 16 million different
%colors. So the appropriate data type is uint8 - that's an unsigned (going
%from 0 to 255 - there is no negative light) 8 bit integer data type. Unsigned: Only takes positive values. 
%The reason for this is economy. In double precision, each value takes 8
%bytes. So the representation as uint8 saves almost an order of magnitude
%in memory. 
A = randi(100,[1e6 1]);
A = uint8(randi(100,[1e6 1]));

testDisp = uint8(zeros(3,3,3)); %This yields a 3x3 matrix that will automatically be interpreted as an image by Matlab.
%The first two here are x and y, the third one is the "channel" - R, G or B

%Look at the matrix as an image:
image(testDisp)
shg
pause

%Turn on the center pixel, and make it white: 
testDisp(2,2,:) = 255; %Max, fully on
image(testDisp)
shg 
pause

%Allie's pixel - yellow 
testDisp(1,1,1:2) = 255; %Again, max
image(testDisp)
shg 
pause

%Link's pixel - salmon
testDisp(2,1,1) = 250; 
testDisp(2,1,2) = 128;
testDisp(2,1,3) = 114; 
image(testDisp)
shg 
pause

%Olesia's pixel - turqoise
herColor = [64,224,208]
testDisp(3,3,:) = herColor;
image(testDisp)
shg 
pause

%% So far for basic pixel handling and addressing
%Just one thing to note if you use uint8's: 
testDisp(2,3,2) = 1000;
testDisp(2,3,2) %The max value of an uint8 is always 255, no matter how much over you go. 

%% Let's make some gradients - on the way to complex images
%This is now the maximal resolution, given uint8
gradDisp = uint8(zeros(128,128,3)); %Now 10x10, but we still only have 3 channels
%We could use nested for loops. Or we could use meshgrids
for ii = 1:128
    for jj = 1:128
        gradDisp(ii,jj,1) = ii-1+jj-1; %Red
        gradDisp(ii,jj,3) = ii-1+jj-1; %Blue
    end
end
image(gradDisp)
shg

%% Natural images

%Loading "the dress" into Matlab
dress = imread('thedress.jpg'); %Imread is an image read function that puts the image file into matrix format
size(dress)
figure
image(dress)
%The dress has been stretched. The scaling is off. Aspect ratio
axis equal %Pixels take up the same space in each dimension

%Once something is in a matrix - and we will do this later with sounds -
%you own it. You can do matrix operations on it. For instance, you can look
%at different channels
figure
subplot(2,2,1)
image(dress) %The full dress
subplot(2,2,2) %Looking only at the red channel
redChannel = dress; %Make a copy of the dress
redChannel(:,:,2:3) = 0; %Turn green and blue off
image(redChannel)
subplot(2,2,3) %Looking only at the green channel
greenChannel = dress; %Make a copy of the dress
greenChannel(:,:,[1 3]) = 0; %Turn red and blue off
image(greenChannel)
subplot(2,2,4) %Looking only at the blue channel
blueChannel = dress; %Make a copy of the dress
blueChannel(:,:,1:2) = 0; %Turn red and green off
image(blueChannel)

%By Tina's suggestion let's look at only the blue channel as a surface
figure
bS = surf(blueChannel(:,:,3));
bS.LineStyle = 'none' %By looking at is as a surface plot, it becomes more clear that there is more blue at the bottom than on top

%If you don't like any of the existing colormaps, you can make your own.
%It's just a mapping of shades to numbers. 
france = [0 0 1; 1 1 1; 1 0 0]; %Blue white and red
colormap(france)

%This obviously emphasizes contrast in the extreme. We could make a more
%gradual map, but we're running out of time. Point is siply that you are
%not restricted to using MATLABs predefined colormaps. 

%Two advantages of making your stimuli in Matlab rather than - say in
%Photoshop or illustrator are: There are no black boxes - you know exactly
%what you are doing. If you have to make a lot of them, you can make them
%fast. For instance, with loops. 

%% Some simple image manipulations
figure
image(dress)
shg
pause
image(flipud(dress)); %Flip matrix upside down
shg
pause
image(fliplr(dress)); %Flip the matrix from left to right

%% As we said, we can now do image manipulations. For instance, it has been suggested in the literature
%that the dress is perceived as more W/G, the brighter it is. We can easily
%make stimuli to test this here .
figure
dress2 = dress; %Make a copy of the dress
for ii = 1:100 %We want to make it gradually brighter
    dress2 = dress2 + 1;
    image(dress2)
    shg
    pause(0.1)
end
   
%% Instead of making the whole thing brighter, how about just making it bluer
figure
dress2 = dress; %Make a copy of the dress
for ii = 1:100 %We want to make it gradually bluer
    dress2(:,:,3) = dress2(:,:,3) + 1;
    image(dress2)
    shg
    pause(0.1)
end

%% Making only the bottom half darker
figure
dress2 = dress; %Make a copy of the dress
for ii = 1:100 %We want to make it gradually darker
    dress2(375:750,:,:) = dress2(375:750,:,:) - 1;
    image(dress2)
    shg
    pause(0.1)
end

%% If you had done this in March 2015, you would have had a Currenty Biology paper: Inverting the dress
dressInverted = 255-dress; %This inverts the dress colors
figure
image(dressInverted)

%% In the interest of quick and dirty image manipulations: Blurring the dress
%With convolution. We'll talk a lot about this in Math tools, for now think
%of it as a moving average
figure
image(dress) %Start with the unfiltered image
pause
kernel = ones(50); %How many pixel values you average together
lpDress = convn(dress,kernel,'same'); %By default, Matlab zero-pads. But that creates edge artifacts and makes it bigger
%If you use the argument "same", it keeps the same dimensionality. If you
%use the argument "valid", we don't zero-pad at all. But that makes the
%image smaller, it depends on what you count in terms of where the kernel
%hits the image and what to pad with. 
%To get back into the same color space from 0 to 255, we need to divide by
%the kernel sum
lpDress = lpDress./sum(sum(kernel)); 
image(uint8(round(lpDress))); %Convolution makes it a double, division creates fractions, so we have to undo that
%Basically back to something Matlab recognizes as an image. 
shg

%% Edge detection
hpDress = dress-uint8(lpDress); 
aboveThresholdIndices = find(hpDress > 10); %This finds the indices of values larger than a threshold
hpDress(aboveThresholdIndices) = 255; 
image(uint8(hpDress))
shg

%% Edge detection2
Dress3 = uint8(diff(dress)); %Differentiation/derivative
aboveThresholdIndices = find(Dress3 > 10); %This finds the indices of values larger than a threshold
Dress3(aboveThresholdIndices) = 255; 
image(uint8(Dress3))
shg

%% ZOUNDS!
%Reinforces the philosophy of putting stuff into a matrix and then owning
%it
load handel
figure
plot(y) %Looking at it
sound(y,Fs*0.5) %Listening to it, but at a lower sampling frequency
%Fs is sampling frequency. This translates to pitch.

%A song
[BS, samplingRate] = audioread('whatever.mp4');
%In BS, we now have a long vector of membrane amplitude deflections from -1
%to 1. The two columns represent stereo.
%%
figure
plot(BS(:,1))
shg
sound(BS(5.5e6:6.5e6,1),samplingRate)

BSconv = conv(BS(:,1),ones(1000,1)); 
sound(BSconv(1:1e5),samplingRate) %It will be an echo

A = rand(1e6,1);
sound(A,samplingRate) %White noise - the sound of randomness

%% Pure tones and chords, fifths
freq = 440;
freq2 = 660; %A fifth
freq3 = 554; %Major
fs = 8000; 
t = 0:1/fs:2; %make a time base from 0 to duration in steps of sampling rate
y = sin(t.*freq.*2.*pi);
y2 = sin(t.*freq2.*2.*pi);
y4 = sin(t.*freq3.*2.*pi);
y3 = (y + y2); %A plus a fifth - dividing by 2 
y5 = (y3+ y4)./3; %Chord - dividing by 3 because we are clipping
sound(y,fs)
sound(y2,fs)
sound(y3,fs)
sound(y5,fs)


