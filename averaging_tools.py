import numpy as np
import cv2
import matplotlib.pyplot as plt

def make_coordinates(image, line_parameters):
    """This function is used to get the coordinates (values of the average of all the slopes) of the lines and unpack them"""
    try:
        slope, intercept = line_parameters
    except TypeError:
        slope, intercept = 0.001,0 # to avoid value 0
    y1 = image.shape[0]
    y2 = int(y1*(3/5))
    x1 = int((y1- intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return np.array([x1, y1, x2, y2])

def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameter = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameter[0]
        intercept = parameter[1]
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
         
    left_fit_average = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis =0)
    left_line = make_coordinates(image, left_fit_average)
    right_line = make_coordinates(image, right_fit_average)
  
    return np.array([left_line, right_line])