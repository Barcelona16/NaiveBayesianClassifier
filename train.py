import os
import re
import random
import json
import math

def loadSet(setName): #加载之前划分好的set
    with open('./dataset/'+setName) as f:
        lines=f.readlines()
        data=[]
        for line in lines:
            data.append((line.split('\n')[0].split(' ')[0], line.split('\n')[0].split(' ')[1]))
        #print(len(data))
    return data 

def train(sample,laplace): #训练并且计算准确值
    toAC=0
    for i in range(1,6):
        trainSet=[]
        testSet=[]
        labelWords={}
        print("testSet is set"+str(i))
        for j in range(1,6):
            #print("load set"+str(j))
            if i != j and sample>random.random():
                trainSet+=loadSet('set'+str(j))
            elif i==j:
                testSet=loadSet('set'+str(j))
        print("trainSet len is "+str(len(trainSet))) 
        for line in trainSet:
            path=line[0]
            label=line[1]
            #print(path+" "+label) 
            if not label in labelWords.keys():
                labelWords[label]={}  
            with open(path,encoding='utf-8') as f:
                mailText=f.read()
                regex=u'[\u4E00-\u9FA5]+'
                pattern=re.compile(regex)
                words=re.findall(pattern,mailText)
                regex=u'http'
                pattern=re.compile(regex)
                words+=re.findall(pattern,mailText)
            for charc in words:
                if not charc in labelWords[label].keys():
                    labelWords[label][charc]=1
                else:
                    labelWords[label][charc]+=1
        toNumber=len(testSet)
        trueLabel=0
        bestAC=0
        for line in testSet:
            path=line[0]
            ans=line[1]
            label=''
            prob=-math.inf
            for curLabel in labelWords.keys():
                curProb=math.log(float(len(labelWords[curLabel]))/float(toNumber))
                with open(path,encoding='utf-8') as f:
                    mailText=f.read()
                    regex=u'[\u4E00-\u9FA5]+'
                    pattern =re.compile(regex)
                    words=re.findall(pattern,mailText)
                    regex=u'http'
                    pattern=re.compile(regex)
                    http_words=re.findall(pattern,mailText)
                    for i in range(10):
                        words+=http_words
                for word in words:
                    if not word in labelWords[curLabel].keys():
                        curProb+=math.log(1.0*laplace/(len(labelWords[curLabel])+laplace*len(words)))
                    else:
                        curProb+=math.log(float(labelWords[curLabel][word])/float(len(labelWords[curLabel])))
                    #print("curProb is ---",curProb)
                if curProb>prob:
                    prob=curProb
                    label=curLabel
            if label==ans:
                trueLabel+=1
        print("trueLabel--",trueLabel,"--toNumber----",toNumber)
        ac=float(float(trueLabel)/toNumber)
        toAC+=ac
        if(bestAC<ac):
            bestAC=ac
            print("best set is ",i)
            with open('trainData/data','w') as f:
                json.dump(labelWords,f,ensure_ascii=False,indent=2)        
        print("cur ac is ------------- "+str(ac))
    print("Average is --------- ",float(toAC/5))

    



train(1,1e-80)