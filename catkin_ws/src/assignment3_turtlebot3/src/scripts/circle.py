#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    #Receiveing the user's input
    #print("Let's move your robot")
    speed = 1
    distance = 2*4
    #isForward = input("Foward?: ")#True or False

    #Checking if the movement is forward or backwards

    vel_msg.linear.x = 0
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

  #  while not rospy.is_shutdown():

        #Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_distance = 0
    spd = 0.3
    
        #Loop to move the turtle in an specified distance
    while(current_distance < 2*2*3.5):
        #Publish the velocity
        vel_msg.linear.x = spd/2;
        vel_msg.angular.z = spd;
 	
            
        velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
        current_distance= spd*(t1-t0)
        print(current_distance)
        #After the loop, stops the robot
    vel_msg.linear.x = 0
    vel_msg.angular.z =0
        #Force the robot to stop
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass

