#!/usr/bin/env python
import subprocess
import time
def main():
	port_table = {}
	blocked_mac= []
	config_file = "l3firewall.config"
	command = "ovs-ofctl dump-flows s1"
	while (True):
		process = subprocess.Popen("ovs-ofctl dump-flows s1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		result,error = process.communicate()
		info = result.split('\n')[1:]
		for packet in info:
			if "dl_src=" in packet and "nw_src=" in packet:
				mac = packet.split('dl_src=')[1].split(',')[0]
				ip = packet.split('nw_src=')[1].split(',')[0]
				if port_table.get(mac,None) is None:
					port_table[mac] = [ip]
				elif port_table.get(mac) is not ip:
					if mac in blocked_mac:
						continue
					else:
						print("--------------------------------------------")
					
						print("Write to config")
						#f = open("/home/vboxuser/pox/l3firewall.config", "a")
						q = open("/home/vboxuser/pox/l2firewall.config", "a")
						q.write("1," + mac + ",any\n")
						
						#f.write("1," + mac + ",any,any,any,any,any,any\n")
						#f.flush()
						q.flush()
						blocked_mac.append(mac)


if __name__ == "__main__":
	main()
