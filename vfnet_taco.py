# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 12:17:39 2022

@author: nikil
"""

_base_ = '/home/s2258567/mmdetection/configs/vfnet/vfnet_r101_fpn_mdconv_c3-c5_mstrain_2x_coco.py'
model = dict(
    bbox_head=dict(num_classes=60)
    )

# data setting
dataset_type = 'CocoDataset'
data_root = '/home/s2258567/TACO/'
classes = ('Aluminium foil', 'Battery', 'Aluminium blister pack', 'Carded blister pack', 'Other plastic bottle', 'Clear plastic bottle', 'Glass bottle', 'Plastic bottle cap', 'Metal bottle cap', 'Broken glass', 'Food Can', 'Aerosol', 'Drink can', 'Toilet tube', 'Other carton', 'Egg carton', 'Drink carton', 'Corrugated carton', 'Meal carton', 'Pizza box', 'Paper cup', 'Disposable plastic cup', 'Foam cup', 'Glass cup', 'Other plastic cup', 'Food waste', 'Glass jar', 'Plastic lid', 'Metal lid', 'Other plastic', 'Magazine paper', 'Tissues', 'Wrapping paper', 'Normal paper', 'Paper bag', 'Plastified paper bag', 'Plastic film', 'Six pack rings', 'Garbage bag', 'Other plastic wrapper', 'Single-use carrier bag', 'Polypropylene bag', 'Crisp packet', 'Spread tub', 'Tupperware', 'Disposable food container', 'Foam food container', 'Other plastic container', 'Plastic glooves', 'Plastic utensils', 'Pop tab', 'Rope & strings', 'Scrap metal', 'Shoe', 'Squeezable tube', 'Plastic straw', 'Paper straw', 'Styrofoam piece', 'Unlabeled litter', 'Cigarette')
data = dict(
    train=dict(
        img_prefix='/home/s2258567/TACO/data/',
        classes=classes,
        ann_file='/home/s2258567/TACO/data/train_T.json'),
    val=dict(
        img_prefix='/home/s2258567/TACO/data/',
        classes=classes,
        ann_file='/home/s2258567/TACO/data/val_T.json'),
    test=dict(
        img_prefix='/home/s2258567/TACO/data/',
        classes=classes,
        ann_file='/home/s2258567/TACO/data/val_T.json'))

# runtime
load_from = '/home/s2258567/models/vfnet_r101_fpn_mdconv_c3-c5_mstrain_2x_coco_20201027pth-7729adb5.pth'
workflow = [('train', 1)]