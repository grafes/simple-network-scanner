import socket

def scan(target, start_port, end_port):
    print(f"\n[+] Scanning {target} from port {start_port} to {end_port}\n")

    open_ports = []

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

        s.close()

    print("\n[+] Scan selesai")
    print(f"[+] Total open ports: {len(open_ports)}")


def main():
    try:
        target = input("Target IP: ")
        start = int(input("Start Port: "))
        end = int(input("End Port: "))

        scan(target, start, end)

    except ValueError:
        print("Input harus angka untuk port")


if __name__ == "__main__":
    main()
