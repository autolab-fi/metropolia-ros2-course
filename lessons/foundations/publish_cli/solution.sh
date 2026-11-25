set -e
source /opt/ros/jazzy/setup.bash
exec ros2 topic pub --rate 5 /learning/temperature std_msgs/msg/Float32 '{data: 20.5}'
