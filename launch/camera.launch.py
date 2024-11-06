import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    # Camera Image
    camera_publisher = Node(
        package='camera_publisher',
        executable='camera_publisher',
        name='camera_publisher',
    )
    return LaunchDescription([
        camera_publisher
    ])
