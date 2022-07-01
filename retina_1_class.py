# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:31:07 2022

@author: nikil
"""
#_base_ = 'C:/Users/nikil/Desktop/Masters/disertation/codes/mmdetection/configs/retinanet/retinanet_r101_caffe_fpn_mstrain_3x_coco.py'
_base_ = 'C:/Users/nikil/Desktop/Masters/disertation/codes/mmdetection/configs/retinanet/retinanet_r50_caffe_fpn_mstrain_1x_coco.py'
# learning policy
model = dict(
    bbox_head=dict(num_classes=3),
    #pretrained='open-mmlab://detectron2/resnet101_caffe',
    backbone=dict(depth=101))
lr_config = dict(step=[28, 34])
#runner = dict(type='EpochBasedRunner', max_epochs=36)
# We also need to change the num_classes in head to match the dataset's annotation
checkpoint_config = dict(interval=5)

# data setting
dataset_type = 'CocoDataset'
data_root = 'data/data_new_1/'
classes = ('_background_', 'other', 'Plastic_Juice_Water_Bottle')
data = dict(
    train=dict(
        img_prefix='data/data_new_1/',
        classes=classes,
        ann_file='data/data_new_1/train_1.json'),
    val=dict(
        img_prefix='data/data_new_1/',
        classes=classes,
        ann_file='data/data_new_1/val_1.json'),
    test=dict(
        img_prefix='data/data_new_1/',
        classes=classes,
        ann_file='data/data_new_1/val_1.json'))

# runtime
load_from = 'retinanet_r101_fpn_mstrain_3x_coco_20210720_214650-7ee888e0.pth'
runner = dict(type='EpochBasedRunner', max_epochs=25)
#workflow = [('train', 5), ('val', 1)]