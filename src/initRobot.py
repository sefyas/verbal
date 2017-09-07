#! /usr/bin/env python
  
from rapid_pbd_msgs.msg import ExecuteProgramGoal
from rapid_pbd_msgs.msg import ExecuteProgramAction
import actionlib
import rospy

def main():
    rospy.init_node('init_robot')
    goal = ExecuteProgramGoal()
    goal.name = 'Yasaman-study start'
    client = actionlib.SimpleActionClient('rapid_pbd/execute_program_action', ExecuteProgramAction)
    client.wait_for_server()
    client.send_goal_and_wait(goal)
    print 'done'


if __name__ == '__main__':
    main()
