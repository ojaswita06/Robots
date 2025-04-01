from setuptools import setup

package_name = 'ros2_tutorials'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your.email@example.com',
    description='A simple ROS 2 publisher and subscriber with CSV logging',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_node = ros2_tutorials.publisher:main',
            'subscriber_node = ros2_tutorials.subscriber:main',
        ],
    },
)
