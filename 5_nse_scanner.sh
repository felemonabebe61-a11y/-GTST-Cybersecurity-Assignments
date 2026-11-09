
#!/bin/bash

echo "===== NSE SCANNER ====="

read -p "Enter target IP: " IP
read -p "Enter NSE script name: " SCRIPT

# Validate IP address
if ! python3 -c \
'import ipaddress,sys; ipaddress.IPv4Address(sys.argv[1])' \
"$IP" 2>/dev/null; then
    echo "Invalid IP address!"
    exit 1
fi

# Allow selected scripts
case "$SCRIPT" in
    banner|http-title|ssh-hostkey|ssl-cert)
        echo "Starting Nmap scan..."
        ;;
    *)
        echo "Script not allowed!"
        exit 1
        ;;
esac

nmap -sT --script "$SCRIPT" "$IP"

echo "Scan completed!"
