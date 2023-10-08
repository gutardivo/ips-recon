import requests
import argparse


def recon(port_range):
    for a in range(256):
        for b in range(256):
            for c in range(256):
                for d in range(256):
                    for port in port_range:
                        url = f"http://{a}.{b}.{c}.{d}:{port}" 
                        try:
                            r = requests.get(url)
                            print("\033[92mURL:", url, "Response:", r.status_code, "\033[0m", end="\n")
                        except requests.exceptions.RequestException as e:
                            # print("\033[91mURL:", url, "Error:", e, "\033[0m") 
                            print("\033[91mURL:", url, "\033[0m", end="\r")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IP Recon Tool")
    parser.add_argument("-p", "--port", type=int, nargs='*', help="Specify the port(s) to scan")
    args = parser.parse_args()

    if args.port:
        port_range = args.port
    else:
        # If no port is specified, scan all ports (1-65535)
        port_range = range(1, 65536)

    recon(port_range)

# You can use in terminal like: python3 main.py 8080 6767
# Or only python3 main.py to scan all ports