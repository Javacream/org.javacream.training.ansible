#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

mkdir -p ssh

if [[ ! -f ssh/id_ed25519 ]]; then
  ssh-keygen -t ed25519 -N "" -C "ansible-training" -f ssh/id_ed25519
fi

chmod 600 ssh/id_ed25519
chmod 644 ssh/id_ed25519.pub

docker compose up -d --build

echo
echo "Trainingsumgebung gestartet."
echo "Control Node öffnen:"
echo "  docker compose exec control bash"
echo
echo "Danach z.B.:"
echo "  ansible all -m ping"
echo "  ansible-playbook playbooks/01-systemd.yml"
