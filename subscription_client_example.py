"""
HTCP Subscription Client Example
Demonstrates client-side subscription usage.
"""

import logging

from dataclasses import dataclass

from htcp import Client


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

client_logger = logging.getLogger("subscription-client")


@dataclass
class Notification:
    id: int
    user_id: int
    message: str
    timestamp: float


def main():
    client = Client(
        server_host="127.0.0.1",
        server_port=2355,
        logger=client_logger
    )

    client.connect()
    print(f"Connected to: {client.server_info()['server_name']}")

    # Example 1: Simple counter subscription
    print("\n--- Counter Subscription (5 values) ---")
    with client.subscribe(event_type="counter", start=100, step=10, delay=0.2) as sub:
        count = 0
        for data in sub:
            print(f"Counter: {data['value']}")
            count += 1
            if count >= 5:
                break  # Unsubscribe after 5 values

    # Example 2: Notification subscription with dataclass
    print("\n--- Notification Subscription (waiting for 3 notifications) ---")
    with client.subscribe(
        event_type="notifications",
        user_id=12345,
        data_type=Notification  # Automatically convert to Notification dataclass
    ) as sub:
        count = 0
        for notification in sub:
            print(f"Notification received: {notification.message}")
            count += 1
            if count >= 3:
                break

    # Example 3: Heartbeat subscription
    print("\n--- Heartbeat Subscription (3 beats) ---")
    with client.subscribe(event_type="heartbeat", interval=0.5) as sub:
        count = 0
        for beat in sub:
            print(f"Heartbeat #{beat['count']} at {beat['server_time']}")
            count += 1
            if count >= 3:
                break

    client.disconnect()
    print("\nDisconnected")


if __name__ == "__main__":
    main()
