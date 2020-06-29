# 本人为深度学习初学者，参照github中大神仓库进行复现，可能存在一些问题，如发现问题欢迎留言。
## 本仓库主要依据yolov4的理论，参考https://github.com/qqwweee/keras-yolo3 和https://github.com/Cartucho/mAP进行修改。主要基于tensorflow-keras实现yolov4的训练、mAP的测试(平均类别准确率)
# 具体操作步骤
## 一、训练环境配置
     GTX Geforce GTX 2080Super 
     CUDA==10.0
     CUDNN>=7.4
     tensorflow=gpu==1.10
     keras==2.15
     python-opencv
     matplotlot
安装提醒： 
    对于初学者建议先采用Anaconda来安装Tensorlow-gpu(Anaconda会依据电脑的显卡配置以及自己选定的Tensorflow-gpu的版本自行匹配CUDA和CUDNN)
## 二、数据集下载
     本仓库可以选用VOC2012、VOC2007或者coco2017进行训练来验证
     voc2012和voc2007数据集的下载地址为：
     coco2017数据集得下载地址为：链接：https://pan.baidu.com/s/1xl3XFzyCLBZSl6RjvnTHvg 提取码：68ux   
     voc2012和voc2007数据集格式：    
         |--voc2007      
　　          |--Annotations(存放图片对应的xml)    
　　          |--ImageSets    
　　          |--JPEGImages(存放的图片)    
     coco2017数据集格式:    
          |--coco2017    
　　         |--train2017    
　　         |--val2017    
　　            |--annotations    
　　　　           |--instances_train2017.json    
　　　　           |--instances_val2017.json    
## 三、
