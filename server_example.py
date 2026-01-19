from htcp.server import Server

from dataclasses import dataclass

import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(filename="server.log", encoding="utf-8", mode="a"),
        logging.StreamHandler()
    ]
)

server_logger = logging.getLogger("my-server")


app = Server(name="example-server", host="0.0.0.0", port=2353, max_connections=100, logger=server_logger)


@app.transaction(code="get_welcome")
def get_welcome_trans(client_name: str) -> (str, int):
    response = f"Welcome {client_name}!"

    return response, 0


@app.transaction(code="upload_file")
def upload_file_trans(file_name: str, file_body: bytes) -> str:
    print(f"Uploaded file '{file_name}' with {len(file_body)} bytes")

    return "ok"


@dataclass
class MyAPIPackage:
    text: str


@app.transaction(code="send_custom_data")
def custom_data_trans(my_custom_data: MyAPIPackage) -> MyAPIPackage:
    print(f"Custom data: {my_custom_data.text}")

    return MyAPIPackage(text="message handled")


if __name__ == "__main__":
    app.up()
    # app.down()
