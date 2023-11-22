import rclpy # Python library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library
import ament_index_python
import yaml
from sensor_msgs.msg import CameraInfo
from image_geometry import PinholeCameraModel
import os
import copy
 
class ImageSubscriber(Node):

  def __init__(self):

    super().__init__('image_subscriber')
    self.camera_model=PinholeCameraModel()  
 
    self.subscription = self.create_subscription(
      Image, 
      'video_frames', 
      self.listener_callback, 
      10)
    self.subscription
    self.publish_rec=self.create_publisher(Image,'retified_image',10)  

    self.br = CvBridge()
    self.calibration_path = os.path.join( ament_index_python.get_package_share_directory('trsa_lab1'), 'calibration','ost.yaml') #import calibration file, if different cam this needs to be changed
    self.load_camera_calibration(self.calibration_path)
    self.camera_model.fromCameraInfo(self.camera_info)

  def load_camera_calibration(self, calibration_path):

    with open(calibration_path, 'r') as file: 
      self.camera_info = CameraInfo() 
      calibration_data = yaml.safe_load(file) 
      self.camera_info.width = calibration_data['image_width'] 
      self.camera_info.height = calibration_data['image_height'] 
      self.camera_info.distortion_model = calibration_data['distortion_model'] 
      self.camera_info.d = calibration_data['distortion_coefficients']['data'] 
      self.camera_info.k = calibration_data['camera_matrix']['data'] 
      self.camera_info.r = calibration_data['rectification_matrix']['data'] 
      self.camera_info.p = calibration_data['projection_matrix']['data']



  def listener_callback(self, data):

    current_frame = self.br.imgmsg_to_cv2(data)



    rectified_image = copy.copy(current_frame)
    self.camera_model.rectifyImage(current_frame,rectified_image)

    rectified_msg = self.br.cv2_to_imgmsg(rectified_image,encoding='bgr8')

    self.publish_rec.publish(rectified_msg)






  
def main(args=None):
  

  rclpy.init(args=args)
  

  image_subscriber = ImageSubscriber()
  
 
  rclpy.spin(image_subscriber)
  

  image_subscriber.destroy_node()
  
  
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()

