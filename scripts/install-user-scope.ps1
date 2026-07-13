$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot

function Copy-AgentDirectory {
    param(
        [Parameter(Mandatory = $true)][string]$Source,
        [Parameter(Mandatory = $true)][string]$Destination
    )

    New-Item -ItemType Directory -Force -Path $Destination | Out-Null
    Copy-Item -Path (Join-Path $Source "*") -Destination $Destination -Force
    Write-Host "Installed $Source -> $Destination"
}

Copy-AgentDirectory (Join-Path $Root ".claude\agents") (Join-Path $HOME ".claude\agents")
Copy-AgentDirectory (Join-Path $Root ".codex\agents") (Join-Path $HOME ".codex\agents")
Copy-AgentDirectory (Join-Path $Root ".cursor\agents") (Join-Path $HOME ".cursor\agents")
Copy-AgentDirectory (Join-Path $Root ".opencode\agents") (Join-Path $HOME ".config\opencode\agents")

Write-Host ""
Write-Host "Installed the Organization Agent Swarm at user scope."
