import cv2
import numpy as np

def canny_edge(input_image, threshold1, threshold2):
    """Combination method of smoothing and canny edge detection for an input image"""
    
    height_input_image = input_image.shape[0]
    width_input_image = input_image.shape[1]
    
    # convert to grayscale
    gray_conversion = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    
    # apply the gaussian blur filter to reduce noise in the image 
    x_kernel_size , y_kernel_size = (5,5)
    blur_conversion = cv2.GaussianBlur(gray_conversion, (x_kernel_size , y_kernel_size), 0)
    
    # create and apply the Canny edge detector to the input image
    canny_conversion = cv2.Canny(blur_conversion, threshold1, threshold2)
    
    return canny_conversion    



def roi_masking(input_image, polygons):
    """Region of interest masking function"""
    
    height_input_image = input_image.shape[0]
    width_input_image = input_image.shape[1]    
    
    # create the mask
    mask = np.zeros_like(input_image)
    
    # fill the ROI mask in the image using polygons and the mask, the mask will whiten all the pixels in the ROI
    cv2.fillPoly(mask, polygons, 255)
    
    # applying on the image
    roi_img_mask = cv2.bitwise_and(input_image, mask)
    
    return roi_img_mask


def show_lines(image, lines):
    """ Function used to draw lines in blue when detected by Hough Transformation"""
    lines_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            X1, Y1, X2, Y2 = line.reshape(4)
            cv2.line(lines_image, (X1, Y1), (X2, Y2), (255,0,0), 10)
    return lines_image

