clc
clear
close all
dets = [24, 23, 29, 22, 24, 26, 26, 24, 23, 28, 21, 22, 32, 17, 30, 23, 25,...
       22, 27, 21, 26, 21, 25, 29, 28, 22, 31, 20, 27, 18, 33, 18, 21, 25,...
       28, 29, 24, 31, 24, 20, 22, 19, 25, 21, 31, 13, 27, 24, 21, 33, 27,...
       15, 27, 31, 33, 27, 29, 25, 32, 33, 24, 15, 21, 23, 23, 22, 34, 23,...
       22, 25, 14, 32, 28, 27, 34, 18, 23, 33, 20, 21, 30, 29, 34, 22, 25,...
       31, 34, 24, 24, 21, 33, 29, 19, 26, 23, 30, 27, 20, 29, 16, 23, 17,...
       23, 23, 33, 22, 25, 20, 26, 26, 32, 17, 22, 25, 20, 18, 20, 24, 27,...
       26, 21, 25, 26, 16, 26, 30, 27, 23, 35, 21, 31, 22, 24, 33, 17, 14,...
       28, 35, 19, 31, 24, 22, 17, 25, 22, 31, 24, 28, 29, 28, 21, 27, 12,...
       28, 23, 26, 31, 29, 19, 37, 24, 30, 23, 22, 21, 31, 34, 25, 24, 22,...
       23, 23, 27, 16, 14, 15, 21, 26, 29, 20, 23, 20, 13, 37, 30, 24, 21,...
       26, 27, 27, 25, 19, 29, 24, 25, 28, 18, 27, 30, 26, 30, 26, 25, 17,...
       32, 24, 14, 28, 19, 31, 20, 23, 19, 25, 33, 28, 22, 23, 27, 28, 28,...
       30, 29, 24, 24, 24, 22, 19, 32, 29, 31, 22, 15, 11, 24, 17, 34, 19,...
       18, 26, 28, 24, 29, 21, 24, 20, 24, 20, 23, 42, 21, 15, 26, 36, 24,...
       29, 22, 22, 27, 30, 22, 16, 19, 25, 28, 29, 20, 36, 29, 33, 28, 30,...
       20, 25, 26, 32, 22, 18, 19, 29, 27, 28, 27, 39, 23, 23, 19, 24, 13,...
       24, 23, 32, 20, 21, 26, 19, 18, 31, 19, 20];



dets1 = [ 1,  9,  6,  6,  1,  4,  5,  8, 10,  8,  3,  2,  4,  4,  3,  8, 12,...
        4,  7,  7,  6,  6,  3, 10,  7,  4,  4,  5,  5,  6,  6,  9,  1,  6,...
       10,  4,  6,  6,  6,  5,  9,  6,  7,  2,  0,  4, 10,  0,  9,  4,  5,...
        5,  4,  8,  2, 10,  4,  3,  5,  3,  3,  5,  5,  5,  9,  9,  6,  6,...
        9,  3,  3,  6,  6,  3,  2,  7,  5,  7, 10,  9,  7,  7,  8,  5,  2,...
        2,  8,  2, 10,  4,  6,  9,  9,  7,  5,  2,  7,  9,  8,  7,  5, 13,...
        2,  6,  9,  7,  7,  5,  3,  5,  7,  7,  6,  6,  7,  5,  5,  6,  6,...
        2,  4,  3,  1,  2,  6,  4,  7,  4,  9,  9,  5,  5,  0,  6,  7,  5,...
        4,  7,  5,  6,  6,  6,  6,  6,  2,  3,  5,  1,  5,  8, 12,  7,  2,...
        6,  6,  4,  3,  9,  3,  8,  8,  7,  0, 11,  7,  5, 10,  3,  2,  5,...
        3,  6,  4,  8,  6,  2,  7,  6,  5,  1,  5,  7,  2,  3,  6,  5,  5,...
        5,  5,  8,  3,  3,  7,  3, 10,  4,  4,  9,  9,  3,  4, 12,  6,  7,...
        7,  6,  1,  5,  8,  6,  1,  6,  7,  7,  7,  7,  3,  7,  5,  0,  5,...
        8,  7,  4,  6,  8,  7,  8,  5,  9,  0,  7,  5,  7,  7,  6, 14,  2,...
        2,  8,  5,  3,  2,  7,  1,  9,  2,  6,  9,  3,  2,  5,  9,  6,  4,...
        7,  7,  6,  2,  8,  9,  6,  6,  6,  5,  6,  5,  3, 11,  9,  5,  7,...
        5,  5,  4,  5,  5,  4,  3,  5,  4,  6,  7,  6,  4,  6,  7,  6, 10,...
        9,  1,  3,  9,  8,  7,  5, 10,  7,  0,  4];


h = histfit(dets);
h(1).FaceColor = 'Yellow';
h(2).Color = [.2 .2 .2];
hold on
H = histfit(dets1);
H(1).FaceColor = 'red';
H(2).Color = 'blue';
legend('Deterministic Scheduler','Normal Curve, \mu = 24.7, \sigma = 5.3','Random Walk Scheduler', 'Normal Curve, \mu = 5.6, \sigma = 2.5', fontsize = 10)
title('Histogram plot for number of Detection', 'Interpreter','latex', FontSize=13)
xlabel('Number of unique planet detections', 'Interpreter','latex',FontSize=13)
ylabel('Frequency of Occurance','Interpreter','latex',FontSize=13)
