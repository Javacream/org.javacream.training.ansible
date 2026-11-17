#!/usr/bin/env python3

import os
import socket
import time

print(f"Hostname: {socket.gethostname()}", flush=True)
print(f"Prozess-ID: {os.getpid()}", flush=True)

time.sleep(30)

print("Python-Skript erfolgreich ausgeführt")

