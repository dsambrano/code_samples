% So far, we have just used scripts as code repositories. 
% Basically so we dont have to retype stuff in the command line and so we
% can edit it. The real power comes from controlling the program flow

% Deshawn Sambrano: DSambrano@nyu.edu
% Version History?


% General heuristics:
%Loops = serial
% Switches - parallel

%% 0 Init
clear all
close all
clc


% Define Constants
startLoop = 0
endLoop = 1e6

%% 1a: FOR loops (There are several kinds of loops)
% Another analogy that might be useful. Some DNA codes for proteins. Other parts
% of the DNA switch genes on and off.
%Programming languages have a similar structure. Commands (in black) do
%stuff. Other instructions (in blue) modify how code is executed.

%These are reserved key words.

% Simple loop: counter or tally
% Syntax: for (a vector) do all instructions each time you go through the
% loop. Close loop with end

for i = startLoop:endLoop % starts the loop
    i % output the counter
end % ends the loop



%% Make this more explicit. how indexing works
indexVector = [3 12 -1 5]
for counter = indexVector
    counter
end



%% Using for loops to do something useful, e.g., running a tally
indexVector = startLoop:endLoop;
tally = 0; %Initialize the tally
%Tally keep track of cumulative sum
for i = indexVector
    tally = tally + i;
end
tally


%% Mixing switches into the loop.
indexVector = startLoop:endLoop;
tally = 0; %Initialize the tally
Knowledge = 912
%Tally keep track of cumulative sum
for i = indexVector
    tally = tally + i;
    if i == Knowledge % IF and ONLY IF this is true
        tally % Output tally
    end % Still need end
end
tally


%% Do something more  than once

indexVector = startLoop:endLoop;
tally = 0; %Initialize the tally
iCare = 5;
Knowledge = 912
%Tally keep track of cumulative sum
for i = indexVector
    tally = tally + i;
    if i < iCare % IF and ONLY IF this is true
        tally % Output tally
    end % Still need end
end
tally

%% Using a more complicated use case to illustrat if statements

% Use Case: Raffle

raffle = randi(10,1) %Draws a random intigter
if raffle == 10
elseif raffle == 9
    disp('Close')
else
    disp('Loser')
end 
raffle



%% while loops
% When we konw how often we want to loop
% While loops when we dont know how often we have to loop

raffle = 0;
numTries = 0;

while raffle ~= 10
    raffle = randi(10,1) %Draws a random intigter
    numTries = numTries + 1;
    if raffle == 10
        disp('WINNER')
        numTries
    elseif raffle == 9
        disp('Close')
    else
        disp('Loser')
    end 
end


%% String handling
%MATLAB sucks with strings
% {} are used for string handling, csells and structures.
%A cell is a matrix of matrices.
% Cells dont have to be consistent


ourMatrices = cell(3,1); %Declares a cell
M1 = rand(10,1);
M2 = rand(5,5);
M3 = zeros(1,99);

ourMatrices{1,1} = M1;
ourMatrices{2,1} = M2;
ourMatrices{3,1} = M3;


% For instance, you might represent all trials of a given participants with
% a matrix but each p will have a different number of trials. And you can
% loop through them

% Back to string handling
name1 = 'betty';
name2 = 'becky';

% There is a whole array of string handling functions. 
strcmp(name1,name2); % Compares whther strings are the same


%num2str obvious and str2num again obvious

%you cant store strings in a matrix
Names{1,1} = name1;
Names{2,1} = name2;


%% A structure is a great data type fore storing info
% They are labeled cells essentially
% They are not that great for computing things so you might have to pull
% something out of storage 

%Analogy
% DNA stores in structure
% RNA does the actual work
%Sotre with structure and compute with arrays

participants = struct(); %Create structure
% as the pictogram shows, they are tress (nested and structured

participants(1).Name = 'Link';
participants(2).Name = 'Dina';
participants(3).Name = 'Tina';

participants(1).Code = 'A';
participants(2).Code = 'B';
participants(3).Code = 'AB';

% Big advantage of structure: You can mix and mathc whatever you want -
% numbers, strings, dates, matrices, cell array, etc. 
% Its nice because structures can have holes


participants(1).Age = 18;
participants(2).Age = 19;
participants(3).Age = 20;

% Adding data
participants(1).Data = [101:105];
participants(2).Data = [4:8];
participants(3).Data = [1:3];


% Multi-layer structures
participants(1).Data2.cond1 = [101:105];
participants(2).Data2.cond2 = [4:8];
participants(3).Data2.cond2 = [1:3];