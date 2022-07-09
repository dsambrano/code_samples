## This is an example that I extracted from Maedeh's 466 class project. 
# I helped her MLM and here are the notes and code that I wrote for the 
# MLM
library(nlme)
library(lme4)
library(lmerTest)
meddata <- data.frame(ID=factor(longdata$Part.id[1:185]), stim.id=factor(longdata$Stim[1:185]),
                      attract=longdata$Ratings[1:185],eyelash=longdata$Ratings[186:370])



# This will work but doesnt account for the nested Stimuli
# Importantly it shows that you 


# This is a cross classified model !!!!
partial.mod <- lmer(attract ~ eyelash + (1|ID) + (1|stim.id), data = meddata)


# partial.mod <- lmer(correct.key ~ rating + (1|Participant.Name:condition:Week), data = c.data)
summary(partial.mod)

lmerTest::anova(partial.mod) # Optional: , ddf="Kenward-Roger"

