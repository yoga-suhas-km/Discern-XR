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

@Authors: Austin Wissborn and Yoga Suhas Kuruba Manjunath

"""

import os
import config as cfg
from tqdm import tqdm
from search_data import findCsv, SearchAndConcatMultiple
from fvr_packet_segment import load_data_pkt_seg_fvr

flick_flag_1 = 0
flick_flag_2 = 0
   
def Dataset3_exp1_processing(training_method, __type, seg_len, iteration_num):
    keywords = []
    global flick_flag_1 

    data_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(data_path+"\\"+cfg.Processed_data3+"\\"+"exp1") 
    
    total_len = len(cfg.Dataset3_exp1_cfg1)*len(cfg.Dataset3_exp1_cfg2)
    
    if (__type == "train"):
        if flick_flag_1 == 0:
            print("Preparing CSVs for Dataset3 exp1...")
            flick_flag_1 = 1
        else:
            print("Capturing online data for Dataset3 exp1...")
            
        with tqdm(total=100) as pbar:
                for i, cfg1 in enumerate(cfg.Dataset3_exp1_cfg1):
                    for j, cfg2 in enumerate(cfg.Dataset3_exp1_cfg2):
                        keywords.append(cfg1)
                        keywords.append(cfg2)
                    
                        status = findCsv(path,"".join(keywords)+"exp1"+".csv") 
                        if status == 1:
                            keywords.clear()
                            pbar.update(100/total_len) 
                            continue
                    
                        SearchAndConcatMultiple(cfg.Dataset3_path, path, keywords, cfg.Dataset3_exp1_usercfg, cfg.Dataset_exp[0])
                        
                        keywords.clear()
                        pbar.update(100/total_len) 
                        
    return load_data_pkt_seg_fvr(path,cfg.Dataset_exp[0],cfg.Data_list[2],training_method,__type, seg_len, iteration_num)


def Dataset3_exp2_processing(training_method, __type, seg_len, iteration_num):
    keywords = []
    global flick_flag_2
    data_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(data_path+"\\"+cfg.Processed_data3+"\\"+"exp2") 
    
    total_len = len(cfg.Dataset3_exp2_cfg1)
    
    if (__type == "train"):
        if flick_flag_2 == 0:
            print("Preparing CSVs for Dataset3 exp2...")
            flick_flag_2 = 1
        else:
            print("Capturing online data for Dataset3 exp2...")
            
        with tqdm(total=100) as pbar:
            for i, cfg1 in enumerate(cfg.Dataset3_exp2_cfg1):
                keywords.append(cfg1)
                
                status = findCsv(path,"".join(keywords)+"exp2"+".csv")
                if status == 1:
                    keywords.clear()
                    pbar.update(100/total_len) 
                    continue
                
                SearchAndConcatMultiple(cfg.Dataset3_path, path, keywords, cfg.Dataset3_exp2_usercfg, cfg.Dataset_exp[1])
                    
                keywords.clear()
                pbar.update(100/total_len) 
                        

    return load_data_pkt_seg_fvr(path,cfg.Dataset_exp[1],cfg.Data_list[2],training_method,__type, seg_len, iteration_num)
