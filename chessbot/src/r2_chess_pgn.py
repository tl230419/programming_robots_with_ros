#!/usr/bin/env python

import sys, rospy, tf, moveit_commander, random
from geometry_msgs.msg import Pose, Point, Quaternion
import pgn

class R2ChessboardPGN:
    def __init__(self):
        self.left_arm = moveit_commander.MoveGroupCommander("left_arm")
        self.right_arm = moveit_commander.MoveGroupCommander("right_arm")

    def set_grasp(self, state):
        if state == "pre-pinch":
            vec = [ 0.3, 0, 1.57, 0,    # index
                    -0.1, 0, 1.57, 0,   # middle
                    0, 0, 0,            # ring
                    0, 0, 0,            # pinkie
                    0, 1.1, 0, 0]       # thumb
        elif state == "pinch":
            vec = [ -0.1, 0, 1.57, 0,
                    0, 0, 1.57, 0,
                    0, 0, 0,
                    0, 0, 0,
                    0, 1.1, 0, 0]
        elif state == "open":
            vec = [0] * 18
        else:
            raise ValueError("unknown hand state; %s" % state)

        self.left_hand.set_joint_value_target(vec)
        self.left_hand.go(True)

    def set_pose(self, x, y, z, phi, theta, psi):
        orient = Quaternion(*tf.transformations.quaternion_from_euler(phi, theta, psi))
        pose = Pose(Point(x, y, z), orient)
        self.left_arm.set_pose_target(pose)
        self.left_arm.go(True)

    def set_square(self, square, height_above_board):
        if len(square) != 2 or not square[1].isdigit():
            raise ValueError(
                "expected a chess rank and file like 'b3' but found %s instead" % square)

        rank_y = -0.3 - 0.05 * (ord(square[0]) - ord('a'))
        file_x = 0.5 - 0.05 * int(square[1])
        z = float(height_above_board) + 1.0
        self.set_pose(file_x, rank_y, z, 3.14, 0.3, -1.57)

    def play_grame(self, pgn_filename):
        game = pgn.loads(open(pgn_filename).read())[0]
        self.set_grasp("pre-pinch")
        self.set_square("a1", 0.15)
        for move in game.moves:
            self.set_square(move[0:2], 0.10)
            self.set_square(move[0:2], 0.015)
            self.set_grasp("pinch")
            self.set_square(move[0:2], 0.10)
            self.set_square(move[2:4], 0.10)
            self.set_square(move[2:4], 0.015)
            self.set_grasp("pre-pinch")
            self.set_square(move[2:4], 0.10)

if __name__ == '__main__':
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('r2_chess_pgn', anonymous=True)
    argv = rospy.myargv(argv=sys.argv)
    if len(argv) != 2:
        print("usage: r2_chess_pgn.py PGNFILE")
        sys.exit(1)

    print("playing %s" % argv[1])
    r2pgn = R2ChessboardPGN()
    r2pgn.play_grame(argv[1])
    moveit_commander.roscpp_shutdown()