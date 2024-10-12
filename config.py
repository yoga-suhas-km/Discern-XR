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


EARLY_STOPPING = 2
ZERO_ERROR_STOPPING = 2
VALIDATION_DATA_RATIO = 0.4
ERROR_THRESHOLD = 0.02



lbl = {"features":[],"label":[],"class":[]}


#feature_eng = ['packets','time_window']

Data_list=["Dataset1", "Dataset2", "Dataset3"]

training_method = ["Online","Offline"]

Dataset_exp = [1, 2, 3]


#********* Dataset 1 configs ************


Dataset1_path = r"F:\XR_Data\Real Data\Dataset1" #provide the absolute path of dataset1.
Processed_data1 = "Dataset1_pre_processed"


#********** Dataset 1 exp1 **************

Dataset1_exp1_cfg1 =['Cloud']
Dataset1_exp1_content = ['Bigscreen','DiRTRally2.0', 'RealityMixer', 'SolarSystemAR', 'VRChat']

Dataset1_exp1_N = 6000 # size of slice
Dataset1_exp1_online_segments = 12

#********* Dataset 2 configs ************

Dataset2_path = r"F:\XR_Data\Real Data\Dataset2" #provide the absolute path of dataset2.
Processed_data2 = "Dataset2_pre_processed"


#********** Dataset 2 exp1 **************

Dataset2_exp1_cfg1 =['Cloud']
Dataset2_exp1_content = ['BeatSaber', 'SteamVR']


Dataset2_exp1_N = 6000 # size of slice
Dataset2_exp1_online_segments = 14

#********** Dataset 3 congifs ***********#

Dataset3_path = r"F:\XR_Data\Real Data\Dataset3" #provide the absolute path of dataset3.
Processed_data3 = "Dataset3_pre_processed"

# Table of corosponding apps:
#              | group1      | group2
# -----------------------------------------
# fast_traffic | Beast Saber | Medal of Honor
# -----------------------------------------
# slow_traffic | Cooking Sim.| Forklift Sim.

#********** Dataset 3 exp1 **************

Dataset3_exp1_N = 16000 # size of slice
Dataset3_exp1_online_segments = 50 # number of train samples

Dataset3_exp1_cfg1 = ['group1', 'group2'] # Differentiating between the two group. Logical equivilant
Dataset3_exp1_cfg2 = ['slow_traffic', 'fast_traffic'] #Differentiation between each application for each group
Dataset3_exp1_usercfg = ['user11'] #list of users to consider



#********** Dataset 3 exp2 ****************************

Dataset3_exp2_N = 12000 # size of slice
Dataset3_exp2_online_segments = 20 # number of train samples


Dataset3_exp2_cfg1 = ['slow_traffic', 'fast_traffic']
Dataset3_exp2_usercfg = ['user11']







