# importing required libraries
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import patches

# read the csv file using read_csv function of pandas
train = pd.read_csv('train.csv')
# print(train.head())

print(train['image_names'].nunique())
print(train['label'].value_counts())
exit()
data = pd.DataFrame()
data['format'] = train['image_names']

for i in range(data.shape[0]):
    data['format'][i] = 'train_images/' + data['format'][i]


for i in range(data.shape[0]):
    data['format'][i] = data['format'][i] + ',' + str(train['xmin'][i]) + ',' + str(train['ymin'][i]) + ',' + str(train['xmax'][i]) + ',' + str(train['ymax'][i]) + ',' + train['label'][i]

data.to_csv('annotate.txt', header=None, index=None, sep=' ')
