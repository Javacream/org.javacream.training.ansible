import ansible_runner
from pathlib import Path
import os
result = ansible_runner.run(
    inventory = "/training/inventory.ini",
    host_pattern="web1,db1",
    module="ansible.builtin.ping",
    quiet=True
)

print(result.status)
print(result.rc)
print(result.events)
for event in result.events:
    if event.get("event") == "runner_on_ok":
        #print(event)
        print(event["event_data"]["res"])

