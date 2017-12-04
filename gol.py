#!/usr/bin/python
from sense_hat import SenseHat
import random
import argparse
import time
x=[0,95,0]
def dosomething(dataset,parameter):
   for k in parameter:
        if k[1]==0 or k[1]>=4:
           dataset[k[0][0]][k[0][1]]=[0,0,0]
        elif k[1]==1 or k[1]==3:
            i=k[0][0]+random.randint(-1,1)
            j=k[0][1]+random.randint(-1,1)
            if i>=0 and i<=7 and j>=0 and j<=7:
                dataset[i][j]=x
        elif k[1]==2:
            i=k[0][0]+random.randint(-1,1)
            j=k[0][1]+random.randint(-1,1)
            if i>=0 and i<=7 and j>=0 and j<=7:
                dataset[i][j]=x
                dataset[k[0][0]][k[0][1]]=[0,0,0]

        
            
def main():
    sense=SenseHat()
    parser=argparse.ArgumentParser()
    parser.add_argument('n',help='probability of initial dots placed in a pixel',type=int)
    parser.add_argument('t',help='time for each run of simlation',type=float)
    args=parser.parse_args()
    i=0
    pixels=list()
    while i < 64:
        if random.randint(0,args.n-1)==0:
            pixels.append(x)
        else:
            pixels.append([0,0,0])
        i+=1
    sense.set_pixels(pixels)

    while True:
       
        dataset=list()
        for j in range(8):
            dataset.append([])
            for i in range(j*8,j*8+8):
                dataset[j].append(pixels[i])
        parameter=list()
        for i in range(8):
            for j in range(8):
                if dataset[i][j]==x:
                    cnt=0
                    if j+1!=8:
                        if dataset[i][j+1]==x:
                            cnt+=1
                    if j-1!=-1:
                        if dataset[i][j-1]==x:
                            cnt+=1
                    if i+1!=8:
                        if dataset[i+1][j]==x:
                            cnt+=1
                    if i-1!=-1:
                        if dataset[i-1][j]==x:
                            cnt+=1
                    if i+1!=8 and j+1!=8:
                        if dataset[i+1][j+1]==x:
                            cnt+=1
                    if i-1!=-1 and j+1!=8:
                        if dataset[i-1][j+1]==x:
                            cnt+=1
                    if i+1!=8 and j-1!=-1:
                        if dataset[i+1][j-1]==x:
                            cnt+=1
                    if i-1!=-1 and j-1!=8:
                        if dataset[i-1][j-1]==x:
                            cnt+=1
                    parameter.append([(i,j),cnt])
        
        if parameter==[]:
            print "Simulation over!"
            return
        dosomething(dataset,parameter)            
        pixels=list()
        for i in range(8):
            for j in range(8):
                pixels.append(dataset[i][j])    
        time.sleep(args.t)
        sense.set_pixels(pixels)                

if __name__=='__main__':
    main()