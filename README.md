# Star Tracker
This repository represents our star tracker implemention in python for exercise 1 in the _Intro To New Space course_.
Below you will find the explanation about the algorithm that we used with the help of our instructor, and examples.

## Part 1
In this part we will exaplain how we implemented the algorithm.
After reaserch and help from our course instructor, we got decided to use this algorithm:
1. Get two sets of points as stars
2. Make 1000 iterations:
2.2 Get random star from the src set
2.3 Get random star from the dst set
2.4 FInd the two nearest neighbors of every star and calculate the angles, a1 a2.
2.5 If the absulote value of a1 - a2 is less that 4 then:
    make the tranform matrix from the six point of the images 
    check inliners by using the matrix to get points from src to dst, with loop:
    if the transformed point is close to the dst point with a treshhold then add the transformed point
    to the inliners.
2.6 If the new inliners set is bigger than the past one then the new inliners will be our inliners.
3. return inliners

## Part 2
In this part we made the detect method in the Algorithm class. Given an image it detects the stars and returns a list with x, y, r, b.
You can see this method in the Algorithm class 
```sh
def detect(self, image):
     ...
        return stars
```
## Part 3
In this part we made the algorithm method in the Algorithm class. Given two lists of stars, number of iterations and a threshold, it returns the stars pattern in both images.
You can see this method in the Algorithm class 
```sh
def algorithm(self, stars1, stars2, num_iterations, threshold):
...
        return inliers, src_inliners
```
## Part 4

## Installation and Run
Our star tracker uses these python packages: cv2, numpy, scipy.spatial, PIL.
If you want to run the code then look at the detect.py file for example
```sh
import cv2
import numpy as np
from Algorithm import *
algo = Algorithm()
dst_inliner, src_inliners = algo.run(image1='pics/fr1.jpg', image2='pics/fr2.jpg')
```

## Authors
Ibrahim Chahine, Yehonatan Amosi
