import cv2
import numpy as np
from Algorithm import *

algo = Algorithm()
dst_inliner, src_inliners = algo.run(image1='pics/ST_db1.png', image2='pics/fr2.jpg')
