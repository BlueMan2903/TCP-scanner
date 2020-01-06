import argparse
import socket

parser = argparse.ArgumentParser(description="Homemade TCP port scanner")

parser.add_argument("host", help="The host IP address")
parser.add_argument("-p", "--ports", help="The port numbers to be scanned.  Enter a comma separated list.")

args = parser.parse_args()

 #AF_INET = IPv4;  SOCK_STREAM = TCP

if __name__ == '__main__':  #if the program is ran as the main program and not imported as a library
    ports = args.ports.split(",")
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((args.host, int(port)))
            print("port {}/tcp is OPEN.".format(port), end="\t\t")
            if port == "80":
                s.send(b"HEAD / HTTP/1.0\r\n\r\n")
                output = str(s.recv(85))
                #print("HTTP " + output[60:].strip("\\rn'"))
                print(output.strip("bc'rn\\"))
            else:
                output = str(s.recv(85))
                print(output.strip("b'nr\\"))
            s.close()
        except Exception as e:
            if str(e) == "timed out":
                print("port {}/tcp is filtered:\tTimed Out".format(port))
            else:
                print("port {}/tcp is closed:\t\t".format(port) + str(e).strip("Errno[]1234567890 "))
