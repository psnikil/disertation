# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 15:41:07 2022

@author: nikil
"""


_base_= '/home/s2258567/mmdetection/configs/retinanet/retinanet_x101_64x4d_fpn_mstrain_640-800_3x_coco.py'
model = dict(
    bbox_head=dict(num_classes=6)
    )

# data setting
dataset_type = 'CocoDataset'
data_root = '/home/s2258567/data/'
classes = ('_background_','Plastic_Juice_Water_Bottle', 'Paper_Newspaper', 'Cardboard','Paper_Cardboard_Container','Plastic_Shopping_Bag')
data = dict(
    train=dict(
        img_prefix='train/',
        classes=classes,
        ann_file='train.json'),
    val=dict(
        img_prefix='val/',
        classes=classes,
        ann_file='val.json'),
    test=dict(
        img_prefix='val/',
        classes=classes,
        ann_file='val.json'))

# runtime
#load_from = '/home/s2258567/models/retinanet_r101_fpn_mstrain_3x_coco_20210720_214650-7ee888e0.pth'