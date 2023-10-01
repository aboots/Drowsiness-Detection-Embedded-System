# Drowsiness-Detection-Embedded-System
This project presents a real-time drowsiness detection embedded system. The system utilizes your webcam to monitor and classify your state into one of three categories: Drowsy, Alert, or Phone. It can detect activities such as talking or working on the phone, yawning, or signs of sleepy eyes. The system operates in two phases: an initial calibration phase using your face, followed by the detection phase. The system is designed with a server-client architecture, allowing it to operate in real-time over networks.
There are two main Python files that you want to run. First of all install requirements with this command.

```pip install requirements.txt```

Now you can run `raspberry_pi_server.py` on your raspberry system with the following command:

```python3 raspberry_pi_server.py '0.0.0.0':<SELECTED_PORT>```

Then you can run your client on your laptop with this command:

```python3 inference.py '<RASPBERRY_IP>':<RASPBERRY_SELECTED_PORT>```

This module opens your webcam and then it has two phases. At first, it calibrates your face and then it begins to work. this module outputs one of the following three classes: Drowsy, Alert, and phone. You can detect talking or working with a phone, yawning, or sleepy eyes.

![Example](https://s8.uupload.ir/files/test_tebs.png)
