import os 
import numpy as np
import shutil

path = '/data1/young/4k-pngs/SDR_4k'
#path = '/home/young/codes/edsr_4k/experiment/edsrtencent_x4/results-Demo/'
store_path = '/data1/young/4k-pngs/SDR_4k_edvr'
dir_index = os.listdir('/data1/young/4k/SDR_4k')
dir_index = [v[:-4] for v in dir_index]

img_list = os.listdir(path)

for dir_name in dir_index:

    tmp_list = [v for v in img_list if dir_name in v]

    dir_store_path = os.path.join(store_path,dir_name)
    if not os.path.exists(dir_store_path):
        os.makedirs(dir_store_path)

    for img_name in tmp_list:

        new_name = img_name[8:12]+'.png'

        shutil.copyfile(os.path.join(path,img_name),os.path.join(dir_store_path,new_name))