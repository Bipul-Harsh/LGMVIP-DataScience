import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser(description="Create sketch image of any given photo.")
parser.add_argument('--input_file', type=str, default="./image.webp", help="(Required) the image file you want to read")
parser.add_argument('--wt_ratio', type=float, default=1, help="width ratio to resize frame horizontally")
parser.add_argument("--ht_ratio", type=float, default=1, help="height ratio to resize frame veritcally")
parser.add_argument("--wt_size", type=int, default=0, help="to provide the frame width size in pixels")
parser.add_argument("--ht_size", type=int, default=0, help="to provide the frame height size in pixels")

args = parser.parse_args()

INPUT_FILE = args.input_file
assert INPUT_FILE != None, "Please provide a image file"
WT_RATIO = args.wt_ratio
HT_RATIO = args.ht_ratio
HT_SIZE = args.ht_size
WT_SIZE = args.wt_size
WINDOW_NAME = "Sketch Maker"

img = cv2.imread(INPUT_FILE)
img = cv2.resize(img, (WT_SIZE,HT_SIZE), fx=WT_RATIO, fy=HT_RATIO)
assert type(img) != type(None), "Please provide valid image location"

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted_img = cv2.bitwise_not(gray_img)
smooth_img = cv2.GaussianBlur(inverted_img, (21, 21), sigmaX=0, sigmaY=0)
def divide(x,y):
    return cv2.divide(x, 255-y, scale=256)
sketch_image = divide(gray_img, smooth_img)

cv2.namedWindow(WINDOW_NAME)

while(True):
    cv2.imshow(WINDOW_NAME, sketch_image)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.imwrite("sketch.png",sketch_image)
cv2.destroyAllWindows()