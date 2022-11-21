# wild_cam_analysis
Tools to analyse data from wild life cameras

## A foreword
I started experimenting with wild-life cameras once wolves became resident in the area I live. My idea was to use wild-life cameras to detect wolves that come near life stock to somehow prevent them from hunting. I soon came acroos this project https://intelligenter-herdenschutz.de which does exactly that. Nonetheless, I learned, that you would need a lot of consumer grade wild-life cameras to surveil a field as large as a sheep pasture. This is because of the active infrared night vision capabilities that only go as far as maybe 10 meters (32 feet) and need a lot of battery. I researched on passive infrared, ultrasonic, motion detectors on sheep, image intensiviers (the "green" night vision), microphones and lidar amongst other methods for generating usable data in low light conditions. So far, I haven't found a device (that is within budget) that could overlook large areas in the night. Still, I gathered a lot of data with my wild-life cameras and came across the issue, that by far the most videos are of leaves that move in the wind and shadows of clouds. I played around with the three sensitivity levels provided by my cameras but the problem remained the same. Going through the videos by hand quickly got on my nerves. This was the motivation to write a script that analyses video clips from wild-life cameras to sort out which ones contain sights of animals or other interesting movements.

## What I tried so far
The problem at hand, differentiating interesting videos (e.g. an animal moving into the picture) from boring ones (e.g. movements of leaves), can be seen as a binary classification. However, I thought it would be better to label videos by the things that could be seen in them (e.g. video showing a bird), which would ease the process of selecting further (I have tons of videos of mice that I am not interested in anymore). The first thing that I tried was to train a neural net for image classification on frames that I extracted from videos ([like this one](#extracted)). This was easily done but did not perform well. I had a thought about how I could improve image classification and came up with the idea to substract the first frame of each video from my extracted frames. By that, everything that did not change between the [first frame](#first) and an [extracted frame](#extracted) would be black, whereas movements will be clearly visible resulting in this [image](#difference). 


<a name="first"></a>
![First_frame](https://user-images.githubusercontent.com/5765662/203027104-90af7d1b-d7dd-4fe1-a8b7-2a251319ac35.jpg)


<a name="extracted"></a>
![Extracted frame](https://user-images.githubusercontent.com/5765662/203026947-c892af3e-5756-42b1-aa43-15e94207b2a0.jpg)


<a name="difference"></a>
![Difference_frame](https://user-images.githubusercontent.com/5765662/203027162-91dd26f3-ab5c-4324-8994-4df4c8adce72.jpg)


