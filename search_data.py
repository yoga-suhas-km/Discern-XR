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
from concatCSV import concatCSV
from saveCSV import SaveCSV
from extract_raw_features import IsolateData
import pandas as pd

pd.__version__
data_append = []
data_collected = []
data_collected_names = []
data_collected_cnt = 0
    
def FindSubstringFlags(mainString, subStrings):
    flags = [1 if subString in mainString else 0 for subString in subStrings]
    return flags

def exploreDirectoryC(directory, wordList, flag = 0, debug = 0):
    global data_append

    path =  os.path.dirname(os.path.realpath(__file__))
    for item in os.listdir(directory):
        
        item_path = os.path.join(directory, item)
        flags1 = FindSubstringFlags(item_path.split(path, 1)[1], wordList)
        flags2 = FindSubstringFlags(item, wordList)
        
        result = [a | b for a, b in zip(flags2, flags1)]
        if os.path.isdir(item_path):
            exploreDirectoryC(item_path, wordList, 1, debug)
        
        else:
            if(all(x==1 for x in result)):
                if item_path.endswith(".csv"):
                    dataSorted = pd.read_csv(item_path)
                    data_append.append(dataSorted)
                elif not (item_path.endswith(".ini")) and (not (item_path.endswith(".pcapng"))):
                    dataSorted, datax = concatCSV(item_path[item_path.find(path)+ len(path):])
                    data_append.append(dataSorted)
    return data_append
   

def SearchAndConcat(directory, path, wordList, exp, debug = 0):
    x = exploreDirectoryC(directory, wordList, debug)
    dataC = pd.concat(x)
    global data_append
    data_append = []
    SaveCSV(path, ''.join((wordList))+"exp" + str(exp), IsolateData(dataC.sort_values(by=dataC.columns[0]).reset_index(drop = True)))
    return dataC.sort_values(by=dataC.columns[0]).reset_index(drop = True)

def SearchAndConcatMultiple(directory, path, wordListRequired, wordListOneOf, exp, debug = 0):
    data = []
    global data_append
    for i in range(len(wordListOneOf)):
        wordListRequired.append(wordListOneOf[i])
        wordListRequired.pop()
    
    
    for i in range(len(wordListOneOf)):
        wordListRequired.append(wordListOneOf[i])
        x = exploreDirectoryC(directory, wordListRequired)
        data_append = []
        wordListRequired.pop()
        data = pd.concat(x)
        
    for i in range(len(wordListOneOf)):
        wordListRequired.append(wordListOneOf[i])
        wordListRequired.pop()
    dataC = (data)
    SaveCSV(path,''.join((wordListRequired))+"exp" + str(exp), IsolateData(dataC.sort_values(by=dataC.columns[0]).reset_index(drop = True)))  
    data = []        
    return(data_collected)        
                

def findCsv(path, file):
    curPath, dirs, files = next(os.walk(path))
    if file in files:
        return 1
    else:
        return 0


