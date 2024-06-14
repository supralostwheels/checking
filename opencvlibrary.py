"""WHAT IS COMPUTER VISSION"""
# To simplify the answer to this – Let us consider a scenario.
#
# We all use Facebook, correct? Let us say you and your friends went on a vacation and you clicked a lot of pictures and you want to upload them on Facebook and you did. But now, wouldn’t it take so much time just to find your friends faces and tag them in each and every picture? Well, Facebook is intelligent enough to actually tag people for you.
#
# So, how do you think the auto tag feature works? In simple terms, it works on computer vision.
#
#
# Computer Vision is an interdisciplinary field that deals with how computers can be made to gain a high-level understanding from digital images or videos.
#
# The idea here is to automate tasks that the human visual systems can do. So, a computer should be able to recognize objects such as that of a face of a human being or a lamppost or even a statue.


"""How Does A Computer Read An Image?"""
# The computer reads any image as a range of values between 0 and 255.
#
# For any color image, there are 3 primary channels – Red, green and blue. How it works is pretty simple.
#
# A matrix is formed for every primary color and later these matrices combine to provide a Pixel value for the individual R, G, B colors.
#
# Each element of the matrices provide data pertaining to the intensity of brightness of the pixel.
#
# Consider the following image:
# As shown, the size of the image here can be calculated as B x A x 3.
#
#
# Note: For a black-white image, there is only one single channel.


"""What Is OpenCV?"""
# OpenCV is a Python library which is designed to solve computer vision problems. OpenCV was originally developed in 1999 by Intel but later it was supported by Willow Garage.
#
# OpenCV supports a wide variety of programming languages such as C++, Python, Java etc. Support for multiple platforms including Windows, Linux, and MacOS.
#
# OpenCV Python is nothing but a wrapper class for the original C++ library to be used with Python. Using this, all of the OpenCV array structures gets converted to/from NumPy arrays.
#
#
# This makes it easier to integrate it with other libraries which use NumPy. For example, libraries such as SciPy and Matplotlib


"""BASIC OPERATIONS"""

##loading an image
import cv2
# colored Image
Img = cv2.imread('images/frog.webp', 1)
# Black and White (gray scale)
Img_1 = cv2.imread('images/frog.webp', 0)
#Later we can read the image using imread module. The 1 in the parameters denotes that it is a color image. If the parameter was 0 instead of 1, it would mean that the image being imported is a black and white image.

##Image Shape/Resolution
print(Img.shape)

##displaying the image
cv2.imshow('bw_frog', Img_1)
cv2.waitKey(0)
# cv2.waitKey(2000)
cv2.destroyAllWindows()

##resizing the image
resized_image = cv2.resize(Img_1, (650, 500))
cv2.imshow('frog',resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# resized_image=cv2.resize(Img_1,int(Img_1.shape[1]/2),int(Img_1.shape[0]/2))
cv2.imshow('frog',resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Here, we get the new image shape to be half of that of the original image



"""FACE DETECTION"""
#Step 1: Considering our prerequisites, we will require an image, to begin with. Later we need to create a cascade classifier which will eventually give us the features of the face.

# Step 2: This step involves making use of OpenCV which will read the image and the features file. So at this point, there are NumPy arrays at the primary data points.
#
# All we need to do is to search for the row and column values of the face NumPy ndarray. This is the array with the face rectangle coordinates.
#
# Step 3: This final step involves displaying the image with the rectangular face box


# First, we create a CascadeClassifier object to extract the features of the face as explained earlier. The path to the XML file which contains the face features is the parameter here.
#
# The next step would be to read an image with a face on it and convert it into a black and white image using COLOR_BGR2GREY.  Followed by this, we search for the coordinates for the image. This is done using detectMultiScale.
#
# What coordinates, you ask? It’s the coordinates for the face rectangle. The scaleFactor is used to decrease the shape value by 5% until the face is found. So, on the whole – Smaller the value, greater is the accuracy.
#
# Finally, the face is printed on the window.\

import cv2

# Create a CascadeClassifier Object
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Reading the image as it is
img = cv2.imread('images/girlimage1.jpeg')

# Reading the image as gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Search the co-ordintes of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05,
                                      minNeighbors=5)
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

resized = cv2.resize(img, (int(img.shape[1] / 7), int(img.shape[0] / 7)))

cv2.imshow("Gray",img)

cv2.waitKey(0)

cv2.destroyAllWindows()

"""Capturing Video Using OpenCV"""
# Capturing videos using OpenCV is pretty simple as well. the following loop will give you a better idea. Check it out:
# Capturing Video:
# Check out the following image:
# First, we import the OpenCV library as usual. Next, we have a method called VideoCapture which is used to create the VideoCapture object. This method is used to trigger the camera on the user’s machine. The parameter to this function denotes if the program should make use of the built-in camera or an add-on camera. ‘0’ denotes the built-in camera in this case.
#
# And lastly, the release method is used to release the camera in a few milliseconds.
#
# When you go ahead and type in and try to execute the above code, you will notice that the camera light switches on for a split second and turns off later. Why does this happen?
#
# This happens because there is no time delay to keep the camera functional.
# Looking at the above code, we have a new line called time.sleep(3) – This makes the script to stop for 3 seconds. Do note that the parameter passed is the time in seconds. So, when the code is executed, the webcam will be turned on for 3 seconds.


import cv2,time
video=cv2.VideoCapture(0)
check,frame=video.read()
print(check)
print(frame)
time.sleep(3)
cv2.imshow('Capturing',frame)
cv2.waitKey(0)
video.release()
cv2.destroyAllWindows
# the
# window:
# Adding
# a
# window
# to
# show
# the
# video
# output is pretty
# simple and can
# be
# compared
# to
# the
# same
# methods
# used
# for images.However, there is a slight change.Check out the following code:
#
#     I
#     am
#     pretty
#     sure
#     you
#     can
#     make
#     the
#     most
#     sense
#     from the above
#
#     code
#     apart
#     from one or two
#     lines.
#
#     Here, we
#     have
#     defined
#     a
#     NumPy
#     array
#     which
#     we
#     use
#     to
#     represent
#     the
#     first
#     image
#     that
#     the
#     video
#     captures – This is stored in the
#     frame
#     array.
#
#     We
#     also
#     have
#     check – This is a
#     boolean
#     datatype
#     which
#     returns
#     True if Python is able
#     to
#     access and read
#     the
#     VideoCapture object.
#
# As you can check out, we got the output as True and the part of the frame array is printed.
#
# But we need to read the first frame/image of the video to begin, correct?
#
# To do exactly that, we need to first create a frame object which will read the images of the VideoCapture object.
# As seen above, the imshow method is used to capture the first frame of the video.
#
# All this while, we have tried to capture the first image/frame of the video but directly capturing the video.



"""CAPTURING VIDEO DIRECTLY"""
#In order to capture the video, we will be using the while loop. While condition will be such that, until unless ‘check’ is True. If it is, then Python will display the frames.
#We make use of the cvtColor function to convert each frame into a grey-scale image as explained earlier.
#
# waitKey(1) will make sure to generate a new frame after every millisecond of a gap.
#
# It is important here that you note that the while loop is completely in play to help iterate through the frames and eventually display the video.
#
# There is a user event trigger here as well. Once the ‘q’ key is pressed by the user, the program window closes.
#
# OpenCV is pretty easy to grasp, right? I personally love how good the readability is and how quickly a beginner can get started working with OpenCV.
#
# Next up on this OpenCV Python Tutorial blog, let us look at how to use a very interesting motion detector use case using OpenCV.
#

import cv2,time
video=cv2.VideoCapture(0)
a=1
while True:
    a=a+1
    check,frame=video.read()
    print(frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Capturing',gray)
    key=cv2.waitkey(1)
    if key==ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows()

