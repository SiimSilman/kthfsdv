import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64


class NodeA(Node):
    def __init__(self):
        # Initiera noden 'nodeA'
        super().__init__('nodeA')

        # Publicera på globalt topic /silman
        self.publisher_ = self.create_publisher(
            Int64, 
            '/silman', 
            10)
        
        # Frekvens 20 Hz = 0.05 sekunder
        timer_period = 0.05
        self.timer = self.create_timer(timer_period, self.timer_callback)

        # Parametrar för publicering
        self.k = 4
        self.n = 4

    def timer_callback(self):
        # Data typ Int64
        msg = Int64()

        # Sätt data i meddelandet
        msg.data = self.k

        # Publicera meddelande på /silman
        self.publisher_.publish(msg)

        # Logga publiceringen
        self.get_logger().info(
            f'Publishing to /silman: {self.k}'
        )

        # Uppdatera k för nästa iteration
        self.k += self.n


def main(args=None):
    # Initiera ROS 2
    rclpy.init(args=args)

    # Skapa noden NodeA
    node = NodeA()

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
