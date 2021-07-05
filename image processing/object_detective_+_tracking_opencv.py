# -*- coding: utf-8 -*-
"""
Created on Sun May 16 18:01:22 2021

@author: Administrator
"""
#%%
import cv2
import numpy as np
#import imutils
# also check: https://zhuanlan.zhihu.com/p/47959726
# video: https://www.youtube.com/watch?v=O1ABXetrMGs
# multi trackers ： https://blog.csdn.net/sinat_36811967/article/details/84141233

#%%

trackerTypes = ['BOOSTING', 'MIL', 'KCF','TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT','MULTI']

def TrackerName(trackerType):
 # Create a tracker based on tracker name
 if trackerType == trackerTypes[0]:
   tracker = cv2.TrackerBoosting_create()
 elif trackerType == trackerTypes[1]: 
   tracker = cv2.TrackerMIL_create()
 elif trackerType == trackerTypes[2]:
   tracker = cv2.TrackerKCF_create()
 elif trackerType == trackerTypes[3]:
   tracker = cv2.TrackerTLD_create()
 elif trackerType == trackerTypes[4]:
   tracker = cv2.TrackerMedianFlow_create()
 elif trackerType == trackerTypes[5]:
   tracker = cv2.TrackerGOTURN_create()
 elif trackerType == trackerTypes[6]:
   tracker = cv2.TrackerMOSSE_create()
 elif trackerType == trackerTypes[7]:
   tracker = cv2.TrackerCSRT_create()
 elif trackerType == trackerTypes[8]:
   tracker = cv2.TrackerMIL_create()
     #tracker = cv2.legacy.MultiTracker_create()
   
 else:
   tracker = None
   print('Incorrect tracker name')
   print('Available trackers are:')
   for t in trackerTypes:
     print(t)
   
 return tracker
#%%
TrDict = {'csrt': cv2.TrackerCSRT_create,
         'kcf' : cv2.TrackerKCF_create,
         'boosting' : cv2.TrackerBoosting_create,
         'mil': cv2.TrackerMIL_create,
         'tld': cv2.TrackerTLD_create,
         'medianflow': cv2.TrackerMedianFlow_create,
         'mosse':cv2.TrackerMOSSE_create}
#%%
#tracker = TrDict['csrt']()
tracker = TrackerName('CSRT')
#trackers = cv2.MultiTracker_creat()
trackers = TrackerName('MULTI')
#%%
#v = cv2.VideoCapture(r'D:\mot.mp4') # video
v = cv2.VideoCapture(r'D:\opencv\video\MVI_9593.mov')

#%%
#%% single
ret, frame = v.read()
#frame = imutils.resize(frame,width=600)
#cv2.imshow('Frame',frame)
bb = cv2.selectROI('Frame',frame)
tracker.init(frame,bb)
#%% single frame track


while True:
    ret, frame = v.read()
    if not ret:
        break
    #frame = imutils.resize(frame,width=600)
    (success,box) = tracker.update(frame)
    # ## save the data in text
    # np.savetext()
    if success:
        (x,y,w,h) = [int(a) for a in box]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(100,255,0),2)
    cv2.imshow('Frame',frame)
    key = cv2.waitKey(5) & 0xFF
    if key == ord('q'):
        break
v.release()
cv2.destroyAllWindows()
#%% multi frames track
ret, frame = v.read()
k = 5
for i in range(k):
    cv2.imshow('Frame',frame)
    bbi = cv2.selectROI('Frame',frame)
    #tracker_i = TrDict['csrt']()
    tracker_i = TrackerName('CSRT')
    trackers.add(tracker_i, frame, bbi)
#%%
    
while True:
    ret, frame = v.read()
    if not ret:
        break
    #frame = imutils.resize(frame,width=600)
    (success,box) = tracker.update(frame)
    # ## save the data in text
    # np.savetext()
    if success:
        (x,y,w,h) = [int(a) for a in box]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(100,255,0),2)
    cv2.imshow('Frame',frame)
    key = cv2.waitKey(5) & 0xFF
    if key == ord('q'):
        break
v.release()
cv2.destroyAllWindows()

#%%
while True:
    ret, frame = v.read()
    if not ret:
        break
    #frame = imutils.resize(frame,width=600)
    (success,box) = tracker.update(frame)
    
    if success:
       # (x,y,r) = [int(a) for a in box]
     for circle in circles[0]:
       x = int(circle[0])
       y = int(circle[1])
       r = int(circle[2])
       cv2.circle(frame, (x, y), r, (0, 0, 255), 3)  # 标记圆
    cv2.imshow('Frame',frame)
    key = cv2.waitKey(5) & 0xFF
    if key == ord('q'):
        break
v.release()
cv2.destroyAllWindows()
# for circle 
           # for circle in circles[0]:
                #  获取圆的坐标与半径
               # x = int(circle[0])
               # y = int(circle[1])
               # r = int(circle[2])
            # (x,y,r) = [int(a) for a in box]
# cv2.circle(frame, (x, y), r, (0, 0, 255), 3)  # 标记圆
# cv2.circle(frame, (x, y), 3, (255, 255, 0), -1)  # 标记圆心