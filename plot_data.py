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

import sys
import os
import matplotlib.pyplot as plt
import seaborn as sns
import random
import config as cfg
from fvr_packet_segment import slice
import pandas as pd
import numpy as np
from frame_analyzer import FrameAnalyzer



# To plot histogram    
def hist_plot(__data, data_path, exp):
    path, dirs, files = next(os.walk(data_path))

    keywords = []
    req_files = []    
    
    if __data == cfg.Data_list[0]: #****************** configs for Dataset 1
         

        if exp == cfg.Dataset_exp[0]: #************** Files for exp 1
   
            
            for i, cfg_1 in enumerate((cfg.Dataset1_exp1_cfg1)):
                for j, game in enumerate((cfg.Dataset1_exp1_content)):
                    keywords.append(cfg_1)                       
                    keywords.append(game)    
                    file_name = "".join(keywords)+"exp1"+".csv"
                    req_files.append(file_name)
                    keywords.clear()  
 


      
    elif __data == cfg.Data_list[1]:#****************** configs for Dataset 2
        
        if exp == cfg.Dataset_exp[0]: #************** Files for exp 1 

            
            for i, config_t in enumerate((cfg.Dataset2_exp1_cfg1)):
                for j, game in enumerate((cfg.Dataset2_exp1_content)):
                    keywords.append(config_t)
                    keywords.append(game)    
                    file_name = "".join(keywords)+"exp1"+".csv"
                    req_files.append(file_name)
                    keywords.clear()   


    elif __data == cfg.Data_list[2]:#****************** configs for Dataset 3
        
        if exp == cfg.Dataset_exp[0]: #************** Files for exp 1 
            
            for i, cfg1 in enumerate(cfg.Dataset3_exp1_cfg1):
                for j, cfg2 in enumerate(cfg.Dataset3_exp1_cfg2):
                    keywords.append(cfg1)
                    keywords.append(cfg2)
                    file_name = "".join(keywords)+"exp1"+".csv"
                    req_files.append(file_name)
                    keywords.clear()
        
        elif exp == cfg.Dataset_exp[1]: #*************** Files for exp2
        
            for i, cfg1 in enumerate(cfg.Dataset3_exp2_cfg1):
                    
                keywords.append(cfg1)
                file_name = "".join(keywords)+"exp2"+".csv"
                req_files.append(file_name)
                keywords.clear()


    
    for x, file in enumerate(req_files):
        print(file)
            
        df = pd.read_csv(os.path.join(data_path,file))

        df = df.dropna()
        
        

        if __data == cfg.Data_list[0]:#****************** configs for Dataset 1

            if exp == cfg.Dataset_exp[0]:#**************  for exp 1
                df_sp = slice(df, cfg.Dataset1_exp1_N)                    

            
        elif __data == cfg.Data_list[1]:#****************** configs for Dataset 2
            if exp == cfg.Dataset_exp[0]:#**************  for exp 1
                df_sp = slice(df, cfg.Dataset2_exp1_N)
                

        elif __data == cfg.Data_list[2]:#****************** configs for Dataset 3
            if exp == cfg.Dataset_exp[0]:#**************  for exp 1
                df_sp = slice(df, cfg.Dataset3_exp1_N) 
            if exp == cfg.Dataset_exp[1]:#************** for exp 2
                df_sp = slice(df, cfg.Dataset3_exp2_N)                   


        D = []

        frame_data = []
        s = 0 
        s_t = 50

        for i in range(s,s_t): 
            v = []
            v = np.array(v)
            
            if i == 0:
                frame_data = FrameAnalyzer().frame(df_sp[i],1)
            else:
                frame_data = FrameAnalyzer().frame(df_sp[i],0)
            v = np.append(v,frame_data)                 
            D.append(v)

        df_t = pd.DataFrame(D)
        df_t.columns =['fc', 'aiat', 'tfdur'] 



        segment_one_index = 15
        segment_two_index = 40

        fig = plt.figure(dpi=300)

        ax = fig.subplots(3,3)

        ax[0,0].hist(df_sp[segment_one_index]['Length'], bins = 100,edgecolor='darkblue', color='darkred', alpha=.5, density=True)
        ax[0,0].legend(["len"])
        #ax.set_title(file.split(".")[0])
        ax[0,0].set_title("a")

        ax[0,1].hist(df_sp[segment_one_index]['inter-arrival'], bins = 100,edgecolor='darkblue', color='darkred', alpha=.5, density=True)
        ax[0,1].legend(["iat"])
        #ax.set_title(file.split(".")[0])    
        ax[0,1].set_title("b")
        

        ax[0,2].hist(df_sp[segment_one_index]['Dir'], bins = 100,edgecolor='darkblue', color='darkred', alpha=.5, density=True)
        ax[0,2].legend(["dir"])
        #ax.set_title(file.split(".")[0])                        
        ax[0,2].set_title("c")    

        ax[1,0].hist(df_sp[segment_two_index]['Length'], bins = 100,edgecolor='darkblue', color='darkred', alpha=.5, density=True)
        ax[1,0].legend(["len"],)
        #ax.set_title(file.split(".")[0])        
        ax[1,0].set_title("d")


        ax[1,1].hist(df_sp[segment_two_index]['inter-arrival'], bins = 100,edgecolor='darkblue', color='darkred', alpha=.5, density=True)
        ax[1,1].legend(["iat"])
        #ax.set_title(file.split(".")[0])              
        ax[1,1].set_title("e")
        

        ax[1,2].hist(df_sp[segment_two_index]['Dir'], bins = 100,edgecolor='darkblue', color='darkred', alpha=.5, density=True)
        ax[1,2].legend(["dir"])
        #ax.set_title(file.split(".")[0])           
        ax[1,2].set_title("f")       
        
       

        ax[2,0].hist(df_t['fc'], bins = 100,edgecolor='darkblue', color='darkred', alpha=.5, density=True)
        ax[2,0].legend(["fc"])
        ax[2,0].set_title("g")
        
        ax[2,1].hist(df_t['aiat'], bins = 100,edgecolor='darkblue', color='darkred', alpha=.5, density=True)
        ax[2,1].legend(["afiat"])
        ax[2,1].set_title("h")
        
        ax[2,2].hist(df_t['tfdur'], bins = 100,edgecolor='darkblue', color='darkred', alpha=.5, density=True)        
        ax[2,2].legend(["tfdur"])
        ax[2,2].set_title("i")

        
        fig.tight_layout()

        plt.savefig(file.split(".")[0]+'.png')


            
def plot(__data, exp,):

    if __data == cfg.Data_list[0]:
        path = os.path.join(cfg.Processed_data1+'\\'+('exp'+str(cfg.Dataset_exp[0])))
        hist_plot(__data,path, exp) #Dataset 1
    if __data == cfg.Data_list[1]:
        path = os.path.join(cfg.Processed_data2+'\\'+('exp'+str(cfg.Dataset_exp[0])))
        hist_plot(__data,path, exp) #Dataset 2    
    if __data == cfg.Data_list[2]:
        path = os.path.join(cfg.Processed_data3+'\\'+('exp'+str(exp)))
        hist_plot(__data,path, exp) #Dataset 3  
