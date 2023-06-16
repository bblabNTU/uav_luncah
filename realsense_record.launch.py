from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_prefix

def generate_launch_description():
    # Get realsense2_camera package path
    realsense2_camera_prefix = get_package_prefix('realsense2_camera')

    # Define the nodes
    realsense_node = Node(
        package='realsense2_camera',
        executable='realsense2_camera_node',
        name='realsense2_camera_node',
        parameters=[{
            'rgb_camera.profile': '1920x1080x30'
        }],
        output='screen'
    )

    # ros2 bag record command
    record_node = ExecuteProcess(
        cmd=['ros2', 'bag', 'record', '/color/image_raw'],

        output='screen'
    )

    # rviz2 command
    rviz_node = ExecuteProcess(
        cmd=[get_package_prefix('rviz2') + '/lib/rviz2/rviz2', '-d','./.rviz/realsense.rviz'],
        output='screen'
    )

    return LaunchDescription([
        realsense_node,
        record_node,
        rviz_node
    ])
