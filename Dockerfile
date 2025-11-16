# Use official Python image (adjust version as needed)
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Ensure pip3 and python3 are used
RUN ln -sf /usr/local/bin/python3 /usr/bin/python && ln -sf /usr/local/bin/pip3 /usr/bin/pip

# Install uv (recommended by MCP docs) and pipx for isolated installs
RUN pip3 install --no-cache-dir uv pipx

# Copy project files
COPY . /app

# Install project dependencies using uv (fast, modern alternative to pip)
RUN uv pip install --system .

# Expose no ports (MCP runs over stdio by default)

# Default command: register the mcp server to claude desktop
CMD ["uv", "run", "mcp", "install", "main.py"]
