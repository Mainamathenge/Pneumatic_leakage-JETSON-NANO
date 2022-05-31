# Pneumatic_leakage-JETSON-NANO
This project uses deep learning with audio classification to detect leakages in a pneumatic cylinder. The model was created with data collected from a microphone and was used to train the model which was later deployed on the Jetson Nano.

![THE PROJECTS FLOW DIAGRAM](https://github.com/Mainamathenge/Pneumatic_leakage-JETSON-NANO/blob/main/project%20images/project%20flow%201.PNG)

## DATA COLLECTION.
The data was collected by recording the real life pneumatic cylinder running collected at sampling rate of 10 seconds with a 16MHZ. The data was collected, labelled and split between 68% for training and 32% for the testing.

![DATA COLLECTION](https://github.com/Mainamathenge/Pneumatic_leakage-JETSON-NANO/blob/main/project%20images/WhatsApp%20Image%202022-05-20%20at%201.59.45%20PM.jpeg)
The dataset had 3 classes:

* CYLINDER_NORMAL   (pneumatic cylinder running without leakages)
* CYLINDER_LEAKAGE  (pneumatic cylinder running without leakages)
* IDLE              (pneumatic cylinder not running)
### Audio MFE
Audio MFE processing block extracts time and frequency features from a signal. However it uses a non-linear scale in the frequency domain, called Mel-scale. It performs well on audio data, mostly for non-voice recognition use cases when sounds to be classified can be distinguished by human ear.
The Audio MFE is used to generate features in the data in the time and frequency data from the data as shown graphically.
![FEATURE EXTRACTION].(https://github.com/Mainamathenge/Pneumatic_leakage-JETSON-NANO/blob/main/project%20images/mfe.PNG)
## MODEL TRAINING.
The model was trained using model was trained using Tensor flow and Keras as show in the [TRAING MODEL](https://github.com/Mainamathenge/Pneumatic_leakage-JETSON-NANO/blob/main/pneumatic%20cylinder/pneumatic%20leakage/model%20training.py)

### Model Architecture
The model was based on a CNN architecture as shown below:
```
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 reshape (Reshape)           (None, 99, 40)            0         
                                                                 
 conv1d (Conv1D)             (None, 99, 8)             968       
                                                                 
 max_pooling1d (MaxPooling1D  (None, 50, 8)            0         
 )                                                               
                                                                 
 dropout (Dropout)           (None, 50, 8)             0         
                                                                 
 conv1d_1 (Conv1D)           (None, 50, 16)            400       
                                                                 
 max_pooling1d_1 (MaxPooling  (None, 25, 16)           0         
 1D)                                                             
                                                                 
 dropout_1 (Dropout)         (None, 25, 16)            0         
                                                                 
 flatten (Flatten)           (None, 400)               0         
                                                                 
 y_pred (Dense)              (None, 3)                 1203      
                                                                 
=================================================================
Total params: 2,571
Trainable params: 2,571
Non-trainable params: 0
_________________________________________________________________
```
### Model validation

Below confussion matrix shows the model perfomance after training:
The confusion matrix showed how the model could collectly predict the diffrent classes of features that were used in training the dataset.

![CONFUSION MATRIX](https://github.com/Mainamathenge/Pneumatic_leakage-JETSON-NANO/blob/main/project%20images/confusion%20matrix.PNG)


## MODEL DEPLOYMENT,
After the model was trained and validated I deployed it on a Jetson nano and run it locally using the [main.py](https://github.com/Mainamathenge/Pneumatic_leakage-JETSON-NANO/blob/main/pneumatic%20cylinder/pneumatic%20leakage/Main.py) python script.

In the main.py file should be modified by
~~~ python
def main():
    count = 0
    dir_path = os.path.dirname('models location')
    modelfile = os.path.join(dir_path, 'model name')
~~~
I deployed the model in an assembly line for assembling Directional Control valves
![PHYSICAL DEPLOYMENT](https://github.com/Mainamathenge/Pneumatic_leakage-JETSON-NANO/blob/main/project%20images/WhatsApp%20Image%202022-05-20%20at%2012.44.52%20PM.jpeg)
The output of the model when the sytem was deployed was shown .On a dsiplay
![Disply output](https://github.com/Mainamathenge/Pneumatic_leakage-JETSON-NANO/blob/main/project%20images/deployment.PNG)
## TWILIO
For user notification  I used [twilio API](https://www.twilio.com/) and used as shown in the [twilio python file](https://github.com/Mainamathenge/Pneumatic_leakage-JETSON-NANO/blob/main/pneumatic%20cylinder/pneumatic%20leakage/twilio_sms.py)

for use the pyhon file can be modified to be as shown.
~~~ python
sid = '#######'
token = '########'
~~~
and to create a custom message and the message receiver.
~~~ python
 client.messages.create(messaging_service_sid = '#####',
                               body = message,
                               to = ['##########'])
~~~
