from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

def main():
    interface = input("Enter the network interface to sniff packets from (e.g., Ethernet, Wi-Fi): ")
    duration = int(input("Enter the duration (in seconds) to sniff packets: "))
    sniff(iface=interface, prn=packet_callback, timeout=duration)
    print("Packet capture complete.")

if __name__ == "__main__":
    main()
