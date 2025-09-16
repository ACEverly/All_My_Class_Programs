'''
Name: Mary-Rose Tracy
ID#:1001852753
Using Windows, using VS Code
In Language of: Python
'''
#First lets do our imports
import os
#let's get into the hard part AKA recursiving it= Needs to calc the amount of size of sub & dir
def DirSpace(DRPathway):
    Sum=0 #you don't even do int for thsi
    #The iteration
    for entry in os.listdir(DRPathway):
        ForwardPWay=os.path.join(DRPathway,entry)
        #The computer reads if = file, + the amountofsize
        if os.path.isfile(ForwardPWay):
            Sum+=os.path.getsize(ForwardPWay)
        #The computer reads if = Dir, recursivs calc the amount of size
        elif os.path.isdir(ForwardPWay):
            Sum+=DirSpace(ForwardPWay)
    return Sum
TargetDir="."
print(DirSpace(TargetDir))
#The Pseduo Code in Class
"""
Pseudocode Given In class:
Lab 1: DirSpace
TargetDir =”.”
int Sum=0;
Sum = Dirspace(TargetDir)
Print Sum;
—------ 
int DirSpace(Str Dir)
int sum=0;
For each entry in Dir // siCip ‘.’ + ‘..’
If entry is file 
 Sum +=size(file)
if entry is Dir sum+=DirSpace(entry)
Return sum
"""