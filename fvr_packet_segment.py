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
import numpy as np
import pandas as pd
import config as cfg
from tqdm import tqdm
from frame_analyzer import FrameAnalyzer

def chunks(nrows, chunk_size):
    return range(1 * chunk_size, (nrows // chunk_size + 1) * chunk_size, chunk_size)

def slice(dfm, chunk_size):
    indices = chunks(dfm.shape[0], chunk_size)
    return np.split(dfm, indices)


def load_data_pkt_seg_fvr(data_path, exp, __data,training_method,__type, seg_len, iteration_num):

    ntk_data = []
    
    path, dirs, files = next(os.walk(data_path))
    
    keywords = []
    req_files = []    
    
    
    if __data == cfg.Data_list[0]: #****************** configs for Dataset 1
    

        if exp == cfg.Dataset_exp[0]: #************** Files for exp 1
            total_len = len(cfg.Dataset1_exp1_cfg1) * len(cfg.Dataset1_exp1_content)      
            
            for i, cfg_1 in enumerate((cfg.Dataset1_exp1_cfg1)):
                for j, game in enumerate((cfg.Dataset1_exp1_content)):
                    keywords.append(cfg_1)                       
                    keywords.append(game)    
                    file_name = "".join(keywords)+"exp1"+".csv"
                    req_files.append(file_name)
                    keywords.clear()


      
    elif __data == cfg.Data_list[1]:#****************** configs for Dataset 2
        
        if exp == cfg.Dataset_exp[0]: #************** Files for exp 1 
            total_len = len(cfg.Dataset2_exp1_cfg1) * len(cfg.Dataset2_exp1_content) 
            
            for i, config_t in enumerate((cfg.Dataset2_exp1_cfg1)):
                for j, game in enumerate((cfg.Dataset2_exp1_content)):
                    keywords.append(config_t)
                    keywords.append(game)    
                    file_name = "".join(keywords)+"exp1"+".csv"
                    req_files.append(file_name)
                    keywords.clear()



    elif __data == cfg.Data_list[2]:#****************** configs for Dataset 3
        
        
        if exp == cfg.Dataset_exp[0]: #************** Files for exp 1
            
            total_len = len(cfg.Dataset3_exp1_cfg1)*len(cfg.Dataset3_exp1_cfg2)

            for i, cfg1 in enumerate(cfg.Dataset3_exp1_cfg1):
                for j, cfg2 in enumerate(cfg.Dataset3_exp1_cfg2):
                    keywords.append(cfg1)
                    keywords.append(cfg2)
                        
                    file_name = "".join(keywords)+"exp1"+".csv"
                    req_files.append(file_name)
                    keywords.clear()
                    
        if exp == cfg.Dataset_exp[1]: #************** Files for exp 2
            
            total_len = len(cfg.Dataset3_exp2_cfg1)
            for i, cfg1 in enumerate(cfg.Dataset3_exp2_cfg1):
                
                keywords.append(cfg1)
                
                        
                file_name = "".join(keywords)+"exp2"+".csv"
                req_files.append(file_name)
                keywords.clear()

    if __type == "train":                 
        print("Frame Vector Representation for train data in progress...")
    elif __type == "test":                 
        print("Frame Vector Representation for test data in progress...")        
        
    with tqdm(total=100) as pbar:
        for x, file in enumerate(req_files):
            D = []
            frame_segment = []
           
            df = pd.read_csv(os.path.join(data_path,file))
            df = df.dropna()
            
            if __data == cfg.Data_list[0]:#****************** configs for Dataset 1

                if exp == cfg.Dataset_exp[0]:#**************  for exp 1
                    df_sp = slice(df, cfg.Dataset1_exp1_N)  
                    seg_length = cfg.Dataset1_exp1_N                     
            
                
            elif __data == cfg.Data_list[1]:#****************** configs for Dataset 2
                
                if exp == cfg.Dataset_exp[0]:#**************  for exp 1
                    df_sp = slice(df, cfg.Dataset2_exp1_N)
                    seg_length = cfg.Dataset2_exp1_N

            elif __data == cfg.Data_list[2]:#****************** configs for Dataset 3

                if exp == cfg.Dataset_exp[0]:#**************  for exp 1
                    df_sp = slice(df, cfg.Dataset3_exp1_N)
                    seg_length = cfg.Dataset3_exp1_N
                elif exp == cfg.Dataset_exp[1]:#**************  for exp 2
                    df_sp = slice(df, cfg.Dataset3_exp2_N) 
                    seg_length = cfg.Dataset3_exp2_N

                    
            
            if __type == "train":
                s = iteration_num*seg_len # start index, zero by deafult 
                s_t = s + seg_len                
            elif __type == "test":
                s = iteration_num*seg_len
                s_t = len(df_sp)
                               


            for i in range(s,s_t):    
                v = []
                up_dn = []
                flow_dur = []
                frame_data = []
                
                if len(df_sp[i]) == seg_length:
                    for j in  range(0, (df_sp[i].shape[1])):                    
                         if j ==0:
                            offset = df_sp[i].iloc[1,0]
                            l = abs(df_sp[i].iloc[:,0] - offset)
                            flow_dur = sum(l)
                         elif j == 1 or j == 2:
                            #df_f =(df_sp[i].iloc[:,j].agg(['min','max', 'mean','std']))
                            df_f =(df_sp[i].iloc[:,j].agg(['max','mean','var','std']))
                            v.append(np.array(df_f))
                         elif j == 3:
                            #up = np.array(df_sp[i].iloc[:,3].value_counts())
                            up_dn = np.array(df_sp[i].iloc[:,3].sum()) ######## this was giving good results.
                            
                    v = np.array(v)
                    v = v.reshape(v.shape[0]*v.shape[1])
                    flow_dur = np.array(flow_dur)            
                    v = np.append(v,up_dn)
                    v = np.append(v,flow_dur)
                    if i == 0:
                        frame_data = FrameAnalyzer().frame(df_sp[i],1)
                    else:
                        frame_data = FrameAnalyzer().frame(df_sp[i],0)
                    v = np.append(v,frame_data)                 
                    D.append(v)

            df_t = pd.DataFrame(D)

            df_t["label"] = x
            df_t["class"] = file.split(".")[0]   
            cfg.lbl["label"].append(file.split(".")[0])
            cfg.lbl["class"].append(x)
            
            ntk_data.append(df_t)
            pbar.update(100/total_len)    


    ntk_data_label = pd.concat(ntk_data,axis=0, sort=False, ignore_index=True)
    ntk_data_label = ntk_data_label.replace(to_replace = np.nan, value = 0)
    ntk_data_label.columns =['max_length','mean_length','var_length','std_length','max_iat','mean_iat','var_iat','std_iat', 'up/dn', 'time', 'frame_count', 'avg_frame_iat', 'total_frame_duration','label','class'] 
    ntk_data_label = ntk_data_label.drop(columns= ['class'])
 

    X = (ntk_data_label.iloc[:,ntk_data_label.columns !="label"])
    X = np.array(X)
    y = np.array(ntk_data_label["label"]) 

    ntk_data_label = ntk_data_label.drop(columns= ['label'])
    cfg.lbl["features"] = list(ntk_data_label.columns)

    return X,y
