"""
HTCP Async Subscription Example
Demonstrates async server and client with subscriptions.
"""

import asyncio
import logging

from dataclasses import dataclass

from htcp import AsyncServer, AsyncClient


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


@dataclass
class StockPrice:
    symbol: str
    price: float
    timestamp: float


# --- SERVER ---

app = AsyncServer(
    name="async-subscription-server",
    host="0.0.0.0", port=2356,
    logger=logging.getLogger("async-server")
)


@app.subscription(event_type="stock_prices")
async def stock_prices_subscription(symbol: str):
    """
    Async subscription that simulates stock price updates.
    """
    import random
    base_price = random.uniform(100, 500)

    while True:
        # Simulate price change
        change = random.uniform(-2, 2)
        base_price = max(1, base_price + change)

        yield StockPrice(
            symbol=symbol,
            price=round(base_price, 2),
            timestamp=asyncio.get_event_loop().time()
        )

        await asyncio.sleep(0.3)


@app.subscription(event_type="chat_messages")
async def chat_subscription(room_id: str):
    """
    Simulates a chat room subscription.
    """
    messages = [
        "Hello everyone!",
        "How's it going?",
        "Anyone here?",
        "This is a test message",
        "Goodbye!"
    ]

    for i, msg in enumerate(messages):
        await asyncio.sleep(0.5)
        yield {
            "room_id": room_id,
            "message_id": i + 1,
            "text": msg,
            "author": f"user_{i % 3}"
        }


# --- CLIENT ---

async def run_client():
    """Run client examples."""
    await asyncio.sleep(0.5)  # Wait for server to start

    async with AsyncClient(server_port=2356) as client:
        print(f"Connected to: {client.server_info()['server_name']}")

        # Example 1: Stock price subscription
        print("\n--- Stock Price Subscription (AAPL, 5 updates) ---")
        async with client.subscribe(
            event_type="stock_prices",
            symbol="AAPL",
            data_type=StockPrice
        ) as sub:
            count = 0
            async for price in sub:
                print(f"  {price.symbol}: ${price.price}")
                count += 1
                if count >= 5:
                    break

        # Example 2: Chat messages subscription
        print("\n--- Chat Room Subscription (room-123) ---")
        async with client.subscribe(event_type="chat_messages", room_id="room-123") as sub:
            async for msg in sub:
                print(f"  [{msg['author']}]: {msg['text']}")

        print("\nClient finished")


async def main():
    """Run server and client concurrently."""
    # Start server task
    server_task = asyncio.create_task(app.up())

    # Run client
    try:
        await run_client()
    finally:
        # Shutdown server
        await app.down()

    print("\nAll done!")


if __name__ == "__main__":
    asyncio.run(main())
