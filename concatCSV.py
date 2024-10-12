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

@Authors: Austin Wissborn

"""
import os
import pandas as pd
import sys

#Function return two DataFrames, one the concatenated data (combined),
# the other is the concatenated data sorted by parameter "Time"
#The CSV files sourced for concatenation are read from 'location'
def ConcatenateData(location): 
    append_data = []
    cnt = 0

    if os.path.exists('./' + location + '/'):
        for file in os.listdir('./' + location + '/'):    
            if file.endswith('.csv'):  
                cnt +=1
                file_path = os.path.join('./' + location + '/' , file)  
                df = pd.read_csv(file_path)
                append_data.append(df)
        if cnt == 0:
            return None, None
        else:
            cData = pd.concat(append_data)
            return cData.sort_values(by='Time').reset_index(drop = True), cData
    else:
        #print("\nFile location",  path + "\\" + location, "does not exist")
        sys.exit()
        return None, None

# Function used to save concatenated data to csv files.
# 'saveLocation' is the location where the .csv's will be stored
# 'saveFileName' is the file name the .csv's will be stored as
# 'dfData' is the un-sorted dataframe
# 'dfDataI' is the sorted dataframe     
def SaveConcat(saveLocation, saveFileName, dfData, dfDataI):
    if not os.path.exists(saveLocation):
        os.makedirs(saveLocation)

    if saveFileName.endswith('.csv'):
        dfData.to_csv(saveLocation + "\\" + saveFileName, index=False)
    else:
        dfData.to_csv(saveLocation + "\\" + saveFileName + ".csv", index=False)

    if saveFileName.endswith('.csv'):
        dfDataI.to_csv(saveLocation + "\\" + "interlaced_" + saveFileName, index=False)
    else:
        dfDataI.to_csv(saveLocation + "\\" + "interlaced_" + saveFileName + ".csv", index=False)


def concatCSV(readFrom):
    concatDataInter, concatData = ConcatenateData(readFrom)
    return concatDataInter, concatData
    



