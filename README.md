# Finger Count Controller EV3

The Finger Count Controller EV3 is a project inspired by the article [Hand Detection and Finger Counting using OpenCV Python](https://medium.com/analytics-vidhya/hand-detection-and-finger-counting-using-opencv-python-5b594704eb08). It allows you to control an EV3 robot using finger gestures recognized by OpenCV. The robot can be controlled by pointing the cursor to buttons on the EV3 Remote application.

## Features

- Hand detection using OpenCV
- Finger counting algorithm
- Control EV3 robot by pointing cursor to buttons
- Simple and intuitive user interface
- Compatible with EV3 Remote application

## Installation

To set up the "Finger Count Controller EV3" project, follow these steps:

1. Clone this repository: `git clone https://github.com/TudorMihaescu24/finger-count-controller-ev3.git`
2. Install the necessary dependencies listed in the `requirements.txt` file. You can use `pip` to install them: `pip install -r requirements.txt`
3. Ensure you have the EV3 Remote application installed on your device. You can download it from the Microsoft Store.
4. Connect your EV3 robot to your device via Bluetooth or USB.
5. Run the `finger_count_controller_ev3.py` script to start the finger counting and cursor control functionality.

## Usage

Once the project is set up, follow these instructions to use the "Finger Count Controller EV3":

1. Launch the EV3 Remote application on your device.
2. Run the `finger_count_controller_ev3.py` script from the project.
3. Point your hand towards the camera and ensure it is detected.
4. Hold up fingers in front of the camera to control the robot:
   - 1 finger: Point the cursor to the "Move Forward" button
   - 2 fingers: Point the cursor to the "Move Backward" button
   - 3 fingers: Point the cursor to the "Turn Left" button
   - 4 fingers: Point the cursor to the "Turn Right" button
   - 5 fingers: Point the cursor to the "Stop" button
5. The robot will respond to the cursor position and perform the corresponding actions based on the buttons selected.

Please note that proper hand positioning and accurate finger detection are essential for precise cursor control. Experiment with different hand positions and gestures to achieve optimal results.

## Contributing

Contributions to this project are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push the changes to your forked repository: `git push origin feature-name`.
5. Open a pull request to the main repository's `master` branch.

We appreciate your contributions, whether they are bug fixes, new features, or improvements to the existing codebase. Together, let's make the "Finger Count Controller EV3" project even better!
