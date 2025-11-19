import socket

for port in range(1, 1025):
    s = socket.socket()
    s.settimeout(0.3)
    try:
        s.connect(("scanme.nmap.org", port))
        print(f"[+] Port {port} OPEN")
    except:
        pass
