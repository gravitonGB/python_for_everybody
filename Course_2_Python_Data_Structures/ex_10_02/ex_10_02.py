# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 13:37:59 2018

@author: tecra
"""
#10.2 Write a program to read through the mbox-short.txt and figure out the 
#distribution by hour of the day for each of the messages. You can pull the 
#hour out from the 'From ' line by finding the time and then splitting the 
#string a second time using a colon.
#
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
#Once you have accumulated the counts for each hour, print out the counts, 
#sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours = {}
for line in handle:
    if line.startswith('From'):
        words = line.split()
        try:
            hour = words[5]
        except:
            if len(words) < 5: continue
        hours[hour[:2]] = hours.get(hour[:2], 0) + 1
lst_hours = []
lst_hours = sorted([(hour, val) for hour, val in hours.items()])
for hour,val in lst_hours:
    print(hour,val)

"""
lst_hours = []
for hour,val in hours.items():
    lst_hours.append((hour, val))
lst_hours = sorted(lst_hours)
for hour,val in lst_hours:
    print(hour,val)
"""