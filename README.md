# Image Projective Transform
Python mini-app that transforms an object in an image so that the object limits matches the image limits.

## Motivation
The app was developed for the purposes of an undergraduate class in Computer Science and Engineering Department of University of Ioannina and it aims to familirize the student with the projective transforms in Computer Vision.

## Requirements
+ [Python](https://www.python.org/)
+ [NumPy](https://numpy.org/)
+ [OpenCV](https://opencv.org/)
+ [Matplotlib](https://matplotlib.org/)
+ [Pillow](https://python-pillow.org/)

## Description
The app uses an 1000x1000 RGB image as input the user clicks to the 4 corners of the object he wants to highlight and the result is automatically produced by solving a 8x8 system and multipling the inverted table of the 8 parameters that are solutions to the system with the demanded positions of the four corners of the object in the output.

## Usage
To run the app in your machine:
1. Type in cmd the following command: python warp.py granma.jpg output.jpg.
2. Click to the 4 corners of the newspaper.

## Notes
Python3 was used for development.

## Contributor
+ [Marios Iakovidis](https://github.com/mariosjkb)