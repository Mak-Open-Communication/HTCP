from htcp.server import Server
from htcp.common.proto import Package

import logging

logging.basicConfig(level=logging.DEBUG)
server_logger = logging.getLogger("my-server")


app = Server(name="example-server", host="0.0.0.0", port=2353, logger=server_logger)


@app.register(transaction="get_welcome")
def get_welcome_trans(request):
    request = request.package()

    out_data =

    response = Package(data=out_data)
    return response


if __name__ == "__main__":
    app.up()
