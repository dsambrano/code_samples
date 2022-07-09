% This Script will focus on data analysis, this is of spiking data
%The data represent how much a give participant liked the movies  Matrix 1
%to matrix 3. 
%Question: Are there significant differences in liking

%Deshawn Sambrano: DSambrano@nyu.edu
%September 1st, Version 1

% Analysis structure/cascade Steps:
% 1) loader: Retina
% 2) Pruner/integritychecker/filter: Plausible data?: LGN
% 3) Categorizer: V1 primary visual cortex
% 4a.b.c) Calculator, 1 section per question or analysis etc. 
% 5) Plotter: Output, action in 
% 6) Wrapper

% Programming structure: % Make a big comments hiierarchy to map onto this
% 1) strategic goals
% 2) Tactics
% 3) Implementation, write the code
% I logical paragraph/section to fit one screen in the editor (I like this)



%% 0 Init 
clear all; close all; clc


% Constants that the experimenter knows
numbCond = 12;
numTrial = 15;
spikeTimes = cell(numbCond,numTrial); % Container for spike times by condition and trial usefu for Ras plot
allSpikes = cell(numbCond,1); % Contain all spikes of a conditions useful to mak the psth
orientation = 0:30:330;

%% 1 loader
load('data/MT_neuron.mat');


%% 2 Pruner

% In this case nothing to do, prof already did this for us. Only valid
% spikes left in dataset


%% 3. Formatting - bringing data into useable format
allSpikes = cell(numbCond,1); % Contain all spikes of a conditions useful to mak the psth
% use concatination to fill so needs to be initialized here. or it will
% just be added
for i = 1:numbCond % Go through all conditions
    for j = 1:length(BLIDS{i,1}) % Go through all trial numbers per condition
        spikeTimes{i,j} = spiketimes{BLIDS{i,1}(j),1};
        % Whiles we are here we are goig to make a big vector with concat
        allSpikes{i,1} = cat(2,allSpikes{i,1}, spikeTimes{i,j}); % cat 2 concates by columes which is how the other is so its is best
    end
end
spikeTimes{4,1:3}; % This should equal the same as the second line. Double check as a manipulation 
spiketimes{BLIDS{4,1}(1:3),1};

spikeTimes{4,5} == spiketimes{BLIDS{4,1}(5),1}; % Manipulationcheck


% Now we need to check for allSpikes: These should match
spikeTimes{1,14:15};
allSpikes{1,:}(205:214)


%% 4 Analysis
% Calculate the mean firing rate and SD per condition
% There is a long baselin. 4000ms after trial oset.
% And was on for 500ms
for i = 1:numbCond
    for j = 1:numTrial
        spikeCounts(i,j) = length(find(spikeTimes{i,j} >4000));
    end
end

%Cuz we want mean of rows not colums
meanSpikeRate = mean(spikeCounts').*2 %One way
%meanSpikeRate = mean(spikeCounts,2).*2 %Another way

stdSpikeRates = std(spikeCounts').*2 % *2 is to convert it to a rate since it was .5 seconds that makes it per second


%% 5 Plotting

% a) Raster plot - thats what we will use the spikeTiems container for

for i = 1:numbCond % through conditions
    figure(1)
    for j = 1:numTrial %thorugh trials
        for k = 1:length(spikeTimes{i,j}) % Through all spikes in that trial
            %Line sintax give it 2 x and y . but vertical x is identical. y
            %position is trial number
            h = line([spikeTimes{i,j}(k) spikeTimes{i,j}(k)], ... % Continues to next line
                [j-1 j]); %plot each spiketime as line to next 
            set(h,'color','k') % Make them all black
        end
    end
    title(['Orientation ', num2str(orientation(i)), char(176)]); % OK?
    pause
    close(1)
end
                


%% 5b PSTH
% Parse all spikes by bines. Peristimulus time histogram

for i = 1:numbCond
    figure 
    binWidth = 100;
    maxTime = 4500;
    edges = 0:binWidth:maxTime; % This is what we will use to parse the allSpikes container
    parsedSpikes = histc(allSpikes{i,1},edges); % histogram count - how often did a spike fall in a given bin
    parsedSpikes = parsedSpikes ./numTrial .* (1000/binWidth); % If we did nothing this would just eb spike counts. Weed need to normalize by fraction of the bin width
    plot(edges+binWidth, parsedSpikes)
    xlabel('ips')
    ylabel('time in ms')
    line([4000 4000], [0 max(ylim)], 'color', 'k', 'lineWidth', 3)
    title(['Orientation ', num2str(orientation(i)), char(176)]); % OK?
    pause
end


%% 5c Tuning Curve: Determining the "preference" of the neuron = does the neuron respond differentially to different neurons
figure
h1 = errorbar(orientation,meanSpikeRate, stdSpikeRates,/sqrt(numTrial));
hold on
h2 = plot(orientation, meanSpikeRate)
set(h1, 'color', 'r')
set(h2, 'color', 'k')




%% 5d Curve fitting/ modeling fitting: Do our emperical data correspond to a math function
% This is a platonic enterprise. So far, we have taken the data at face
% calue. The data is the dat.
% In curve fittin, the data represents hints to what the function would
% have looked like in a perfect world. But we go beyond the data.


% Let's see how well a sinusoid fits

figure 
myString = 'p(1) + p(2) * cos(theta - p(3))'; % string that is the function
%p(1): offset which is baseline firing rate
%p(2): Amplitude
%p(3): Phase shift
%P94): would be freauency but it is implied to 1

myFun = inline(myString, 'p', 'theta'); % Theta is the angle
% Determin the parameter s by curve fitting
p = nlinfit(deg2rad(orientation), meanSpikeRate,myFun,[1 1 1]); %Last vector is the initial guesses
yFit = myFun(p,deg2rad(orientation)); % Actual fitting
plot(orientation,meanSpikeRate)
hold on
plot(orientation,yFit,'color','r')


%% Lets try circular gaussian - von mises
figure 
myString2 = 'p(1) * (exp(p(2) * cos(theta-p(3))))/(2 *pi * besseli(0,p(2)))';

myFun2 = inline(myString2, 'p', 'theta'); % Theta is the angle
% Determin the parameter s by curve fitting
p = nlinfit(deg2rad(orientation), meanSpikeRate,myFun2,[1 1 1]); %Last vector is the initial guesses
yFit2 = myFun2(p,deg2rad(orientation)); % Actual fitting
plot(orientation,meanSpikeRate)
hold on
plot(orientation,yFit2,'color','r')


% It looks like the von Mises fit is a reasonable fit for this example
% neuron. If you want to quantify this, nlinefit can return all kinds of
% values, such as residuals, RMSEA, only sratching the surface.
