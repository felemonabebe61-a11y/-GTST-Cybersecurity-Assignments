
# Nmap Module – Study Notes

## 1. What is Nmap?
Nmap stands for Network Mapper.
It is an open-source network scanning tool.

## 2. What is Python-Nmap?
Python-Nmap is a Python library that allows Python programs to control Nmap.

## 3. Installation
```bash
sudo apt install nmap
pip install python-nmap
```

## 4. Importing
```python
import nmap
```

## 5. Creating a scanner
```python
scanner = nmap.PortScanner()
```

## 6. Important methods

- scan(): Starts a scan.
- all_hosts(): Returns discovered hosts.
- state(): Returns host status.
- all_protocols(): Returns detected protocols.

## 7. Common Nmap commands

- nmap -sn IP: Host discovery.
- nmap -sT IP: TCP connect scan.
- nmap -p 80 IP: Scan port 80.
- nmap -sV IP: Service detection.

## 8. Uses of Nmap

- Network discovery
- Port scanning
- Service detection
- Network security auditing

## 9. What is NSE?
Nmap Scripting Engine allows Nmap to run scripts for network analysis.
