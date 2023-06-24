# Drowsiness-Detection-Embedded-System
This project is a simulation for drowsiness detection embedded system. There are two main python files which you want to run. First of all install requirements with this command.
```pip install requirements.txt```
Now you can run `raspberry_pi_server.py` on your raspberry system with the following command:
```python3 raspberry_pi_server.py '0.0.0.0':<SELECTED_PORT>```
Then you can run your client on your laptop with this command:
```python3 inference.py '<RASPBERRY_IP>':<RASPBERRY_SELECTED_PORT>```
This module opens your webcam and then it has two phases. At first it calibrates your face and then it begins to work. this module outputs one of the following three classes: Drowsy, Alert, and phone. You can detect talking or working with phone, yawning, or sleepy eyes.