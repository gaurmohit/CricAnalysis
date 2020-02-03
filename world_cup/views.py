# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import sys 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from .cup_form import world_cup_form
import json

# Create your views here.
def world_cup(request):
    if request.method == 'POST':
        dataset=pd.read_csv('/home/mohit/Documents/clg-t/project/pro/LabelledDataset.csv')
        form = world_cup_form(request.POST)
        if form.is_valid():
            world_cup = form.data
            x= dataset.iloc[:,0:46].values
            y= dataset.iloc[:,217].values
            m=[]
            n=[]              
            a=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]              
            # e=input('Enter the contienent hosting the worldcup \n')
            e = world_cup['conti']
            # f=('enter 1 if the worldcup is of the form group a and group b,0 if the worldcup happens as a single group \n')
            f = int(world_cup['group_type'])
            if f==1:
                # z=input('enter the no of teams in group a \n')
                z = int(world_cup['num_of_teams_a'])
                # w=input('enter the no of teams in group b \n')
                w = int(world_cup['num_of_teams_b'])

                m = list(map(int , world_cup['team_a'].split(" ")))

                for k in range(0,z):
                    if m[k]=='1':
                        a[0]=1
                    elif m[k]=='2':
                        a[1]=1
                    elif m[k]=='3':
                        a[2]=1
                    elif m[k]=='4':
                        a[3]=1
                    elif m[k]=='5':
                        a[4]=1
                    elif m[k]=='6':
                        a[5]=1
                    elif m[k]=='7':
                        a[6]=1
                    elif m[k]=='8':
                        a[7]=1
                    elif m[k]=='9':
                        a[8]=1
                    elif m[k]=='10':
                        a[9]=1
                    elif m[k]=='11':
                        a[10]=1
                    elif m[k]=='12':
                        a[11]=1
                    elif m[k]=='13':
                        a[12]=1
                    elif m[k]=='14':
                        a[13]=1
                    elif m[k]=='15':
                        a[14]=1
                    elif m[k]=='16':
                        a[15]=1
                    elif m[k]=='17':
                        a[16]=1
                    elif m[k]=='18':
                        a[17]=1
                    elif m[k]=='19':
                        a[18]=1
                    elif m[k]=='20':
                        a[19]=1
                    elif m[k]=='21':
                        a[20]=1
                    elif m[k]=='22':
                        a[21]=1
                    elif m[k]=='23':
                        a[21]=1

                n = list(map(int , world_cup['team_b'].split(" ")))
                
                for k in range(0,w):
                        if n[k]=='1':
                            a[24]=1
                        elif n[k]=='2':
                            a[25]=1
                        elif n[k]=='3':
                            a[26]=1
                        elif n[k]=='4':
                            a[27]=1
                        elif n[k]=='5':
                            a[28]=1
                        elif n[k]=='6':
                            a[29]=1
                        elif n[k]=='7':
                            a[30]=1
                        elif n[k]=='8':
                            a[31]=1
                        elif n[k]=='9':
                            a[32]=1
                        elif n[k]=='10':
                            a[33]=1
                        elif n[k]=='11':
                            a[34]=1
                        elif n[k]=='12':
                            a[35]=1
                        elif n[k]=='13':
                            a[36]=1
                        elif n[k]=='14':
                            a[37]=1
                        elif n[k]=='15':
                            a[38]=1
                        elif n[k]=='16':
                            a[39]=1
                        elif n[k]=='17':
                            a[40]=1
                        elif n[k]=='18':
                            a[41]=1
                        elif n[k]=='19':
                            a[42]=1
                        elif n[k]=='20':
                            a[43]=1
                        elif n[k]=='21':
                            a[44]=1
                        elif n[k]=='22':
                            a[45]=1    
                
            elif f==0:
                # z=input('enter the no of teams participating \n')
                z = int(world_cup['num_of_teams'])
                w=int(z/2)

                # m = list(map(int , world_cup['teams'].split(" ")))
                d = list(map(int , world_cup['teams'].split(" ")))
                for i in range(0,w):
                    m.append(d[i])
                
                for k in range(0,w):
                        if m[k]=='1':
                            a[0]=1
                        elif m[k]=='2':
                            a[1]=1
                        elif m[k]=='3':
                            a[2]=1
                        elif m[k]=='4':
                            a[3]=1
                        elif m[k]=='5':
                            a[4]=1
                        elif m[k]=='6':
                            a[5]=1
                        elif m[k]=='7':
                            a[6]=1
                        elif m[k]=='8':
                            a[7]=1
                        elif m[k]=='9':
                            a[8]=1
                        elif m[k]=='10':
                            a[9]=1
                        elif m[k]=='11':
                            a[10]=1
                        elif m[k]=='12':
                            a[11]=1
                        elif m[k]=='13':
                            a[12]=1
                        elif m[k]=='14':
                            a[13]=1
                        elif m[k]=='15':
                            a[14]=1
                        elif m[k]=='16':
                            a[15]=1
                        elif m[k]=='17':
                            a[16]=1
                        elif m[k]=='18':
                            a[17]=1
                        elif m[k]=='19':
                            a[18]=1
                        elif m[k]=='20':
                            a[19]=1
                        elif m[k]=='21':
                            a[20]=1
                        elif m[k]=='22':
                            a[21]=1
                        elif m[k]=='23':
                            a[21]=1
                # for k in range(0,w):
                #     u=input('enter the country')
                #     n.append(u)
                for i in range(w,z):
                    n.append(d[i])

                n = list(map(int , world_cup['teams'].split(" ")))
                for k in range(0,w):
                        if n[k]=='1':
                            a[24]=1
                        elif n[k]=='2':
                            a[25]=1
                        elif n[k]=='3':
                            a[26]=1
                        elif n[k]=='4':
                            a[27]=1
                        elif n[k]=='5':
                            a[28]=1
                        elif n[k]=='6':
                            a[29]=1
                        elif n[k]=='7':
                            a[30]=1
                        elif n[k]=='8':
                            a[31]=1
                        elif n[k]=='9':
                            a[32]=1
                        elif n[k]=='10':
                            a[33]=1
                        elif n[k]=='11':
                            a[34]=1
                        elif n[k]=='12':
                            a[35]=1
                        elif n[k]=='13':
                            a[36]=1
                        elif n[k]=='14':
                            a[37]=1
                        elif n[k]=='15':
                            a[38]=1
                        elif n[k]=='16':
                            a[39]=1
                        elif n[k]=='17':
                            a[40]=1
                        elif n[k]=='18':
                            a[41]=1
                        elif n[k]=='19':
                            a[42]=1
                        elif n[k]=='20':
                            a[43]=1
                        elif n[k]=='21':
                            a[44]=1
                        elif n[k]=='22':
                            a[45]=1    
                
                
            from sklearn.cross_validation import train_test_split
            x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/4,random_state=0)
            #fitting simple linear regression to the training set
            #feature scalling
            from sklearn.preprocessing import StandardScaler
            
            sc=StandardScaler()
            x_train=sc.fit_transform(x_train)
            # x_test=sc.fit_transform(x_test)

            from sklearn.linear_model import LogisticRegression
            classifier=LogisticRegression(random_state=0)
            classifier.fit(x_train,y_train)
            y_pred = classifier.predict([a])
            y_pred = y_pred[0]
            # print('the predicted country to win the 2019 worldcup is: ')
            # print(y_pred)
            dat = {"t" : y_pred}
            # return render_to_response('worldcup.html', locals())
            with open("world_cup/data_file.json", "w") as write_file:
                print("=================="+str(dat))
                json.dump(dat, write_file)
            
            import pdb; pdb.set_trace()
            with open("world_cup/data_file.json", "r") as read_file:
                da = json.load(read_file)
            print("yoooooooooooooo" + da["t"])
            return render(request,'worldcup.html')
        else:
            raise ValueError("Enter correct values only")
            # with open("data_file.json", "r") as read_file:
            #      data = json.load(read_file)
            # print(data)
    else:
        form = world_cup_form()
        return render(request , 'worldcup.html', {'form' : form})

def final_cup(request):
    with open("world_cup/data_file.json", "r") as read_file:
                da = json.load(read_file)
                print("yooooooooooo11111ooo" + da["t"])
    print("YYWWWW")
    return render_to_response(request , 'worldcup.html',da)