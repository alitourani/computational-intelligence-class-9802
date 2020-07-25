# Implementation of an Age Prediction Application using Deep Neural Networks

## Team Members:
- Seyyed Hossein Mirhosseini (960122680028)
- Omid Pakshekar (960122681009)

## Age_net.caffemodel
  This is the model that you must download before running AgeDetection_(Using CV) 
  https://drive.google.com/file/d/1oxxlMNdJFgCOEeZvQAnho6WfGdlJG-e9/view?usp=sharing
  
## Report File
  https://drive.google.com/file/d/1l42Li3yBtA841ZpT9P6p1kf1QnFc0sZx/view?usp=sharing

## Video(Report)
  https://drive.google.com/file/d/1Cw-KK7q-mIRxlWMbn-ygpfBFsnJFHtl6/view?usp=sharing
  
## Optional Report
  Here are some things that we did but didn't succeed(This is optional to see)
  https://drive.google.com/file/d/1ZYf_3ldJ2QZ2LyFQdrrxd8YFGpVKu-XF/view?usp=sharing
  
## Data
We combined these four datasets and for imdb we use panda to analyze the data
- IMDB     https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/
- Kaggle  https://www.kaggle.com/mariafrenti/age-prediction
- Kaggle  https://www.kaggle.com/frabbisw/facial-age
- Wiki     https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/

## Data analyze
We use panda to analyze data and bring the data out.And crop the images by face detection algorithms 

## Face Detection
We use face detection to recognize face from the image and then crop the face and save to the folder 

In opencv project we have 8 classes
- 0-2 years old
- 4-6 years old
- 8-12 years old
- 15-20 years old
- 25-32 years old
- 38-43 years old
- 48-53 years old
- 60-100 years old

In keras project we have 6 classes
- 0-5 years old
- 6-16 years old
- 17-30 years old
- 31-50 years old
- 51-70 years old
- 71-100 years old

## Library and widget we use: 
- panda
- imutils
- opencv
- matplotlib
- tensorflow
- keras
- numpy
- seaborn
