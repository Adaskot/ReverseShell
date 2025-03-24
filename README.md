# ReverseShell

This is a simple Python-based reverse shell program consisting of two components:
- `client.py`: A Python script that connects back to the server to establish a reverse shell.
- `server.py`: A Python script that listens for incoming client connections and allows remote command execution.

## Features

- **Server-side**: The server listens for incoming client connections.
- **Client-side**: The client connects back to the server and provides remote shell access.
- **Command-line interface**: Basic interaction for managing and controlling client connections.

## Installation

### Prerequisites

- Python 3.x should be installed on both the client and server machines.
- Make sure the server's IP address is accessible and not blocked by any firewalls.

### Steps

1. **Clone the repository**:
   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Adaskot/ReverseShell.git

## How to use

1. Write ip in client this client must connect with server ip.
2. First run server.py
3. Run client.py
4. After connection estabilished use this command:
    - list => show active clients
    - select [id of client] => selecting client to remote cmd

# ReverseShell
