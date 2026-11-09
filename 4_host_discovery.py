
import subprocess
import ipaddress

# Get default gateway
route = subprocess.check_output(
    ["ip", "route", "show", "default"],
    text=True
)

gateway = route.split()[2]
interface = route.split()[4]

# Get local IP
address = subprocess.check_output(
    ["ip", "-o", "-f", "inet", "addr", "show", "dev", interface],
    text=True
)

ip_cidr = address.split()[3]
local_ip = ipaddress.ip_interface(ip_cidr)
network = local_ip.network

# Determine IP class
first = int(str(local_ip.ip).split(".")[0])

if 1 <= first <= 126:
    ip_class = "Class A"
elif 128 <= first <= 191:
    ip_class = "Class B"
elif 192 <= first <= 223:
    ip_class = "Class C"
elif 224 <= first <= 239:
    ip_class = "Class D"
else:
    ip_class = "Class E"

print("Gateway IP:", gateway)
print("Local IP:", local_ip.ip)
print("Network:", network)
print("IP Class:", ip_class)

# Discover hosts on local network
if network.num_addresses > 256:
    print("Network too large for this example.")
    raise SystemExit

print("\nDiscovering active hosts...")

for host in network.hosts():
    if host == local_ip.ip:
        continue

    result = subprocess.run(
        ["ping", "-c", "1", "-W", "1", str(host)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if result.returncode == 0:
        print("[+] Active host:", host)

print("\nDiscovery completed!")
