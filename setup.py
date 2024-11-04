from setuptools import find_packages, setup

package_name = 'camera_publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Khaled Gabr',
    maintainer_email='khaledgabr77@gmail.com',
    description=' CSI-Camera (like the Raspberry Pi Version 2.1 camera) with the NVIDIA Jetson Developer Kit',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera_publisher = camera_publisher.camera_publisher:main'

        ],
    },
)
