import subprocess
import os
import platform
import glob
from Template_Task_Psychopy import tobii_research as tr
from eye_tracker import get_eyetracker


def call_eyetracker_manager_example():
    ETM_PATH =r'C:\Users\iCRIN_server\AppData\Local\Programs\TobiiProEyeTrackerManager\TobiiProEyeTrackerManager.exe'
    DEVICE_ADDRESS = "tet-tcp://169.254.218.51"
    eyetracker = tr.EyeTracker(DEVICE_ADDRESS)
    mode = "displayarea"
    etm_p = subprocess.Popen([ETM_PATH,
                              "--device-address=" + eyetracker.address,
                              "--mode=" + mode],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             shell=False)
    stdout, stderr = etm_p.communicate()  # Returns a tuple with (stdout, stderr)
    if etm_p.returncode == 0:
        print("Eye Tracker Manager was called successfully!")
    else:
        print("Eye Tracker Manager call returned the error code: " + str(etm_p.returncode))
        errlog = stdout  # On Windows ETM error messages are logged to stdout

        for line in errlog.splitlines():
            if line.startswith("ETM Error:"):
                print(line)


if __name__ == "__main__":
    call_eyetracker_manager_example()