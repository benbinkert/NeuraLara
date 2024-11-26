#!/usr/bin/env python3
import sys
import rospy
import moveit_commander
from geometry_msgs.msg import Pose

def main():
    # ROS initialisieren
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_robot', anonymous=True)

    # RobotCommander und PlanningSceneInterface initialisieren
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()

    # MoveGroupCommander für eine Planungsgruppe
    group_name = "moveit_lara5"  # Name der Gruppe aus MoveIt
    move_group = moveit_commander.MoveGroupCommander(group_name)

    # Zielpose definieren
    pose_target = Pose()
    pose_target.orientation.w = 1.0
    pose_target.position.x = 0.4
    pose_target.position.y = 0.1
    pose_target.position.z = 0.4
    move_group.set_pose_target(pose_target)

    # Bewegung planen und ausführen
    plan = move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()

    # Shutdown
    moveit_commander.roscpp_shutdown()

if __name__ == '__main__':
    main()