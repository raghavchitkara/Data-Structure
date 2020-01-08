# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 17:49:56 2019

@author: Raghav Chitkara
"""

def towers_of_hanoi(number_of_disks, startpeg=1, endpeg=3):
    if number_of_disks :
        print(startpeg, endpeg)
        towers_of_hanoi(number_of_disks-1,startpeg,6-startpeg-endpeg)
        print("move disk %d from peg %d to peg %d ",number_of_disks,startpeg,endpeg)
        towers_of_hanoi(number_of_disks-1,6-startpeg-endpeg,endpeg)
        
        
towers_of_hanoi(number_of_disks=3)