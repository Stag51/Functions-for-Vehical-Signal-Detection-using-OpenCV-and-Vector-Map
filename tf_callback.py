def tf_callback(self, tf_msg):
        # Process TF messages
        rospy.loginfo("Received TF Message: {}".format(tf_msg))
        # Example: Extracting transform information
        for transform in tf_msg.transforms:
            source_frame = transform.header.frame_id
            target_frame = transform.child_frame_id
            translation = transform.transform.translation
            rotation = transform.transform.rotation
            rospy.loginfo("Transform: {} to {}, Translation: {}, Rotation: {}".format(
                source_frame, target_frame, translation, rotation))
