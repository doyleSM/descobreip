import socket
import fcntl
import struct
import subprocess

def get_ip_address():
    proc = subprocess.Popen(["""route | grep '^default' | grep -o '[^ ]*$'"""], stdout=subprocess.PIPE, shell=True)
    interface = proc.communicate()[0]
    ifname = interface.decode('ascii').replace("\n","")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack("256s", (ifname[:15]).encode('utf-8'))
    )[20:24])


print(get_ip_address())
