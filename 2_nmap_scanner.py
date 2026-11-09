import nmap

scanner = nmap.PortScanner()

target = input("Enter target IP: ")
ports = input("Enter ports (example 1-100): ")

print("Starting Nmap scan...")

scanner.scan(hosts=target, ports=ports, arguments="-sT")

for host in scanner.all_hosts():
    print("Host:", host)
    print("State:", scanner[host].state())

    for protocol in scanner[host].all_protocols():
        print("Protocol:", protocol)

        for port in sorted(scanner[host][protocol].keys()):
            state = scanner[host][protocol][port]["state"]
            print(f"Port {port}: {state}")

print("Scan completed!")
