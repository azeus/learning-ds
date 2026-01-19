import socket
import time
import random


def unreliable_network_simulator():
    """See the problem viscerally"""

    class UnreliableChannel:
        def __init__(self, drop_rate=0.3, delay_range=(0.1, 2.0)):
            self.drop_rate = drop_rate
            self.delay_range = delay_range

        def send(self, message):
            # Messages can be dropped
            if random.random() < self.drop_rate:
                print(f"✗ Message '{message}' LOST in transit")
                return None

            # Messages can be delayed unpredictably
            delay = random.uniform(*self.delay_range)
            time.sleep(delay)
            print(f"✓ Message '{message}' delivered after {delay:.2f}s")
            return message

    # Try to coordinate without acknowledgments
    channel = UnreliableChannel(drop_rate=0.3)

    # General A sends attack command
    print("General A: Sending ATTACK command...")
    result = channel.send("ATTACK_AT_DAWN")

    if result:
        print("General A: Message delivered! But did B get it?")
        # This is the Two Generals Problem - we can never be SURE
    else:
        print("General A: Message lost! B won't attack.")


unreliable_network_simulator()