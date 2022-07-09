%This script we will layout the basic skills to lay out behvioural data
%This will generalize
%Deshawn sambrano: DSambrano
% August 29p


%% 0 Init
clear all 
close all
clc

%% 1 Measuring time in MatLab

%There are many ways but we will do on

%tic toc
tic %Resets timer to zero
toc %Counts how much timer has elasped

%Its a cumulative stop watch


%% 2 Measuring the consistency of timeing in Matlab and seing how preallocation matter

numRep = 1e6; %Number of reps
for i  = 1:numRep % One big loop
    tic
    A(i,1) = i;
    A(i,2) = toc;
end

% This is taking so long because we did not preallocate A. The size of A
% changes each teration. Internally it has to copy and paste each time.
% Disasterous becasue some breaks request to much memory


%%
timeMicro = A(:,2) *1e6;
mean(timeMicro)

figure 
histogram(timeMicro)
mean(timeMicro)
std(timeMicro)
max(timeMicro)
plot(timeMicro)



%% Terrible so we do preallocation

numRep = 1e6; %Number of reps
A = nan(numRep,2);
for i  = 1:numRep % One big loop
    tic
    A(i,1) = i;
    A(i,2) = toc;
end



%% 
%The remaining variablity comes from other stuff thata is going in the 
% backgroud. All modern op do this. So close everything possible. Including
% internet. Close as much as possible.


%% After seeing that preallocation can cause a speedup of several orders of mag
% Lets use timing functions to capture reaction times. 


tic
pause % wait till button is pressed
rT = toc 

%% Pause is more versatile than this. You can also use it for stimulus presentation. 

% Say you want to present a stim for 200 ms


tic
pause(.2)
toc


A = nan(100,1);
for i = 1:length(A)
    tic
    pause(.197);
    A(i,1) = toc;
end




%% What if we care which button the participant pressed
%a) with user input function
tic
kP = input('Please press the k', 's') %if you dont put an s it expects a number
toc


% This works fine for user input like name age etc.
% Teriible for reactiontime because doesnt move on until pressed enter

%% b) user input without carriage return
% MATLAB stores the character that the user pressed as figure property
% Of the current figure

f5 = figure;
shg
pause
%Now we care which button the participant pressed
userPressedKey = get(f5,'CurrentCharacter'); %Is the current character property of the figure

% Modern Matlab
f5.CurrentCharacter

%% c) Make sure they participant pressed only one of two valid keys, e.g., q and p

validKey = 0

f6 = figure;
shg
while validKey == 0

pause
userPressedKey = get(f6,'CurrentCharacter'); %Is the current character property of the figure

    if strcmp(userPressedKey, 'q') == 1
        validKey = 1
    elseif strcmp(userPressedKey, 'p') == 1
        validKey = 1
    end
end


%% To really do anythin useful with user input  (be it mouse or man) you need to parse the input
%For instance in a 2 AFC experiment, stim or not and two choices,
% Ex Hit Miss Fase pose and correct jection
%We need nested IF statements to parse thise you can then package into a
%function

stimulusPresent = 1;
% p represent stim present, q not 

if  stimulusPresent == 1 & strcmp(userPressedKey, 'q') == 1
    correct = 1;
elsep
    correct = 0;
end

if stimulusPresent == 0 & strcmp(userPressedKey, 'p') == 1
    correct = 1;
else 
    correct = 0;
end
    
    
    
