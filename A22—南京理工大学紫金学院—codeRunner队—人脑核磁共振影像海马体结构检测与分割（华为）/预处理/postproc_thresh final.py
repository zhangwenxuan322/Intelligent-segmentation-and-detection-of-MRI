import nibabel
import numpy as np
import sys
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片


#lena = mpimg.imread('C:/Users/lenovo/Desktop/图书馆.jpg') # 读取和代码处于同一目录下的 lena.png
# 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
#lena.shape #(512, 512, 3)

#plt.imshow(lena) # 显示图片
#plt.axis('off') # 不显示坐标轴
#plt.show()

subjname = sys.argv[0] #"example_brain_t1"
#subjname = sys.argv[1]

for fname in [ "C:/Users/lenovo/Desktop/2018fwwb 1/Data&Labels/atlas-part1/ADNI_062_S_0690_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070424115325478_S16924_I50468.nii.gz".format(subjname), "C:/Users/lenovo/Desktop/2018fwwb 1/Data&Labels/atlas-part1/ADNI_062_S_0690_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070424115325478_S16924_I50468.nii.gz".format(subjname) ]:
    img = nibabel.load( fname )
    d = img.get_data(caching="unchanged")
    d[d < 256] = 0

    outimg = nibabel.Nifti1Image( d.astype("uint8"), img.affine )
    outimg.to_filename( fname )

    vol = (d > 0).sum() * np.abs(np.linalg.det(img.affine))
    print("%4.6f" % vol)
