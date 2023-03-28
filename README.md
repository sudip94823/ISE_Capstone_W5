# ISE_Capstone_W5

###Our project is for the IoT based baby monitoring and under this vast concept, the below can be one 

The basic outline of a ROS-based project is pointed down below:

1. Setting Up ROS environment 

- Installation of ROS and creating a catkin workspace
- Creating a package of the project 

2. Designing the System

- The system consists of 3 nodes, the camera node , the motion detector node, and the alert node. 
- The camera node captures video and publishes it to a ROS topic.
- The motion detector node subscribes to the video topic and detects motion using OpenCV.
- The alert node provides a service that can be called to alert the caregiver when motion is detected.
- The action server will control the motion detector node and receive requests to detect motion. 

3. Implementing the camera node:
- Using OpenCV to capture video from a webcam or a Raspberry Pi camera. 
- Publish the video frames to a ROS topic

4. Implementing the motion detector node:
- Subscribing to the video topic and using OpenCV to detect motion in the frames.
- When motion is detected, caall the alert service to notify the caregiver.

5. Implementing the alert service:
- Creating a service that can be called to notify the caregiver when motion is detected 
- The service should accept a message with the location of the motion.
- The service can notify the caregiver via email, SMS, or some other method.

6. Implementing the action server:

 - Create an action server that controls the motion detector node.
 - The action server should receive requests to detect motion and return a response indicating      whether motion was detected or not.
 -The action server should also publish a message to the alert service when motion is detected.

7. Testing the system:

- Start the camera node, the motion detector node, and the alert node.
- Call the action server to detect motion and verify that the system works as expected.
