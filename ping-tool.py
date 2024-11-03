import argparse
from scapy.all import IP, ICMP, sr
import time

class PingTool:
    def __init__(self, target_ip, count=4, timeout=2):
        self.target_ip = target_ip  # IP address to ping
        self.count = count  # Number of ping attempts (default is 4)
        self.timeout = timeout  # Time to wait for each ping response (default is 2 seconds)
        self.successful_pings = 0  # Keeps track of how many pings succeeded

    def send_ping(self):
        """Sends an ICMP Ping packet and checks the response."""
        ping_packet = IP(dst=self.target_ip) / ICMP()  # Create an ICMP ping packet
        response, _ = sr(ping_packet, timeout=self.timeout, verbose=False)  # Send and receive the response
        
        if response:
            self.successful_pings += 1  # Increment success count if we get a response
            print(f"Successful ping: {response[0][1].src}")  # Print source IP of the response
        else:
            print(f"Ping request to {self.target_ip} timed out.")  # Notify if there was no response

    def run(self):
        """Sends the specified number of ping requests."""
        print(f"Sending ping requests to {self.target_ip}...\n")
        for i in range(self.count):
            print(f"Ping {i+1}...")  # Display the current ping number
            self.send_ping()  # Call the method to send a ping
            time.sleep(1)  # Wait 1 second between pings
        
        print(f"\nTotal successful pings: {self.successful_pings}/{self.count}")  # Summary of results

def main():
    parser = argparse.ArgumentParser(description="PingChecker with Class")  # Set up the argument parser
    parser.add_argument("target_ip", help="The target IP address to ping")  # Mandatory argument: target IP
    parser.add_argument("-c", "--count", type=int, default=4, help="Number of ping requests to send")  # Optional argument: number of pings
    parser.add_argument("-t", "--timeout", type=int, default=2, help="Ping request timeout duration (seconds)")  # Optional argument: timeout

    args = parser.parse_args()  # Parse the arguments from the command line

    # Initialize the PingTool class with the command-line arguments and run the ping operations
    ping_tool = PingTool(target_ip=args.target_ip, count=args.count, timeout=args.timeout)
    ping_tool.run()

if __name__ == "__main__":
    main()
