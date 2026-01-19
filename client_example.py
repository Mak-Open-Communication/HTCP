from htcp.client import Client

from dataclasses import dataclass

import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(filename="client.log", encoding="utf-8", mode="a"),
        logging.StreamHandler()
    ]
)

client_logger = logging.getLogger("client-of-my-server")


client = Client(server_host="0.0.0.0", server_port=2353, logger=client_logger)


@dataclass
class MyAPIPackage:
    text: str


if __name__ == "__main__":
    client.connect()

    print(client.server_info())
    # {
    #   "server_name": "example-server",         "server_name": "unknown",
    #   "server_addr": {
    #     "host": "127.0.0.1",                   "server_name": "unknown" and
    #     "port": 2353                           "port": 0 if server has not been connected
    #   },
    #   "connected": True
    # }

    result1 = client.call(transaction="get_welcome", client_name="John")
    print(result1[0], "\nExit code:", result1[1])
    # Welcome, John!
    # Exit code: 0

    result2 = client.call(transaction="upload_file", file_name="example.txt", file_body=b"Hello World!")
    print(result2)

    result3 = client.call(transaction="send_custom_data", my_custom_data=MyAPIPackage(text="My custom message content"))
    print(result3.text)

    # client.disconnect()
