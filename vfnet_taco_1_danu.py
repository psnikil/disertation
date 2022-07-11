# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 18:00:53 2022

@author: nikil
"""

_base_ = '/home/s2258567/mmdetection/configs/vfnet/vfnet_x101_64x4d_fpn_mdconv_c3-c5_mstrain_2x_coco.py'
model = dict(
    pretrained = None,
    bbox_head=dict(num_classes=5),
    backbone=dict(init_cfg=dict(type='Pretrained', checkpoint='/home/s2258567/work_dirs/vfnet_taco/latest.pth'))
    )

# data setting
dataset_type = 'CocoDataset'
dataset_type = 'CocoDataset'
data_root = '/home/s2258567/data/'
classes = ('Plastic_Juice_Water_Bottle', 'Paper_Newspaper', 'Cardboard','Paper_Cardboard_Container','Plastic_Shopping_Bag')
data = dict(
   train=dict(
       img_prefix='/home/s2258567/data/train/',
        classes=classes,
        ann_file='/home/s2258567/data/train.json'),
    val=dict(
        img_prefix='/home/s2258567/data/val/',
        classes=classes,
        ann_file='/home/s2258567/data/val.json'),
    test=dict(
        img_prefix='/home/s2258567/data/val/',
        classes=classes,
        ann_file='/home/s2258567/data/val.json'))

# runtime
#load_from = '/home/s2258567/models/vfnet_x101_64x4d_fpn_mdconv_c3-c5_mstrain_2x_coco_20201027pth-b5f6da5e.pth'
workflow = [('train', 1)]