"""
HTCP Subscription Server Example
Demonstrates server-side subscription handlers.
"""

import time
import random
import logging

from dataclasses import dataclass
from typing import Generator

from htcp import Server


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

server_logger = logging.getLogger("subscription-server")


app = Server(
    name="subscription-example-server",
    host="0.0.0.0", port=2355,
    max_connections=100,
    expose_transactions=True,
    logger=server_logger
)


@dataclass
class Notification:
    id: int
    user_id: int
    message: str
    timestamp: float


# Simulated notification storage
notification_counter = 0


@app.subscription(event_type="notifications")
def notifications_subscription(user_id: int) -> Generator[Notification, None, None]:
    """
    Subscribe to notifications for a specific user.

    This generator yields new notifications as they arrive.
    In a real application, this would poll a database or message queue.
    """
    global notification_counter

    print(f"User {user_id} subscribed to notifications")

    try:
        while True:
            # Simulate checking for new notifications
            time.sleep(1)

            # Randomly generate a notification (in real app, this would be from a queue)
            if random.random() > 0.5:
                notification_counter += 1
                notification = Notification(
                    id=notification_counter,
                    user_id=user_id,
                    message=f"Notification #{notification_counter} for user {user_id}",
                    timestamp=time.time()
                )
                print(f"Sending notification: {notification}")
                yield notification

    except GeneratorExit:
        print(f"User {user_id} unsubscribed from notifications")


@app.subscription(event_type="counter")
def counter_subscription(start: int = 0, step: int = 1, delay: float = 0.5):
    """
    Simple counter subscription that yields incrementing numbers.
    """
    current = start
    while True:
        yield {"value": current, "timestamp": time.time()}
        current += step
        time.sleep(delay)


@app.subscription(event_type="heartbeat")
def heartbeat_subscription(interval: float = 1.0):
    """
    Heartbeat subscription - useful for keeping connection alive
    or monitoring server status.
    """
    count = 0
    while True:
        count += 1
        yield {
            "type": "heartbeat",
            "count": count,
            "server_time": time.time()
        }
        time.sleep(interval)


@app.transaction(code="get_status")
def get_status() -> dict:
    """Simple transaction to check server status."""
    return {
        "status": "running",
        "notification_count": notification_counter
    }


if __name__ == "__main__":
    print("Starting subscription server on port 2355...")
    print("Available subscriptions:")
    print("  - notifications (user_id: int)")
    print("  - counter (start: int, step: int, delay: float)")
    print("  - heartbeat (interval: float)")

    app.up()
