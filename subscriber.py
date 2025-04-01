import os
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import csv

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')

        # Ensure the directory exists before writing the file
        data_dir = '/data'
        os.makedirs(data_dir, exist_ok=True)
        self.csv_file_path = os.path.join(data_dir, 'messages.csv')
        self.csv_file = open(self.csv_file_path, mode='a', newline='')
        self.csv_writer = csv.writer(self.csv_file)

        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.listener_callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')
        self.csv_writer.writerow([msg.data])  # Write received message to CSV
        self.csv_file.flush()  # Ensure data is written immediately

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Subscriber shutting down.")
    finally:
        node.csv_file.close()  # Close file on exit
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
