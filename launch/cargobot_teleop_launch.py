from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            output='screen',
            parameters=[{'dev': '/dev/input/js0'}]
        ),

        Node(
            package='cargobot_teleop',
            executable='cargobot_teleop',
            name='cargobot_teleop',
            output='screen'
        )
    ])