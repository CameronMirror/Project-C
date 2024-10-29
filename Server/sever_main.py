import socket
import _thread
import sys

# Main compiling file for the server

server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)