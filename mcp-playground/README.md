https://medium.com/@piyushagni5/build-your-own-mcp-server-and-client-a-complete-guide-ee1451068458# 🧠 Build Your Own MCP Server & Client

This project demonstrates how to create a custom **MCP (Model Context Protocol)** server and client to extend AI capabilities using Python. Inspired by [this tutorial](https://medium.com/@piyushagni5/build-your-own-mcp-server-and-client-a-complete-guide-ee1451068458), it walks through setting up tools, exposing resources, and integrating with Claude Desktop.

---

## 🚀 Features

- Custom MCP server using `FastMCP`
- Tool and resource exposure via decorators
- Client-server communication over `stdio`
- Claude Desktop integration
- Python-based setup with `uv` for speed

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/mcp-server-client
cd mcp-server-client

### 2. Create Virtual Environment

```bash
uv venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate      # Windows
```

3. Install Dependencies
uv pip install mcp mcp[cli]


```bash
uv pip install mcp mcp[cli]
```


### 📦 Server Code (server.py)
```python 
from mcp.server.fastmcp import FastMCP
import math

mcp = FastMCP("HelloWorld")

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> float:
    return a / b

@mcp.tool()
def sqrt(a: int) -> float:
    return math.sqrt(a)

@mcp.tool()
def factorial(a: int) -> int:
    return math.factorial(a)

@mcp.resource("greeting://{name}")
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="stdio")
```


## 🧪 Testing Locally
Run the server:
python server.py

```bash
python server.py {serverpath}
```

