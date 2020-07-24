# Bone Fracture Detection from X-Ray images using Deep Neural Networks

## [](https://github.com/alitourani/ci-class-9802/tree/master/12-bone-fracture-detection#team-members)Team Members:

-   Seyyedeh Sara Naziri (960122680032)
-   Peyman Afshari (960122680083)
-   Taha Asghari (960122680119)

## [](https://github.com/alitourani/ci-class-9802/tree/master/12-bone-fracture-detection#descreption)Descreption:

To detect bone fractures, we used the mura dataset's `XR_humerus` category. This is a somewhat small category suited for our purpose.
We also used cross with TF (Tensorflow) backend and grabbed the classification,supervisor learning library inception-V3 from TF.

## [](https://github.com/alitourani/ci-class-9802/tree/master/12-bone-fracture-detection#dataset)Dataset:
the dataset was directly imported from kaggle to google colab and image size was set to 150 ( `IMG_SIZE=150`). then sorted them into 16 categories with `batch_size` and feed them to the model 30 times.
then we examine them for inappropriate data and categorize them under two folders. `Negative(normal)` and `Positive(abnormal)`. 
## [](https://github.com/alitourani/ci-class-9802/tree/master/12-bone-fracture-detection#training)Training the model:
after defining `train_directory` and connecting `pos`and`neg`folders (Positive data is much more important for model's precison) and defining base parameters of dataset, linking inception V3, defining model's structure and giving it default values, everything is ready for training.
We trained the model using cell's decison making (code) and cell's history.
## [](https://github.com/alitourani/ci-class-9802/tree/master/12-bone-fracture-detection#result)Saving the result:
the trained model was saved using `mode.save` with `.h5` format.

### [](https://github.com/alitourani/ci-class-9802/tree/master/12-bone-fracture-detection#dataset)imported library list:

![](https://user-images.githubusercontent.com/6348644/88411421-24689b80-cded-11ea-9147-2e76b35ba76e.png)
### full output:
![](https://user-images.githubusercontent.com/6348644/88411584-71e50880-cded-11ea-87c5-13bf705c62ed.png)
## [video](https://drive.google.com/file/d/1cJJTRMlEBG4Sz4VUSZIgiJVa2TFxTBrs/view?usp=sharing)
