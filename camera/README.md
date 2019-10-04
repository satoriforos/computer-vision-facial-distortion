# "Photo Boo" camera
Takes a photo, thenreplaces a face with a background

## Requirements
- python 2 or 3
- dlib
- opencv
- pathlib2
- numpy
- picamera
- imutils
- requests

```
$ pip install python-opencv
$ pip install dlib
$ pip install pathlib2
$ pip install numpy
$ pip install picamera
$ pip install imutils
$ pip install requests
```

Be sure to enable your camera in the raspi-config

To get this working on a Pi, install Raspbian "Jesse":
https://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2017-07-05/

And follow these instructions to install OpenCV:
https://github.com/jabelone/OpenCV-for-Pi

Install python-dev
```
$ sudo apt-get install python-dev
```

Follow these instructions to install dlib:
https://www.pyimagesearch.com/2017/05/01/install-dlib-raspberry-pi/

## Running

```
$ ./run_photoboo.py
```
