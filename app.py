import pandas as pd
import matplotlib as plt
import networkx as nx
import pyshark
import socket


def scan_open_ports_on_lm():
    target = 'localhost'
    port = 22
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")


def pyshark_pcap_file_reader():
    pcap = pyshark.FileCapture(r'', display_filter='')
    for pkt in pcap:
        print(pkt.pretty_print())


def create_list_of_specific_fields_from_pcap():
    pcap = pyshark.FileCapture(r'')
    list_obj = [pkt.usb.src for pkt in pcap if "usb" in pkt and pkt.usb.has_field('src')]
    print(list_obj)


def obtain_network_traffic_with_pandas():
    cap = pyshark.FileCapture(r'', display_filter='')
    data = []
    for packet in cap:
        data.append({
            'source': packet.ip.src,
            'destination': packet.ip.dst,
            'protocol': packet.transport_layer,
            'length': packet.length
        })
    df = pd.DataFrame(data)
    print(df.head())
    print(df.groupby('protocol')['length'].sum())