"""
MIT License

Copyright (c) 2024 Yoga Suhas Kuruba Manjunath

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

@Authors: Yoga Suhas Kuruba Manjunath and Austin Wissborn

"""

import os
import pandas as pd
import random
import config as cfg
from dataset3_pre_processing import Dataset3_exp1_processing, Dataset3_exp2_processing
from dataset2_pre_processing import Dataset2_exp1_processing
from dataset1_pre_processing import Dataset_exp1_processing


random.seed(10)

def get_classes():
        return cfg.lbl
 
# call to get the dataset for train or test    
def get_dataset(__data, training_method , exp, __type, seg_len, iteration_num):
    cfg.lbl["label"].clear()
    cfg.lbl["class"].clear()

    if __data == cfg.Data_list[0]: #****************** for Dataset 1
        if not os.path.exists(cfg.Processed_data1):
            os.mkdir(cfg.Processed_data1) 
        
        
        if exp == cfg.Dataset_exp[0]: #****************** for Dataset 1 exp1
            curPath, dirs, files = next(os.walk(cfg.Processed_data1))
            
            if not ('exp'+str(cfg.Dataset_exp[0])) in dirs:
                os.mkdir(os.path.join(cfg.Processed_data1+'\\'+('exp'+str(cfg.Dataset_exp[0])))) 
            
            return Dataset_exp1_processing(training_method, __type, seg_len, iteration_num)            


    
    if __data == cfg.Data_list[1]: #****************** for Dataset 2
        if not os.path.exists(cfg.Processed_data2):
            os.mkdir(cfg.Processed_data2) 
      
        
        if exp == cfg.Dataset_exp[0]: #****************** for Dataset 2 exp1
            curPath, dirs, files = next(os.walk(cfg.Processed_data2)) 
            
            if not ('exp'+str(cfg.Dataset_exp[0])) in dirs: 
                os.mkdir(os.path.join(cfg.Processed_data2+'\\'+('exp'+str(cfg.Dataset_exp[0])))) 
            return Dataset2_exp1_processing(training_method, __type, seg_len, iteration_num) 
 


    if __data == cfg.Data_list[2]: #****************** for Dataset 3
        if not os.path.exists(cfg.Processed_data3): 
            os.mkdir(cfg.Processed_data3) 
       
        
        if exp == cfg.Dataset_exp[0]: #****************** for Dataset 3 exp1
            curPath, dirs, files = next(os.walk(cfg.Processed_data3)) 
            if not ('exp'+str(cfg.Dataset_exp[0])) in dirs: 
                os.mkdir(os.path.join(cfg.Processed_data3+'\\'+('exp'+str(cfg.Dataset_exp[0])))) 
            return Dataset3_exp1_processing(training_method, __type, seg_len, iteration_num) 
        
        if exp == cfg.Dataset_exp[1]: #****************** for Dataset 3 exp2
            curPath, dirs, files = next(os.walk(cfg.Processed_data3)) 
            if not ('exp'+str(cfg.Dataset_exp[1])) in dirs: 
                os.mkdir(os.path.join(cfg.Processed_data3+'\\'+('exp'+str(cfg.Dataset_exp[1])))) 
            return Dataset3_exp2_processing(training_method, __type, seg_len, iteration_num) 

            
       
     
