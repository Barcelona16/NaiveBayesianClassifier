import os
import random

labels = {}
set1=[]
set2=[]
set3=[]
set4=[]
set5=[]
with open('./trec06c-utf8/label/index') as f:
    lines=f.readlines()
    for line in lines:
        line=line.split('\n')[0]
        label=line.split(' ')[0]
        #print("label is       "+label)
        path = [ line.split(' ')[1].split('/')[2], line.split(' ')[1].split('/')[3] ]      
        path=path[0]+'/'+path[1]
        #print(path)
        labels[path]=label
pathDataCut='./trec06c-utf8/data_cut/'
pathDCdirs=os.listdir(pathDataCut)
for dirs in pathDCdirs:
    curFileNames=pathDataCut+dirs
    files=os.listdir(curFileNames)
    for filesName in files:
        rNumber=random.random()
        path=pathDataCut+dirs+'/'+filesName
        if rNumber>0.8:
            set1.append(path+" "+labels[dirs+'/'+filesName]+'\n')
        elif rNumber>0.6:
            set2.append(path+" "+labels[dirs+'/'+filesName]+'\n')
        elif rNumber>0.4:
            set3.append(path+" "+labels[dirs+'/'+filesName]+'\n')
        elif rNumber>0.2:
            set4.append(path+" "+labels[dirs+'/'+filesName]+'\n')
        else:
            set5.append(path+" "+labels[dirs+'/'+filesName]+'\n')

with open('./dataset/set1','w') as f:
    f.writelines(set1)
with open('./dataset/set2','w') as f:
    f.writelines(set2)
with open('./dataset/set3','w') as f:
    f.writelines(set3)
with open('./dataset/set4','w') as f:
    f.writelines(set4)
with open('./dataset/set5','w') as f:
    f.writelines(set5)




            
            


