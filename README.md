# kthfsdv
## KTH Formula: Driverless recruitment exercises
### excercise 1
Created files nodeA and nodeB to communicate with each other.

Task: 
nodeA counts k+=n and publishes it with /silman topic at 20Hz (k_0=4, n=4)
nodeB subscribes to /silman topic and divides received message k/q (q=0.15)
nodeB logs the received message and the new value
setup.py connects the python script with the terminal in ROS2

Objective: Learn the basic structure of ROS2 Jazzy, rclpy and plotjuggler.

Setup:  Run docker setup to get ROS2 environment
        Within /src/exc1/packageX create python packageX
        Load nodeX.py within /src/exc1/packageX/packageX
        Load setup.py within /src/exc1/packageX
        (X = [A, B])
        
        
