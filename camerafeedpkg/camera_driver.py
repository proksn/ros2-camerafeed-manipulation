import cv2
import rclpy # Python Client Library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images


class ImagePublisher(Node):

  def __init__(self):

    super().__init__('image_publisher')
      

    self.publisher_ = self.create_publisher(Image, 'video_frames', 10)
      
    #publish a message every 0.042 seconds
    timer_period = 0.042  

    self.timer = self.create_timer(timer_period, self.timer_callback)
         
    # Create a VideoCapture object
    # The argument '0' gets the default webcam.
    self.cap = cv2.VideoCapture("/home/trsa2024/lab_work/src/trsa_lab1/video/test.mov")
    #self.cap = cv2.VideoCapture('0')
         
    self.br = CvBridge()
   
  def timer_callback(self):

    ret, frame = self.cap.read()

    if ret == True:

      self.publisher_.publish(self.br.cv2_to_imgmsg(frame))
     


def main():
    rclpy.init()
  

    image_publisher = ImagePublisher()
  

    rclpy.spin(image_publisher)
  
    image_publisher.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()
