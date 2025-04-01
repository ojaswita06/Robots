# Use an official ROS 2 Humble base image
FROM ros:humble-ros-base

# Update and install necessary packages
RUN apt-get update && \
    apt-get install -y \
    python3-colcon-common-extensions \
    python3-pip \
    python3-rosdep \
    && rm -rf /var/lib/apt/lists/*