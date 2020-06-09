#!/usr/bin/python
# -*- coding: UTF-8 -*-

#
import os
import random
dir_datapercent={'trainval_percent':0.9,'train_percent':0.8}
#生成的训练集、验证集、测试集文件夹
dir_dataname={'trainval_file':'trainval.txt','train_file':'train.txt','validation_file':'validation.txt','test_file':'test.txt'}
filepath="/train_txt/"
#读取Annotation文件
Annotation_path='/VOCdevkit/VOC2007/Annotations/'
xml_Annotations=os.listdir(Annotation_path)
total_data=len(xml_Annotations)
list=range(total_data)
trainval_data=random.sample(list,int(dir_datapercent['trainval_percent']*total_data))
train_data=random.sample(list,int(dir_datapercent['train_percent']*total_data*dir_datapercent['trainval_percent']))

#打开数据文件
ftrainval_data=open(os.path.join(filepath,dir_dataname['trainval_file']),'w')
ftrain_data=open(os.path.join(filepath,dir_dataname['train_file']),'w')
fvalidation_data=open(os.path.join(filepath,dir_dataname['validation_file']),'w')
ftset_data=open(os.path.join(filepath,dir_dataname['test_file']),'w')

for i in list:
    image_name=xml_Annotations[i][:-4]+'\n'
    if i in trainval_data:
        ftrainval_data.write(image_name)
        if i in train_data:
            ftrain_data.write(image_name)
        else:
            fvalidation_data.write(image_name)
    else:
        ftset_data.write(image_name)
ftrainval_data.close()
ftrain_data.close()
fvalidation_data.close()
ftset_data.close()




