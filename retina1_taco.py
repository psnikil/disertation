# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 20:50:06 2022

@author: nikil
"""

_base_ = 'C:/Users/nikil/Desktop/Masters/disertation/codes/mmdetection/configs/retinanet/retinanet_r50_caffe_fpn_mstrain_1x_coco.py'
# learning policy
model = dict(
    bbox_head=dict(num_classes=60),
    #pretrained='open-mmlab://detectron2/resnet101_caffe',
    backbone=dict(depth=101))
lr_config = dict(step=[28, 34])
#runner = dict(type='EpochBasedRunner', max_epochs=36)
# We also need to change the num_classes in head to match the dataset's annotation
checkpoint_config = dict(interval=5)

# data setting
dataset_type = 'CocoDataset'
data_root = 'data/taco/'
classes = ('Aluminium foil', 'Battery', 'Aluminium blister pack', 'Carded blister pack', 'Other plastic bottle', 'Clear plastic bottle', 'Glass bottle', 'Plastic bottle cap', 'Metal bottle cap', 'Broken glass', 'Food Can', 'Aerosol', 'Drink can', 'Toilet tube', 'Other carton', 'Egg carton', 'Drink carton', 'Corrugated carton', 'Meal carton', 'Pizza box', 'Paper cup', 'Disposable plastic cup', 'Foam cup', 'Glass cup', 'Other plastic cup', 'Food waste', 'Glass jar', 'Plastic lid', 'Metal lid', 'Other plastic', 'Magazine paper', 'Tissues', 'Wrapping paper', 'Normal paper', 'Paper bag', 'Plastified paper bag', 'Plastic film', 'Six pack rings', 'Garbage bag', 'Other plastic wrapper', 'Single-use carrier bag', 'Polypropylene bag', 'Crisp packet', 'Spread tub', 'Tupperware', 'Disposable food container', 'Foam food container', 'Other plastic container', 'Plastic glooves', 'Plastic utensils', 'Pop tab', 'Rope & strings', 'Scrap metal', 'Shoe', 'Squeezable tube', 'Plastic straw', 'Paper straw', 'Styrofoam piece', 'Unlabeled litter', 'Cigarette')
data = dict(
    train=dict(
        img_prefix='data/taco/',
        classes=classes,
        ann_file='data/taco/annotations_1.json'),
    val=dict(
        img_prefix='data/taco/',
        classes=classes,
        ann_file='data/taco/val_2.json'),
    test=dict(
        img_prefix='data/taco/',
        classes=classes,
        ann_file='data/taco/val_2.json'))

# runtime
load_from = 'retinanet_r101_fpn_mstrain_3x_coco_20210720_214650-7ee888e0.pth'
runner = dict(type='EpochBasedRunner', max_epochs=25)
#workflow = [('train', 5), ('val', 1)]