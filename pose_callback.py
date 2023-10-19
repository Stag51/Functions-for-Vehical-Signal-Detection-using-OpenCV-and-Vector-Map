#Following is the code to get current position of car from any vector map
    def pose_callback(self, pose_msg):
        # Process pose data
        rospy.loginfo("Received Pose Message: {}".format(pose_msg))
        # Example: Extracting position
        position = pose_msg.pose.position
        rospy.loginfo("Position: x={}, y={}, z={}".format(position.x, position.y, position.z))
