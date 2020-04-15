# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:22:26 2018

@author: weixw
"""


import SVMX.SMO as sm

#通过训练数据计算 b, alphas
dataArr,labelArr = sm.loadDataSet('trainingData.txt')
b, alphas = sm.smoP(dataArr, labelArr, 200, 0.0001, 10000, ('rbf', 0.10))
sm.drawDataMap(dataArr,labelArr,b,alphas)
sm.getTrainingDataResult(dataArr, labelArr, b, alphas, 0.10)
dataArr1,labelArr1 = sm.loadDataSet('testData.txt')
#测试结果
sm.getTestDataResult(dataArr1, labelArr1, b, alphas, 0.10)

