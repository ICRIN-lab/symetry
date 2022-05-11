import time
from tkinter import Tk, PhotoImage
import base64
import os

# import Template_Task_Psychopy.tobii_research as tr
from Template_Task_Psychopy import tobii_research as tr


def get_eyetracker():
    eyetracker = tr.find_all_eyetrackers()[0]
    print("eyetrackers : ", eyetracker)

    print("Address: " + eyetracker.address)
    print("Model: " + eyetracker.model)
    print("Name (It's OK if this is empty): " + eyetracker.device_name)
    print("Serial number: " + eyetracker.serial_number)
    return eyetracker


def gaze_data_callback(gaze_data):
    # Print gaze points of left and right eye
    print("Left eye: ({gaze_left_eye}) \t Right eye: ({gaze_right_eye})".format(
        gaze_left_eye=gaze_data['left_gaze_point_on_display_area'],
        gaze_right_eye=gaze_data['right_gaze_point_on_display_area']))


def get_eyetracker_gaze(eyetracker):
    print("Subscribing to gaze data for eye tracker with serial number {0}.".format(eyetracker.serial_number))
    eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
    os.system('python symetry.py')

    eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
    print("\nUnsubscribed from gaze data.")


eyetracker = get_eyetracker()
