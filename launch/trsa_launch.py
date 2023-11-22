#launch file for 4 nodes camera_driver, rectifyer, processor and reader nodes

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        Node(
            package='trsa_lab1',
            #namespace='turtlesim1',
            executable='camera_driver',
            name='camera_driver'
        ),
        Node(
            package='trsa_lab1',
            #namespace='turtlesim2',
            executable='camera_destorter_sub',
            name='Rectifyer'
        ),
        Node(
            package='trsa_lab1',
            #namespace='turtlesim2',
            executable='imageprocessor_subpub',
            name='Processor'
        ),
        Node(
            package='trsa_lab1',
            #namespace='turtlesim2',
            executable='camera_reader_sub',
            name='Reader'
        ),
    ])