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


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sn
from functools import reduce
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report,confusion_matrix
from process_data import get_dataset, get_classes
from plot_data import plot
import numpy as np
import pandas as pd
import joblib
import sys
import os
import config


import warnings
warnings.filterwarnings("ignore")

classifiers = []
called = []

def eva_clf(y_true, y_pred_t, flag, mode):

    accuracy = accuracy_score(y_true, y_pred_t)
    if mode == "test":
        
        if flag != -1:
            print("\n******\nPerformance Metrics on Validation Data\n******\n")
        elif flag == -1:
            print("\n******\nPerformance Metrics on Test Data\n******\n")
        
        precision = precision_score(y_true, y_pred_t, average='weighted',labels=np.unique(y_pred_t))
        recall = recall_score(y_true, y_pred_t,average='weighted')
        f1 = f1_score(y_true, y_pred_t, average='weighted',labels=np.unique(y_pred_t))

        print('Accuracy: %f' % accuracy)
        print('Precision: %f' % precision)
        print('Recall: %f' % recall)
        print('F1 score: %f' % f1)
        
        print('classification report')
        print(classification_report(y_true, y_pred_t,labels=np.unique(y_pred_t)))
        
        print('confusion matrix')
        
        cf = confusion_matrix(y_true, y_pred_t)
        print((cf))
        
        FP = cf.sum(axis=0) - np.diag(cf)  
        FN = cf.sum(axis=1) - np.diag(cf)
        TP = np.diag(cf)
        TN = cf.sum() - (FP + FN + TP)

        # Sensitivity, hit rate, recall, or true positive rate
        TPR = TP/(TP+FN)
        print("True Positive rate",TPR)
        # Specificity or true negative rate
        TNR = TN/(TN+FP) 
        print("True negative rate",TNR)
        
        # Precision or positive predictive value
        PPV = TP/(TP+FP)
        print("positive predictive value",PPV)
        
        # Negative predictive value
        NPV = TN/(TN+FN)
        print("Negative predictive value",NPV) 
        
        # Fall out or false positive rate
        FPR = FP/(FP+TN)
        print("false positive rate",FPR) 
        
        # False negative rate
        FNR = FN/(TP+FN)
        print("false negative rate",FNR) 
        
        # False discovery rate
        FDR = FP/(TP+FP)
        print("false discovery rate",FDR)     

        # Overall accuracy
        ACC = (TP+TN)/(TP+FP+FN+TN)
        print("Accuracy",ACC)

    if flag == -1:
        lbl = get_classes()    
        cf = confusion_matrix(y_true, y_pred_t, normalize='true')
        df_cm = pd.DataFrame(cf, index = [i for i in lbl["label"]],
                      columns = [i for i in lbl["label"]])

        plt.figure(figsize = (10,7))
        sn.set(font_scale=2) # for label size
        sn.heatmap(df_cm, annot=True, annot_kws={"size": 20})
        
        plt.tight_layout()
        plt.savefig("confusion_matrix_"+called+'.png')

    return accuracy
    
def model(X, y, flag):
    
    if flag == 0:
        clf = RandomForestClassifier(n_estimators=(50), random_state=0, warm_start=True)
    elif flag != -1 and flag != 0:
        clf = RandomForestClassifier(n_estimators=(50*flag), random_state=0)
    elif flag == -1:
        clf = RandomForestClassifier(n_estimators=(50), random_state=0)
    clf.fit(X, y)  
    
    if flag == -1:
        importances = clf.feature_importances_

        features = get_classes() 
        print("\n******\nFeature Importance\n******\n")


        for i, feature in enumerate ((features["features"])):
          print(feature,':',importances[i],'\n')     
          
        feat_importances = pd.Series(clf.feature_importances_, index=features["features"])
        feat_importances.nlargest(20).plot(kind='barh')
        plt.tight_layout()
        plt.savefig("feature_importance_"+ called +'.png')

        
    return clf
    
def combine_rfs(rf_a, rf_b):
    rf_a.estimators_ += rf_b.estimators_
    rf_a.n_estimators = len(rf_a.estimators_)
    return rf_a    
    
def test(X_test, y_test, test_flag):
    if test_flag != -1:
        clf = reduce(combine_rfs, classifiers)
    else:
        clf = joblib.load("./random_forest.joblib")
        
    y_pred_t = clf.predict(X_test)    
 
    accuracy = eva_clf( y_test, y_pred_t, test_flag, "test") 
    return accuracy
    
def start(__data, training_method, exp,__type, segment_num=0):
  
            
    if training_method == config.training_method[0]:

        if __data == config.Data_list[0] and exp == config.Dataset_exp[0]:
            segments = config.Dataset1_exp1_online_segments
        elif __data == config.Data_list[0] and exp == config.Dataset_exp[1]:
            segments = config.Dataset1_exp2_online_segments
        elif __data == config.Data_list[0] and exp == config.Dataset_exp[2]:
            segments = config.Dataset1_exp3_online_segments
        elif __data == config.Data_list[1] and exp == config.Dataset_exp[0]:
            segments = config.Dataset2_exp1_online_segments        
        elif __data == config.Data_list[1] and exp == config.Dataset_exp[1]:
            segments = config.Dataset2_exp2_online_segments   
        elif __data == config.Data_list[2] and exp == config.Dataset_exp[0]:
            segments = config.Dataset3_exp1_online_segments    
        elif __data == config.Data_list[2] and exp == config.Dataset_exp[1]:
            segments = config.Dataset3_exp2_online_segments    
        elif __data == config.Data_list[2] and exp == config.Dataset_exp[2]:
            segments = config.Dataset3_exp3_online_segments             
    
        if __type == "train":

                
            early_stop = 0
            zero_error = 0
            prev_accuracy = 0
            prev_error = 0
            
            X_C = []
            X_C_l = []
            y_C = []
           
            if os.path.exists("./random_forest.joblib"):
                os.remove("./random_forest.joblib")
                
                   
            X, y = get_dataset(__data, training_method, exp,__type, segments, segment_num)
            
            X_C = np.array(X_C)
            y_C = np.array(y_C)
            X_C = np.append(X_C, X)
            X_C = X_C.reshape(X.shape[0],X.shape[1])
            
            X_C_l.append(X_C)
            y_C = np.append(y_C,y)

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = config.VALIDATION_DATA_RATIO)
            
            rf = model(X_train, y_train, segment_num)
            #print("\n******\n main_aar:model saved for segment number:", segment_num )
            classifiers.append(rf)

            current_accuracy = test(X_test, y_test, segment_num)
            prev_error = 1 - prev_accuracy
            current_error = 1 - current_accuracy

            print("\n******\n prev_error:", round(abs(prev_error),3), "current_error:", round(abs(current_error),3), "error_change:", round(abs(current_error-prev_error),3), "Segment_num:", segment_num, "\n******\n")
            
            while early_stop < config.EARLY_STOPPING and zero_error < config.ZERO_ERROR_STOPPING:
                
                X_t = []
                X_t = np.array(X_t)
                prev_error = current_error
                segment_num += 1 
                X, y = get_dataset(__data, training_method, exp,__type, segments, segment_num)
                
                X_t = np.append(X_t, X)
                X_t = X_t.reshape(X.shape[0],X.shape[1])
                
                X_C_l.append(X_t)
                y_C = np.append(y_C,y)
   
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = config.VALIDATION_DATA_RATIO)
                rf = model(X_train, y_train, segment_num)
                

                classifiers.append(rf)
                current_accuracy = test(X_test, y_test, segment_num)
                current_error = 1 - current_accuracy
                if current_error == 0:
                    zero_error += 1
                
                if (round(abs(current_error-prev_error),3) <= config.ERROR_THRESHOLD):
                    early_stop += 1
                
                print("\n******\nprev_error:", round(abs(prev_error),3), "current_error:", round(abs(current_error),3), "error_change:", round(abs(current_error-prev_error),3), "Segment_num:", segment_num, "\n******\n")
                

            X_C_l = np.array(X_C_l)
            X_C_l = X_C_l.reshape(X_C_l.shape[0]*X_C_l.shape[1], X_C_l.shape[2])
            X_C_l = list(X_C_l)
            X_C_l = pd.DataFrame(X_C_l)
            y_C = pd.DataFrame(y_C)

            print("\n******\nFinal model is saved for segment number:", segment_num )
            print("******\n")
            rf = model(np.array(X_C_l), np.array(y_C), -1)
            classifiers.append(rf)
            
            return(segment_num)
                
        elif __type == "test":
            X_test, y_test = get_dataset(__data, training_method, exp,__type, segments, segment_num)
            test(X_test, y_test, -1)      
       

def print_notice():
    print("Master please give me a correct command")
    print(" eg:") 
    print("     python main_aar.py Dataset1")
    print("     python main_aar.py Dataset2")
    print("     pyhton main_aar.py Dataset3 exp=1")
    print("     pyhton main_aar.py Dataset3 exp=2")

    print("     python main_aar.py plot Dataset1")
    print("     python main_aar.py plot Dataset2")
    print("     python main_aar.py plot Dataset3 exp=1")
    print("     python main_aar.py plot Dataset3 exp=2")
    



def main(argv):
    global called
    
    if (len(argv) == 0 ):
        print_notice()
        sys.exit()      
    elif (len(argv) >= 3):
        if ((argv[0] != "plot")):
            print_notice()
            sys.exit()        
    elif (len(argv) == 1): 
        if ((argv[0] not in config.Data_list) and (argv[0]) != "Dataset3"):
            print_notice()
            sys.exit()
            
    if (argv[0] == config.Data_list[0]): #Dataset1
        
        exp = 1
        start_segment = 0
        called = "Dataset1_exp{}".format(exp)
     
        start_segment = start(config.Data_list[0], "Online", exp, "train", start_segment)
        start_segment += 1
        clf = reduce(combine_rfs, classifiers)
        joblib.dump(clf, "./random_forest.joblib") 

        start(config.Data_list[0], "Online", exp, "test", start_segment)
 
    elif argv[0] == config.Data_list[1]: #Dataset2
        start_segment = 0
        exp = 1
        called = "Dataset2_exp{}".format(exp)
        start_segment = start(config.Data_list[1], "Online", exp, "train", start_segment)
        start_segment += 1
        clf = reduce(combine_rfs, classifiers)
        joblib.dump(clf, "./random_forest.joblib")         
        start(config.Data_list[1], "Online", exp, "test", start_segment)      
        

    elif argv[0] == config.Data_list[2]: #Dataset3
        if len(argv) != 2:
            print_notice()  
            sys.exit()
        start_segment = 0
        exp = argv[1].split('=')
        called = "Dataset3_exp{}".format(exp)
        start_segment = start(config.Data_list[2], "Online", int(exp[1]), "train", start_segment)
        start_segment += 1        
        clf = reduce(combine_rfs, classifiers)
        joblib.dump(clf, "./random_forest.joblib")         
        start(config.Data_list[2], "Online", int(exp[1]), "test", start_segment)               
            

    if argv[0] == "plot" and argv[1] == config.Data_list[0]:   #Plot command for Dataset1 
        exp =1
        plot(config.Data_list[0], exp)
        
    elif argv[0] == "plot" and argv[1] == config.Data_list[1]: #Plot command for Dataset2      
        exp = 1        
        plot(config.Data_list[1], exp)      
        
    elif argv[0] == "plot" and argv[1] == config.Data_list[2]: #Plot command for Dataset3      
        exp = argv[2].split('=')        
        plot(config.Data_list[2], int(exp[1])) 

if __name__ == "__main__":
    main(sys.argv[1:]) 

