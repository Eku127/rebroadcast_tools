# rebroadcast_tools

**rebroadcast_tools** is a modular ROS 2 package designed for cross-machine communication in restricted network environments. It allows rebroadcasting remote topics (e.g., `/chatter`, `/image_raw`) as local topics, making them fully visible and usable in your local ROS graph.

## ✨ Features

- 🔁 Re-publishes remote topics to local ones for ROS visibility
- ✅ Supports partial DDS discovery (CycloneDDS peer mode)
- 🧱 Easy to extend: add new bridges for image, point cloud, tf, etc.
- 📦 Cleanly packaged with ROS 2 Python best practices

## 📦 Nodes

| Node Name | Function |
|-----------|----------|
| `rebroadcast_chatter` | Re-publishes `/chatter` → `/chatter` locally |



## 🚀 Usage

```bash
mkdir ~/ros2_ws/src
git clone https://github.com/Eku127/rebroadcast_tools.git

cd ~/ros2_ws
colcon build
source install/setup.sh

# for chatter test
ros2 run rebroadcast_tools rebroadcast_chatter
