setwd('D:/Projects/PlaygroundSeries Season 3, Episode 13/Data')

library(tidyverse)

train <- read.csv('train.csv')

train$prognosis <- as_factor(train$prognosis)

summary(train)

train %>% gather()
ggplot(gather(train),aes(value,stat="count")) + geom_bar() + facet_wrap(~key,scales='free_x')

ggplot(train,aes(x=prognosis,stat='count',group = abdominal_pain)) + geom_bar(aes(fill=abdominal_pain),position = 'stack')
