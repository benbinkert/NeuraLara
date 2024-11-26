import sys
import moveit_commander
from moveit_commander.robot_trajectory import RobotTrajectory
from moveit_commander.planning_interface import MoveGroupInterface
import rospy


def move_robot():
    # Initialisierung von MoveIt!
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('moveit_example_python', anonymous=True)

    # Robot-Kommander und MoveGroup-Commander
    robot = moveit_commander.robot_trajectory.RobotCommander()
    scene = moveit_commander.planning_interface.PlanningSceneInterface()
    group = moveit_commander.MoveGroupCommander(
        "moveit_lara5")  # Ändern Sie den Arm-Namen entsprechend Ihrer Konfiguration

    # Starten Sie den Roboter
    group.set_named_target("home")  # Beispiel für vordefinierte Position, z.B. 'home'
    group.go(wait=True)

    # Eine einfache Bewegung zu einer Zielpose
    target_pose = group.get_current_pose().pose  # Holen Sie sich die aktuelle Pose
    target_pose.position.x += 0.1  # Bewege den Roboter um 0.1m auf der X-Achse
    target_pose.position.y += 0.1  # Bewege den Roboter um 0.1m auf der Y-Achse
    target_pose.position.z += 0.1  # Bewege den Roboter um 0.1m auf der Z-Achse

    # Setzen der Zielpose
    group.set_pose_target(target_pose)

    # Planen und ausführen der Bewegung
    plan = group.plan()
    group.go(wait=True)

    # Stoppen des Roboters
    group.stop()

    # MoveIt! schließen
    moveit_commander.roscpp_shutdown()


if __name__ == "__main__":
    move_robot()
