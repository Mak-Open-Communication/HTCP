import logging
import asyncio

from htcp import AsyncClient

from dataclasses import dataclass


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(filename="async_client.log", encoding="utf-8", mode="a"),
        logging.StreamHandler()
    ]
)

client_logger = logging.getLogger("async-client-of-my-server")
client_logger.setLevel(logging.INFO)


@dataclass
class MyAPIPackage:
    text: str


async def main():
    # Using async context manager
    async with AsyncClient(
        server_host="0.0.0.0",
        server_port=2354,
        logger=client_logger
    ) as client:
        print(client.server_info())
        # {
        #   "server_name": "example-async-server",
        #   "server_addr": {"host": "127.0.0.1", "port": 2354},
        #   "connected": True,
        #   "available_transactions": ["get_welcome", "upload_file", "send_custom_data"]
        # }

        result1 = await client.call(transaction="get_welcome", client_name="John")
        print(result1[0], "\nExit code:", result1[1])
        # Welcome, John!
        # Exit code: 0

        result2 = await client.call(
            transaction="upload_file",
            file_name="example.txt",
            file_body=b"Hello World!"
        )
        print(result2)

        result3 = await client.call(
            transaction="send_custom_data",
            my_custom_data=MyAPIPackage(text="My custom message content"),
            result_type=MyAPIPackage
        )
        print(result3.text)


if __name__ == "__main__":
    asyncio.run(main())
