$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

New-Item -ItemType Directory -Force -Path "ssh" | Out-Null

if (-not (Test-Path "ssh/id_ed25519")) {
    ssh-keygen -t ed25519 -N "" -C "ansible-training" -f "ssh/id_ed25519"
}

docker compose up -d --build

Write-Host ""
Write-Host "Trainingsumgebung gestartet."
Write-Host "Control Node öffnen:"
Write-Host "  docker compose exec control bash"
Write-Host ""
Write-Host "Danach z.B.:"
Write-Host "  ansible all -m ping"
Write-Host "  ansible-playbook playbooks/01-systemd.yml"
