from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'camerafeedpkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'video'), glob('video/*.mov')),
        (os.path.join('share', package_name, 'calibration/images'), glob('calibration/images/*')),
        (os.path.join('share', package_name, 'calibration'), glob('calibration/*.yaml')),
        (os.path.join('share', package_name, 'calibration'), glob('calibration/*.txt')),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Wolfgang Prokop',
    maintainer_email='wolfgang.prokop98@gmail.com',
    description='A few different nodes that will read in a video, rectifiy it and later make some different opencv algorithm like canny edge and laplacian edge detection',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera_driver = camerafeedpkg.camera_driver:main',
            'img_publisher=camerafeedpkg.camera_driver.py:main',
            'camera_calibration_pub = camerafeedpkg.camera_calibration_pub:main',
            'camera_destorter_sub= camerafeedpkg.camera_destorter_sub:main',
            'imageprocessor_subpub = camerafeedpkg.imageprocessor_subpub:main',
            'camera_reader_sub= camerafeedpkg.camera_reader_sub:main',
        ],
    },
)
