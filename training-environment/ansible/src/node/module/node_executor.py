#!/usr/bin/python3
"""Demonstration: Python-Modul wird auf dem Managed Node ausgeführt."""

import os
import socket
import time

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(argument_spec={})

    hostname = socket.gethostname()
    pid = os.getpid()

    time.sleep(30)

    module.exit_json(
        changed=False,
        hostname=hostname,
        pid=pid,
        message="Python-Modul erfolgreich auf dem Managed Node ausgeführt",
    )


if __name__ == "__main__":
    main()
