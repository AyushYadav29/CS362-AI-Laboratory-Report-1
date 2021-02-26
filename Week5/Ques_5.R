library(bnlearn)
library(bnclassify)
library(e1071)
library(caret)

mydata<-read.table("C:/Users/ADMIN/Desktop/AI Codes/Week_5/2020_bn_nb_data.txt",head=TRUE)

data1<-mydata
column<-data1$QP


set.seed(2)
random <- sample(2, nrow(data1), prob = c(0.7, 0.3), replace = T)

data_train <- data1[random == 1, ]
data_test <- data1[random == 2, ]


tn <- tan_cl('QP', data_train)
tn<- lp(tn,data_train, smooth =1)
pred_nb_2 <- predict(tn, data_test)
accuracy(pred_nb_2 , data_test $QP)
confusionMatrix(table(pred_nb_2, data_test $QP