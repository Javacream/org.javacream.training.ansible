#!/usr/bin/python3
# -*- coding: utf-8 -*-

DOCUMENTATION = r'''
---
module: node_executor
short_description: Führt ein Python-Demobeispiel auf dem Managed Node aus
description:
  - Ermittelt Hostname und Prozess-ID des Managed Nodes.
  - Wartet 30 Sekunden, um die Ausführung beobachten zu können.
  - Ändert keine Ressourcen auf dem Zielsystem.
author:
  - Dr. Rainer Sawitzki
'''

EXAMPLES = r'''
- name: Eigenes Collection-Modul ausführen
  javacream.training.node_executor:
  register: result

- name: Ergebnis anzeigen
  ansible.builtin.debug:
    var: result
'''

RETURN = r'''
hostname:
  description: Hostname des Managed Nodes.
  returned: always
  type: str
  sample: web1
pid:
  description: Prozess-ID des Python-Moduls auf dem Managed Node.
  returned: always
  type: int
  sample: 1234
message:
  description: Statusmeldung.
  returned: always
  type: str
  sample: Python-Modul erfolgreich auf dem Managed Node ausgeführt
'''

import os
import socket
import time

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    if module.check_mode:
        module.exit_json(changed=False, message="Check Mode: keine Ausführung")
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
