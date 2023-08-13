from PIL import Image
import os


def tile(img, save_path, box):
    
    if box == "L":
        box= (0, 0, 256, 256)
    
    if box == "R":
        box= (256, 0, 512, 256)      
        
    img.crop(box).save(save_path)


### Split concat images (input, output) (train) ###

PATH_IN = "/home/tracy/Documents/VSGD-Net/human_data"
PATH_OUT = "/home/tracy/Documents/VSGD-Net/HE_datasets"
c_type = "HE"
d_type = "train"
folder = c_type + "_" + d_type
# fn = "img_0.png"
# tile(fn, PATH, d_type)

filelist = os.listdir(os.path.join(PATH_IN, folder))
for fn in filelist:
    if (fn.endswith(".png")):
        # name, ext = os.path.splitext(fn)
        img = Image.open(os.path.join(PATH_IN, folder, fn))
        tile(img, os.path.join(PATH_OUT, d_type + "_A", fn), "L")
        tile(img, os.path.join(PATH_OUT, d_type + "_B", fn), "R")

### Extract mask images (H) (train) ###

PATH_IN = "/home/tracy/Documents/VSGD-Net/human_data"
PATH_OUT = "/home/tracy/Documents/VSGD-Net/HE_datasets"
c_type = "H"
d_type = "train"
folder = c_type + "_" + d_type

filelist = os.listdir(os.path.join(PATH_IN, folder))
for fn in filelist:
    if (fn.endswith(".png")):
        img = Image.open(os.path.join(PATH_IN, folder, fn))
        tile(img, os.path.join(PATH_OUT, d_type + "_mask", fn), "R")