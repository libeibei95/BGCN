#!/usr/bin/env python3
# -*- coding: utf-8 -*-

CONFIG = {
    'name': '@your_name',
    'path': '.',
    'log': './log',
    'visual': './visual',
    'gpu_id': "0",
    'note': 'some_note',
    'model': 'BGCN',
    'sample': 'simple',
    #  'sample': 'hard',
    'b_hard_prob': [0.4, 0.4], # = 0.8
    'lrs' : [1e-5, 3e-5, 1e-4, 3e-4, 1e-3, 3e-3],
    'message_dropouts' : [0, 0.1, 0.3, 0.5]     ,
    'node_dropouts' : [0, 0.1, 0.3, 0.5]     , 
    'decays' : [1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2],
    'dataset_name': 'NetEase',
    #  'dataset_name': 'Youshu',
    'mission': 'bundle',
    'conti_train': 'your_model.pth',
    'task': 'tune',
    'eval_task': 'test',
    'epochs': 1000,
    'early': 20,
    'log_interval': 20,
    'test_interval': 1,
    'retry': 1
}

