import asyncio
import logging

from htcp import AsyncServer

from dataclasses import dataclass


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(filename="async_server.log", encoding="utf-8", mode="a"),
        logging.StreamHandler()
    ]
)

server_logger = logging.getLogger("my-async-server")
server_logger.setLevel(logging.INFO)


app = AsyncServer(
    name="example-async-server",
    host="0.0.0.0", port=2354,
    max_connections=100,
    expose_transactions=True,
    logger=server_logger
)


@app.transaction(code="get_welcome")
async def get_welcome_trans(client_name: str) -> tuple[str, int]:
    # Simulate async operation
    await asyncio.sleep(0.01)
    response = f"Welcome {client_name}!"
    return response, 0


@app.transaction(code="upload_file")
async def upload_file_trans(file_name: str, file_body: bytes) -> str:
    print(f"Uploaded file '{file_name}' with {len(file_body)} bytes")
    return "ok"


@dataclass
class MyAPIPackage:
    text: str


@app.transaction(code="send_custom_data")
async def custom_data_trans(my_custom_data: MyAPIPackage) -> MyAPIPackage:
    print(f"Custom data: {my_custom_data.text}")
    return MyAPIPackage(text="message handled")


if __name__ == "__main__":
    asyncio.run(app.up())
