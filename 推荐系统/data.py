#coding=utf-8
import sklearn
import os
import urllib3
from urllib.request import urlopen

# def downloader_data():
#
#     data_path = 'https://www.kaggle.com/blastchar/telco-customer-churn?select=WA_Fn-UseC_-Telco-Customer-Churn.csv'
#     # urllib3.
#     webpage = urlopen(data_path)
#     data = webpage.read()
#     with open("data.csv",'wb') as code:
#         code.write(data)

class Churn(object):
    def __init__(self):
        self.data_path = "./WA_Fn-UseC_-Telco-Customer-Churn.csv"
        self.train_data = None
        self.val_data = None

    def featrue_transform(self):
        if not os.path.exists("data/new_churn.csv"):
            print("Start Feature Transform ...")
            feature_dict = {"gender":{"Male":1,"Female":0}}


if __name__=='__main__':
    # os.system('ls')




    # downloader_data()