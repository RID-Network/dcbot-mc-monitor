from __future__ import annotations


import subprocess
from subprocess import Popen
import os
from mcstatus import JavaServer

MC_SERVER = os.getenv("MC_SERVER", "localhost:25565")

SERVER_EXECUTABLE = os.getenv("SERVER_EXECUTABLE")


class ServerInstance:
    def __init__(self, process: Popen) -> None:
        self.process = process
        self.server = JavaServer.lookup(MC_SERVER)

    def stop(self):
        self.process.stdin.write(b"stop\n")

    @staticmethod
    def start() -> ServerInstance:
        process = subprocess.Popen(
            [SERVER_EXECUTABLE], stdout=subprocess.PIPE, stdin=subprocess.PIPE
        )
        return ServerInstance(process)

    def query(self):
        return self.server.query()

    def status(self):
        return self.server.status()

    def broadcast(self, message: str):
        self.process.stdin.write(f"say {message}\n".encode())