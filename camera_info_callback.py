#Following is the ros code for getting camera info to main terminal
def camera_info_callback(self, camera_info_msg):
        # Process camera info data
        rospy.loginfo("Received Camera Info Message: {}".format(camera_info_msg))
        # Example: Extracting camera information
        focal_length_x = camera_info_msg.K[0]
        focal_length_y = camera_info_msg.K[4]
        rospy.loginfo("Focal Length: fx={}, fy={}".format(focal_length_x, focal_length_y))
