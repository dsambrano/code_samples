% This Script will focus on data analysis, real data that instructor
% recorded
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





%%Init 0
clear all 
close all
clc


% Import ToolBoxes/Functions


% Constants


%% 1) Loader - Either section or program if big

% a) Get data with excel from other source
M1 = xlsread('data/MATRIX1.xls');
M2 = xlsread('data/MATRIX2.xls');
M3 = xlsread('data/MATRIX3.xls');

% b) when you already have it in mat file
load data/M1.mat
load data/M2.mat
load data/M3.mat


%% 2) "Thalamus the data: pruning of missing data

% There is a fundamental problem not everyone saw all three movies
% There is missing data. Is this missing data  likely to missing randomly
% Missing data is likely missing systematically. We need to make a choice,
% how to remove missing data. 


% 2a) There are several options: element wise
% Easiest, but probably the most limited in turns of conclusion
% Find missing values and delete them. Problems: uneven number of remaining
% participants. This sets you up for independent analysis downstream. This
% might bias the results, if only fans so the last one due to experimental
% mortality, this method would inflate relative quality of 3rd. 

% Element-wise removal:
% See how big of a problem this is count missing values per movie:
%This will limit the conclusions you can draw. Sets up for independent
%sample analysis
sum(isnan(M1)) % Counts missing values
validM1 = M1(isnan(M1) ==0);
sum(isnan(M2)) % Counts missing values
validM2 = M2(isnan(M2) ==0);
sum(isnan(M3)) % Counts missing values
validM3 = M3(isnan(M3) ==0);
% As expected there is experimental mortality.


% 2c: Imputation. basically guessing - on the bassis of the available data
% - but it holds a lot of assumptions. So in practice imputation,
% imputationis more commonly used in industry and engineering. And there
% are many ways of making these guesses



%% 3 Formatting

% Unlike in the neural data there isnt much to do becauase its pre
% formatted. 


%% 4) Analysisd
%a) descriptive

MEANS = [mean(validM1) mean(validM2) mean(validM3)];
STDs = [std(validM1) std(validM2) std(validM3)];
Ns = [length(validM1) length(validM2) length(validM3)];
SEMS = [STDs(1)./sqrt(Ns(1)) STDs(2)./sqrt(Ns(2)) STDs(3)./sqrt(Ns(3))];


%b) Inferential statistics: Ttest
% 1 vs 2
[sig12, p12, CI12, params12] = ttest2(validM1,validM2, 'alpha', .001) %Independent Samples
% 1 vs 3
[sig13, p13, CI13, params13] = ttest2(validM1,validM3, 'alpha', .01) %Independent Samples
% 2 vs 3
[sig23, p23, CI23, params23] = ttest2(validM2,validM3, 'alpha', .05) %Independent Samples


% ANOVA: 1 factor with 3 levels: so one factor anova
% since unbalanced need a grouping vector
G1 = ones(Ns(1),1);
G2 = ones(Ns(2),1).*2;
G3 = ones(Ns(3),1).*3;
G = [G1;G2;G3];
V = [validM1; validM2; validM3];
[p, antab, stats] = anova1(V, G)



% this is all nice, but we did the wrong test: Its not on an interval scale
% What are the right tests? Ordinal versions of ttest and ANOVA


% TTest: Mann-whitney-wilcox test
% 1 vs 2
[Up12, Usig12, Uparams12] = ranksum(validM1,validM2, 'alpha', .001) %Man whitney-wilcox
% 1 vs 3
[Up13, Usig13, Uparams13] = ranksum(validM1,validM3, 'alpha', .01) %Man whitney-wilcox
% 2 vs 3
[Up23, Usig23, Uparams23] = ranksum(validM2,validM3, 'alpha', .05) %Man whitney-wilcox



% ANOVA: kruskal Wallis
[Hp, Hantab, Hstats] = kruskalwallis(V, G)



%% Listwise: Row wise  deletion
% Idea: We keep only people who ahve seen all 3 
% Lose a lot of data/power
% Upside: clean, within subjects analysis
RATINGS = [M1 M2 M3];

for i = 1:3
    killset = find(isnan(RATINGS(:,i))==1);
    RATINGS(killset,:) = []; % Elemenate people that didnt see the first one
end
% We lost 2/3rd of the dataset, but everyone who is left saw all three


%% 3) Formatting
 % WE dont have one

%% 4) Analysis
%a) descriptive

MEANS = mean(RATINGS);
STDs = std(RATINGS);
N = length(RATINGS);
SEMS = [STDs(1)./sqrt(N) STDs(2)./sqrt(N) STDs(3)./sqrt(N)];
% We see that the other analsyis was hiding the true conclusions, we need
% to ask for comparative judgment if they experience alternatives. More
% appropriate.


%b) Inferential statistics: Ttest for paired samples
% 1 vs 2
[sig12, p12, CI12, params12] = ttest(RATINGS(:,1),RATINGS(:,2), 'alpha', .001) %Dependent Samples
% 1 vs 3
[sig13, p13, CI13, params13] = ttest(RATINGS(:,1),RATINGS(:,3), 'alpha', .01) %Dependent Samples
% 2 vs 3
[sig23, p23, CI23, params23] = ttest(RATINGS(:,2),RATINGS(:,3), 'alpha', .05) %Dependent Samples

% Despite losing a lot of power, since we lost most of the sample, our
% power increase because the pairwise ttest is inherently more powerful
% because you are your own control. Useful for movies in particular.



% In the interest of time we skip all the others and jump straight to
% Except for the K

% ANOVA: kruskal Wallis
[Hp, Hantab, Hstats] = kruskalwallis(RATINGS)
[Hp, Hantab, Hstats] = friedman(RATINGS)

% Now that we have the same number of people we can do correlation
% Is it the same people that liked the movies

[r,p] = corrcoef(RATINGS)








