# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 15:41:07 2022

@author: nikil
"""


_base_= '/home/s2258567/mmdetection/configs/retinanet/retinanet_r101_fpn_mstrain_640-800_3x_coco.py'
model = dict(
    pretrained = None,
    bbox_head=dict(num_classes=5),
    backbone=dict(init_cfg=dict(type='Pretrained', checkpoint='/home/s2258567/models/retinanet_r101_fpn_mstrain_3x_coco_20210720_214650-7ee888e0.pth'))
    )
checkpoint_config = dict(interval=5)
loss_cls=dict(
    type='FocalLoss',
    use_sigmoid=True,
    gamma=2,
    alpha=0.25,
    loss_weight=1.0)
# data setting
dataset_type = 'CocoDataset'
data_root = '/home/s2258567/data/'
classes = ('Plastic_Juice_Water_Bottle', 'Paper_Newspaper', 'Cardboard','Paper_Cardboard_Container','Plastic_Shopping_Bag')
data = dict(
    train=dict(
        dataset=dict(
            img_prefix='/home/s2258567/data/train/',
            classes=classes,
            ann_file='/home/s2258567/data/train.json')),
    val=dict(
        img_prefix='/home/s2258567/data/val/',
        classes=classes,
        ann_file='/home/s2258567/data/val.json'),
    test=dict(
        img_prefix='/home/s2258567/data/val/',
        classes=classes,
        ann_file='/home/s2258567/data/val.json'))

# runtime
runner = dict(type='EpochBasedRunner', max_epochs=25)
#load_from = 'models/retinanet_r101_fpn_mstrain_3x_coco_20210720_214650-7ee888e0.pth'