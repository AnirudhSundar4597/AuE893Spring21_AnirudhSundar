Welcome to the assignment7 readme

For part 1, ssh into the rpi using the password 'turtlebot'.

Run the command : roslaunch assignment7_slam mapping.launch slam_method:="<METHOD>"

Replace <METHOD> with gmapping or karto, as required.


For part 2, use the lidar_default.launch to run slam with the default lidar.

Use the lidar_h3d.launch to run slam with the Hokuyo 3D lidar.

The launch files for navigation don't work because of error in assigning the address to the map files. Map files are placed in the map folder for reference.

The videos show the recordings for SLAM and navigation for maps generated for both the lidars.


OBSERVATIONS BETWEEN THE default LIDAR and Hokuyo 3d

1. Range - The Hokuyo 3D lidar clearly has more scanning range than the default lidar. This is evident from the extent of the green highlight from the recordings of the respective SLAMs.
2. Accuracy - The Hokuyo 3D lidar generates a cleaner and more definite map in a shorter time as compared to the default lidar. It takes the Tbot3 lesser amount of total distance to get a good map of 
the overall environment.

3. Although performed in a simple environment, the H3D lidar will perform better in a real world environment and generate more accurate maps. From gazebo, it was clear that the H3D lidar generates maps
in a faster and accurate manner, as compared to the default lidar. Features such as wall edges are represented better in the H3D generated map.


PS: As usual this assignment was completed by Atef and I. I don't really care how the grading is done, but I just want to put it out there because the scene with our team is absolutely apathetic. It's just impossible for me to think of the group as a set of 'graduate' students.
