# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 03:02:57 2022

@author: nikil
"""

_base_ = 'C:/Users/nikil/Desktop/Masters/disertation/codes/mmdetection/configs/vfnet/vfnet_r101_fpn_mdconv_c3-c5_mstrain_2x_coco.py'
model = dict(
    bbox_head=dict(num_classes=6)
    )

# data setting
dataset_type = 'CocoDataset'
data_root = 'data/data/'
classes = ('_background_','Plastic_Juice_Water_Bottle', 'Paper_Newspaper', 'Cardboard','Paper_Cardboard_Container','Plastic_Shopping_Bag')
data = dict(
    train=dict(
        img_prefix='data/data/train/',
        classes=classes,
        ann_file='data/train.json'),
    val=dict(
        img_prefix='data/data/val/',
        classes=classes,
        ann_file='data/val.json'),
    test=dict(
        img_prefix='data/data/val/',
        classes=classes,
        ann_file='data/val.json'))

# runtime
load_from = 'vfnet_r101_fpn_mdconv_c3-c5_mstrain_2x_coco_20201027pth-7729adb5.pth'
workflow = [('train', 1)]