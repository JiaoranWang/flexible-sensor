# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
## opencv testing code
# import cv2
# import numpy as np
# img = cv2.imread('D:/opencv/1.jpg', cv2.IMREAD_COLOR)
# # img = cv2.imread('C:/Users/Administrator.DESKTOP-R4RKNS2/Desktop/USC2021SUM/PHD program/2022FALL/CV/1.jpg',cv2.IMREAD_COLOR)
# cv2.imshow("image", img)
# cv2.waitKey(0)

## opencv read then capture the video

# import cv2
# ##原文链接：https://blog.csdn.net/dz4543/article/details/86532092
# # https://blog.csdn.net/qq_34451909/article/details/109848613?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-0&spm=1001.2101.3001.4242
# cap = cv2.VideoCapture("D:/opencv/v1.mov")#名为'003.mp4'的文件
# c=0                             #文件名从0开始
# while(1):
#     # get a frame
#     ret, frame = cap.read()
#     # show a frame
#     cv2.imshow("capture", frame)
#     cv2.imwrite('image/'+str(c) + '.jpg',frame) #存储为图像
#     c=c+1
#     if cv2.waitKey(100) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()


# second try https://blog.csdn.net/he99774/article/details/111162775

from cv2 import VideoCapture
from cv2 import imwrite
 
# 定义保存图片函数
# image:要保存的图片名字
# addr；图片地址与相片名字的前部分
# num: 相片，名字的后缀。int 类型
def save_image(image, addr, num):
    address = addr + str(num) + '.jpg'
    imwrite(address, image)
 
if __name__ == '__main__':
 
    video_path = "D:/USC2021SPR/Group work/Picsvideos/video/MVI_9697/MVI_9697.mov" #视频路径
   
    out_path = "D:/USC2021SPR/Group work/Picsvideos/video/MVI_9697/img_" #保存图片路径+名字
 
    is_all_frame = False #是否取所有的帧
    sta_frame = 1 #开始帧
    end_frame = 1200 #结束帧
 
    ######
    time_interval = 30 #时间间隔
 
    # 读取视频文件
    videoCapture = VideoCapture(video_path)
 
    # 读帧
    success, frame = videoCapture.read()
    print(success)
 
    i = 0
    j = 0
    if is_all_frame:
        time_interval = 30
 
    while success:
        i = i + 1
        if (i % time_interval == 0):
            if is_all_frame == False:
                if i >= sta_frame and i <= end_frame:
                    j = j + 1
                    print('save frame:', i)
                    save_image(frame, out_path, j)
                elif i > end_frame:
                    break
            else:
                j = j + 1
                print('save frame:', i)
                save_image(frame, out_path, j)
 
        success, frame = videoCapture.read()


## Set the video to greyscale

# import numpy as np
# import cv2
# '''
# 这是一个将彩色视频装换成灰度视频的代码块
# '''
# # 捕获视频
# cap = cv2.VideoCapture('C:/Users/Administrator/Desktop/video.mp4')
# # 定义编解码器，创建VideoWriter 对象
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('C:/Users/Administrator/Desktop/output1.mp4',fourcc, 20.0, (1280,720),False)
# #（写出的文件，？？，帧率，（分辨率），是否彩色）  非彩色要把每一帧图像装换成灰度图
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret==True:
#         # frame = cv2.flip(frame,0)  #可以进行视频反转
#         # write the flipped frame
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #换换成灰度图
#         out.write(frame)
#         cv2.imshow('frame',frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
# # Release everything if job is finished
# cap.release()
# out.release()
# cv2.destroyAllWindows()



