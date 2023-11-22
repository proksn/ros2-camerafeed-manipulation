#imageprocessing with opencv
import rclpy 
from rclpy.node import Node 
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 
import cv2 



 
class ImageSubscriber(Node):

  def __init__(self):

    super().__init__('image_subscriber')

    self.subscription = self.create_subscription(
      Image, 
      'retified_image', 
      self.listener_callback, 
      10)
    self.subscription # only to dont get a warning for unused variable
    self.publish_Canny=self.create_publisher(Image,'processedCanny_image',10)
    self.publish_Laplace=self.create_publisher(Image,'processedLaplace_image',10)  
  
    self.br = CvBridge()
      


  def listener_callback(self, data):

    self.get_logger().info('Receiving video in the processor')

    current_frame = self.br.imgmsg_to_cv2(data)

  
    gray_image = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    gauss = cv2.GaussianBlur(gray_image,(21,21),cv2.BORDER_DEFAULT)
    edge=cv2.Canny(gauss,0,10)

    laplacian = cv2.Laplacian(gauss, cv2.CV_64F)
    laplacian = cv2.normalize(laplacian, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)


    processed_msg = self.br.cv2_to_imgmsg(edge,encoding='8UC1')
    processedLaplace_msg=self.br.cv2_to_imgmsg(laplacian,encoding='8UC1')

    self.publish_Canny.publish(processed_msg)
    self.publish_Laplace.publish(processedLaplace_msg)




  
def main(args=None):
  

  rclpy.init(args=args)
  

  image_subscriber = ImageSubscriber()
  

  rclpy.spin(image_subscriber)
  image_subscriber.destroy_node()

  rclpy.shutdown()
  
if __name__ == '__main__':
  main()
