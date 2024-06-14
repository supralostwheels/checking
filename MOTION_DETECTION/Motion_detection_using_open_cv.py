import cv2, time, pandas
from datetime import datetime

# You have been approached by a company that is studying human behavior. Your task is to give them a webcam, that can detect the motion or any movement in front of it. This should return a graph, this graph should contain how long the human/object was in front of the camera.
#Initially, we save the image in a particular frame.

# The next step involves converting the image to a Gaussian blur image. This is done so as to ensure we calculate a palpable difference between the blurred image and the actual image.
#
# At this point, the image is still not an object. We define a threshold to remove blemishes such as shadows and other noises in the image.
#
# Borders for the object are defined later and we add a rectangular box around the object as we discussed earlier on the blog.
#
# Lastly, we calculate the time at which the object appears and exits the frame.


first_frame = None
status_list = [None,None]
times = []
df=pandas.DataFrame(columns=["Start","End"])

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame=gray
        continue
#We make use of the absdiff function to calculate the difference between the first occurring frame and all the other frames.

# The threshold function provides a threshold value, such that it will convert the difference value with less than 30 to black. If the difference is greater than 30 it will convert those pixels to white color. THRESH_BINARY is used for this purpose.
#
# Later, we make use of the findContours function to define the contour area for our image. And we add in the borders at this stage as well.
#
# The contourArea function, as previously explained, removes the noises and the shadows. To make it simple, it will keep only that part white, which has an area greater than 1000 pixels as we’ve defined for that.

# Later, we create a rectangular box around our object in the working frame.
#     As discussed earlier, the frame changes every 1 millisecond and when the user enters ‘q’, the loop breaks and the
#     window closes. We’ve covered all of the major details on this OpenCV Python Tutorial blog.One thing that remains
#     with our use-case is that we need to calculate the time for which the object was in front of the camera.

    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

    (cnts,_)=cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status=1

        (x, y, w, h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)
    status_list.append(status)

    status_list=status_list[-2:]


    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())


    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("Color Frame",frame)

    key=cv2.waitKey(1)

    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

print(status_list)
print(times)

for i in range(0, len(times), 2):
    df = df.append({"Start": times[i],"End": times[i+1]}, ignore_index=True)

df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows


"""Calculating the time"""
# We make use of DataFrame to store the time values during which object detection and movement appear in the frame.
#
# Followed by that is VideoCapture function as explained earlier. But here, we have a flag bit we call status. We use this status at the beginning of the recording to be zero as the object is not visible initially.
# We will change the status flag to 1 when the object is being detected as shown in the above figure.
# We are going to make a list of the status for every scanned frame and later record the date and time using datetime in a list if and where a change occurs.
# And we store the time values in a DataFrame as shown in the above explanatory diagram. We’ll conclude by writing the DataFrame to a CSV file as shown.