#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import os


class Color:
    END = "\33[0m"
    BOLD = "\033[1m"
    YELLOW = "\33[33m"
    RED = '\033[91m'
    BLUE = "\033[94m"


class Config:
    LHOST = "127.0.0.1"  # Example
    LPORT = 8080  # Example


def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((Config.LHOST, Config.LPORT))
        print("[•] Server started.")
        s.listen(1)
        print("[•] Listening...")
        conn, addr = s.accept()
        print(f"{Color.YELLOW}[•] Connected to {Color.BOLD}{addr[0]}{Color.END}")
        while True:
            comm = input(f"{Color.BLUE}[>] {Color.END}")
            if not comm:
                print("[•] Connection finished.")
                break
            try:
                conn.send(comm.encode())
            except BrokenPipeError:
                print(f"{Color.RED}[•] Connection lost.{Color.END}")
                break
            else:
                output = conn.recv(1024)
                print(output.decode().removesuffix("\n"))


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        os.system("clear")
        print("[•] Exiting...")
        exit(0)
