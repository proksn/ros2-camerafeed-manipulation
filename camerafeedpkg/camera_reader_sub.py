#creating a subscriber that is subscribed to every topic
#imageprocessing with opencv
import rclpy 
from rclpy.node import Node 
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 
import cv2 


 
class ImageSubscriber(Node):

  def __init__(self):

    super().__init__('image_subscriber')


    self.subscription_raw = self.create_subscription(
      Image, 
      'video_frames', 
      self.listener_callback_raw, 
      10)
    self.subscription_raw 
    
    self.subscription_rect = self.create_subscription(
      Image, 
      'retified_image', 
      self.listener_callback_rect, 
      10)
    self.subscription_rect

    self.subscription_processCanny = self.create_subscription(
      Image, 
      'processedCanny_image', 
      self.listener_callback_Canny, 
      10)
    self.subscription_processCanny

    self.subscription_processLaplace = self.create_subscription(
      Image, 
      'processedLaplace_image', 
      self.listener_callback_Laplace, 
      10)
    self.subscription_processCanny




    self.br = CvBridge()

      


  def listener_callback_raw(self, data):

    self.get_logger().info('Receiving raw video frame')

    current_frame = self.br.imgmsg_to_cv2(data)

    cv2.imshow("Raw Camera Image", current_frame)
    cv2.waitKey(1)

  def listener_callback_rect(self, data):

    self.get_logger().info('Receiving rect video frame')

    current_frame = self.br.imgmsg_to_cv2(data)


    cv2.imshow("Rectified Camera Image", current_frame)
    cv2.waitKey(1)

  def listener_callback_Canny(self, data):

    self.get_logger().info('Receiving Canny video frame')

    current_frame = self.br.imgmsg_to_cv2(data)

    cv2.imshow("Canny Camera Image", current_frame)
    cv2.waitKey(1)


  def listener_callback_Laplace(self, data):

    self.get_logger().info('Receiving Laplace video frame')

    current_frame = self.br.imgmsg_to_cv2(data)

    cv2.imshow("Laplace Camera Image", current_frame)
    cv2.waitKey(1)


  
def main(args=None):
  
  rclpy.init(args=args)
  
  image_subscriber = ImageSubscriber()

  rclpy.spin(image_subscriber)

  image_subscriber.destroy_node()
  
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()





