# wild_cam_analysis
Tools to analyse data from wild life cameras

## A foreword
I started experimenting with wild-life cameras once wolves became resident in the area I live. My idea was to use wild-life cameras to detect wolves that come near life stock to somehow prevent them from hunting. I soon came acroos this project https://intelligenter-herdenschutz.de which does exactly that. Nonetheless, I learned, that you would need a lot of consumer grade wild-life cameras to surveil a field as large as a sheep pasture. This is because of the active infrared night vision capabilities that only go as far as maybe 10 meters (32 feet) and need a lot of battery. I researched on passive infrared, ultrasonic, motion detectors on sheep, image intensiviers (the "green" night vision), microphones and lidar amongst other methods for generating usable data in low light conditions. So far, I haven't found a device (that is within budget) that could overlook large areas in the night. Still, I gathered a lot of data with my wild-life cameras and came across the issue, that by far the most videos are of leaves that move in the wind and shadows of clouds. I played around with the three sensitivity levels provided by my cameras but the problem remained the same. Going through the videos by hand quickly got on my nerves. This was the motivation to write a script that analyses video clips from wild-life cameras to sort out which ones contain sights of animals or other interesting movements.

## What I tried so far
The problem at hand, differentiating interesting videos (e.g. an animal moving into the picture) from boring ones (e.g. movements of leaves), can be seen as a binary classification. However, I thought it would be better to label videos by the things that could be seen in them (e.g. video showing a bird), which would ease the process of selecting further (I have tons of videos of mice that I am not interested in anymore). The first thing that I tried was to train a neural net for image classification on frames that I extracted from videos ([like this one](#extracted)). This was easily done but did not perform well. I had a thought about how I could improve image classification and came up with the idea to substract the first frame of each video from my extracted frames. By that, everything that did not change between the [first frame](#first) and an [extracted frame](#extracted) would be black, whereas movements will be clearly visible resulting in [the third image](#difference) shown below. You might have noticed that I removed the lower section of the image showing the timestamp. 


<a name="first"></a>
![First_frame](https://user-images.githubusercontent.com/5765662/203027104-90af7d1b-d7dd-4fe1-a8b7-2a251319ac35.jpg)


<a name="extracted"></a>
![Extracted frame](https://user-images.githubusercontent.com/5765662/203026947-c892af3e-5756-42b1-aa43-15e94207b2a0.jpg)


<a name="difference"></a>
![Difference_frame](https://user-images.githubusercontent.com/5765662/203027162-91dd26f3-ab5c-4324-8994-4df4c8adce72.jpg)

Using these ["difference images"](#difference) for training an image classification neural net did not result in the desired accuracy and it got apparent, that object recognition is maybe better suited for the task. Therefore, the next thing I tried was to use [AWS Rekognition](https://aws.amazon.com/de/rekognition/) on [extracted frames](#extracted). Here, the bird was detected in the image with a confidence of 94%.

<a name="aws_rekognition_extracted"></a>
![aws_recognition_bird](https://user-images.githubusercontent.com/5765662/203055062-08916262-b920-445a-91df-429950a459ea.jpg)

A bird was also detected using the [difference image](#difference) but with a lower confidence of 70%. No bounding box was given for this detected bird.

I then used AWS Rekognition on a couple of images and the result was not overwhelming. Here are a few examples that suprised me:

![210416_dscf0055](https://user-images.githubusercontent.com/5765662/204999743-2513d5d0-3287-43ba-8b41-719c09254bab.jpg)
A mammal was detected with a convidence of only 67%. The marten was not recognized as such.

![frame_500 8](https://user-images.githubusercontent.com/5765662/205000581-7ade3998-4363-4e9d-a401-012957b930d0.jpg)
The cat was not detected nor any othe animal. I think the car label is also quite funny.

![210416_dscf0019](https://user-images.githubusercontent.com/5765662/205001573-badd120e-80ed-47d3-a99c-5edc7dfa5fb6.jpg)
The mouse did not get recognized. Therefore a mammal was detected with a confidence of 73% which it thinks may be a cougar (57%), kit fox (57%) or a fox (57%). No idea where this is recognized since no bounding box is given.

These last three images were all taken with infrared lighting as you might have noticed. For images taken in daylight it seems to work a little better but this is just my gut feeling.

It showed that AWS Rekognition is good at detecting an animal of some kind in images. All images that were interesting (meaning containing an animal) were highlighted. However, when it comes to the type of animal, there are issues. For example, cats got labelled as dogs, pigs and bears and mice never got recognized as such.


