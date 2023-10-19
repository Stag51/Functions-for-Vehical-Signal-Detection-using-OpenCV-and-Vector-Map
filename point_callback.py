#Following is the code for Point Callback from any vector map
def point_callback(self, point_msg):
        # Process point data
        rospy.loginfo("Received Point Message: {}".format(point_msg))
        # Example: Extracting point information
        point_id = point_msg.pid
        point_coordinates = (point_msg.x, point_msg.y, point_msg.z)
        rospy.loginfo("Point ID: {}, Coordinates: {}".format(point_id, point_coordinates))

