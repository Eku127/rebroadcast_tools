from setuptools import setup

package_name = 'rebroadcast_tools'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Eku127',
    maintainer_email='jjiang127@connect.hkust-gz.edu.cn',
    description='A ROS 2 package for rebroadcasting topics like chatter, image, etc.',
    license='MIT',
    entry_points={
        'console_scripts': [
            'rebroadcast_chatter = rebroadcast_tools.rebroadcast_chatter:main',
            # 后续添加更多节点入口
            'rebroadcast_image_compressed = rebroadcast_tools.rebroadcast_image_compressed:main',

        ],
    },
)
