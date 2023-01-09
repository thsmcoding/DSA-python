# -*- coding: utf-8 -*-
"""
Created on Jan  2 08:22:37 2023
@author: HTS
"""

""" Chapter Recursion
    DSA - Exercices and problems 
    Language: Python
"""

def displayAllSubsets(l, used):
    if l is None:
        return
    elif len(l)==0:
        print("{}") 
        used.append([])
        return
    else:
        used.append([u for u in l])
        print(str(l).replace(']', '}').replace('[', '{'))            
        for i in range(len(l)-1, -1,-1):
            removed=l[i]
            l.pop(i)
            if not l in used:
                displayAllSubsets(l, used)
            l.insert(i,removed)       

def displaySubsets(l):
    mylist=[]
    displayAllSubsets(l, mylist)
    print("Program has found", len(mylist), " subsets.")

