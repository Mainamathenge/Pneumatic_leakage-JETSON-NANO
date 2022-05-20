# Pneumatic_leakage-JETSON-NANO
This project uses Artificial inteligence to detect leakages in a pneumatic cylinder the model was created with data collected from a microphone and was used to train the model and the model was later deployed on the jetson nano.
![THE PROJECTS FLOW DIAGRAM](https://github.com/Mainamathenge/Pneumatic_leakage-JETSON-NANO/blob/main/project%20images/project%20flow%201.PNG)

## DATA COLLECTION.
The data was collected by recording the real life pneumatic cylinder running. I used  I managed to get 7 minutes. the data was 10 seconds with a 16MHZ data set . I collected the data and made the labels manualy during and also split the data to the training and testing datasets for each and every label with a split of 68% for training and 32% for the testing data. i later converted the to a json file to allow the dat to be used for training.
![DATA COLLECTION](https://github.com/Mainamathenge/Pneumatic_leakage-JETSON-NANO/blob/main/project%20images/WhatsApp%20Image%202022-05-20%20at%201.59.45%20PM.jpeg)
The data was classified into labels 
* CYLINDER_NORMAL   (pneumatic cylinder running without leakages)
* CYLINDER_LEAKAGE  (pneumatic cylinder running without leakages)
* IDLE              (pneumatic cylinder not running)
## MODEL CREATION.
Before the traing the features in the data was extracted using audio MFE block that extracted the frequency and time data from the audio data that was being used in the project.
The model was ceated using Tensor flow and Keras with 
 * input layer with (3960)features 
 * Dropout (rate 0.25)
 * 1D conv / pool layer (16 neurons, 3 kernel size, 1 layer)
 * Flatten layer
 * Output layer (3 classes)


 

