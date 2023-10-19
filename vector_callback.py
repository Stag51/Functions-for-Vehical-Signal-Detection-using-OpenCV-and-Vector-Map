#Following is the code for Vector Callback from any vector map
def vector_callback(self, vector_msg):
        # Process vector data
        rospy.loginfo("Received Vector Message: {}".format(vector_msg))
        # Example: Extracting vector information
        vector_id = vector_msg.vid
        rospy.loginfo("Vector ID: {}".format(vector_id))
