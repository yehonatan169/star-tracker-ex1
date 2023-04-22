import cv2
import numpy as np
import random

num_images = 1
for i in range(num_images):
    img1 = np.zeros((600, 600), np.uint8)
    img2 = np.zeros((600, 600), np.uint8)
    num_stars_big = random.randint(50, 100)
    num_stars_small = random.randint(5, 15)
    stars = []
    for j in range(num_stars_big):
        x = random.randint(0, 600)
        y = random.randint(0, 600)
        r = random.randint(3, 7)
        b = random.randint(200, 250)
        stars.append((x, y, r, b))
        cv2.circle(img1, (x, y), r, b, -1)
    index = np.random.choice(
            len(stars), num_stars_small, replace=False)
    stars2 = [stars[j] for j in index]
    for star in stars2:
        cv2.circle(img2, (star[0], star[1]), star[2], star[3], -1)

    filename1 = f"image_big_{i}.jpg"
    cv2.imwrite(filename1, img1)
    filename2 = f"image_small_{i}.jpg"
    cv2.imwrite(filename2, img2)