clc
clear
close all
detRand1200 = cell2mat(struct2cell(load('ObsData1200Rand.mat'))); 
det_300 = cell2mat(struct2cell(load("ObsData300Scheduler.mat")));
detRand900 = cell2mat(struct2cell(load('ObsData900Rand.mat')));
det300_3Y = cell2mat(struct2cell(load('ObsData300Scheduler3Y.mat')));
figure()
ax = gca;
de = histfit(detRand1200);
legend('Deterministic Scheduler for 5Y mission','Normal Curve, \mu = 13.4, \sigma = 3.5', fontsize = 15)
title('Histogram plot for number of Detection', 'Interpreter','latex', FontSize=15,FontWeight = 'bold')
xlabel('Number of unique planet detections', 'Interpreter','latex',FontSize=15,FontWeight = 'bold')
ylabel('Frequency of Occurance','Interpreter','latex',FontSize=15,FontWeight = 'bold')
ax.FontSize = 14;
hold on 
histfit(detRand900,5)