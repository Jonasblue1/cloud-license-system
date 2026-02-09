$software = Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* |
Select DisplayName, DisplayVersion |
Where-Object { $_.DisplayName } |
ForEach-Object {
    @{
        machine=$env:COMPUTERNAME
        name=$_.DisplayName
        version=$_.DisplayVersion
    }
}

$json = $software | ConvertTo-Json
Invoke-RestMethod -Uri http://localhost:8000/upload -Method POST -Body $json -ContentType "application/json"
