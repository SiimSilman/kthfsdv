import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64, Float64


class NodeB(Node):
    def __init__(self):
        # Initiera noden 'nodeB'
        super().__init__('nodeB')
        
        # Prenumerera på globalt topic /silman
        self.subscription = self.create_subscription(
            Int64,
            '/silman',
            self.listener_callback,
            10
        )
        
        # Publicera på /kthfs/result (Float64 eftersom vi dividerar med 0.15)
        self.publisher_ = self.create_publisher(
            Float64, 
            '/kthfs/result', 
            10)

        # Parameter för division
        self.q = 0.15

    def listener_callback(self, msg):
        # Data typ Int64
        result = Float64()

        # Sätt data i meddelandet och dividera med q
        result.data = msg.data / self.q

        # Publicera resultatet på /kthfs/result
        self.publisher_.publish(result)

        # Logga mottagningen och publiceringen
        self.get_logger().info(
            f'Received: {msg.data} Publishing to /kthfs/result: {result.data:.2f}'
        )


def main(args=None):
    # Initiera ROS 2
    rclpy.init(args=args)

    # Skapa noden NodeB
    node = NodeB()

    # While-loop för att hålla noden igång tills avbrott
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()