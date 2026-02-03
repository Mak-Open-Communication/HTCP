# HTCP

**HTCP** (High Transfer Control Protocol) is a lightweight binary TCP protocol library for Python that enables fast and type-safe client-server communication with automatic serialization.

## Features

- **Binary Protocol** — Efficient binary format for minimal overhead
- **Automatic Type Detection** — Supports all Python types including `dataclasses`, `Enum`, `datetime`, `Decimal`, `UUID`, and nested structures
- **Type-Safe RPC** — Transaction-based remote procedure calls with automatic argument conversion
- **Decorator-Based API** — Simple `@transaction` decorator for registering server handlers
- **Connection Management** — Built-in connection limits, graceful shutdown, and client tracking
- **Logging Integration** — Full logging support with configurable levels
- **Context Manager Support** — Use `with` statement for automatic connection handling

## Installation

```bash
git clone https://github.com/Mak-Open-Communication/HTCP.git
cd htcp
pip install -r requirements.txt
```

## Quick Start

### Server

```python
from htcp.server import Server
from dataclasses import dataclass

app = Server(name="my-server", host="0.0.0.0", port=2353)

@app.transaction(code="greet")
def greet(name: str) -> str:
    return f"Hello, {name}!"

@dataclass
class User:
    name: str
    age: int

@app.transaction(code="create_user")
def create_user(name: str, age: int) -> User:
    return User(name=name, age=age)

if __name__ == "__main__":
    app.up()
```

### Client

```python
from htcp.client import Client
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

client = Client(server_host="127.0.0.1", server_port=2353)
client.connect()

# Simple call
result = client.call(transaction="greet", name="World")
print(result)  # "Hello, World!"

# Call with dataclass result
user = client.call(transaction="create_user", name="John", age=30, result_type=User)
print(user.name, user.age)  # "John" 30

client.disconnect()
```

## Supported Data Types

| Type                                           | Support |
|------------------------------------------------|---------|
| `None`, `bool`, `int`, `float`, `str`, `bytes` | Full    |
| `list`, `tuple`, `dict`, `set`, `frozenset`    | Full    |
| `dataclasses`                                  | Full    |
| `pydantic.BaseModel`                           | Full    |
| `Enum`                                         | Full    |
| `datetime`, `date`, `time`, `timedelta`        | Full    |
| `Decimal`, `complex`, `UUID`                   | Full    |
| Nested structures                              | Full    |
| Big integers (arbitrary precision)             | Full    |

## Server Configuration

```python
Server(
    name="my-server",           # Server name
    host="0.0.0.0",             # Bind address
    port=2353,                  # Port number
    max_connections=100,        # Max simultaneous connections (0 = unlimited)
    expose_transactions=True,   # Allow clients to list available transactions        (OPTIONAL)
    logger=my_logger            # Custom logger instance                              (OPTIONAL)
)
```

## Use Cases

HTCP is ideal for:

- **Microservices Communication** — Fast binary protocol for internal service-to-service calls
- **Game Servers** — Low-latency communication for multiplayer games
- **IoT Applications** — Efficient protocol for resource-constrained devices
- **Real-time Systems** — When JSON/REST overhead is too high
- **Custom APIs** — Building proprietary protocols with type safety
- **Distributed Computing** — Task distribution and result collection

## Project Structure

```
htcp/
├── htcp/
│   ├── __init__.py
│   ├── client/
│   │   └── __init__.py      # Client implementation
│   ├── server/
│   │   └── server.py        # Server implementation
│   └── common/
│       ├── proto.py         # Protocol definitions
│       ├── serialization.py # Type serialization
│       └── utils.py         # Utilities
├── server_example.py
├── client_example.py
├── requirements.txt
├── CONTRIBUTING.md
└── LICENSE
```

## Requirements

- Python 3.10+

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Contacts

- **Author**: mk-samoilov (Mak Open Communication org)
- **Author GitHub**: [github.com/mk-samoilov](https://github.com/mk-samoilov)
- **Send issues here**: [github.com/Mak-Open-Communication/HTCP/issues](https://github.com/Mak-Open-Communication/HTCP/issues)

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
