# a traceroute program
# send a ICMP packet with incremental TTL value, till the destination is reached
# 1.send set of ICMP packets with varying TTL values from 4 to 32
# 2.store the answeres in trcrt list
# 3.if dstip == icmp respose IP . exit loop else append the sr return value to trcrt

from scapy.all import *

icmppkt = IP()/ICMP()/"X"
icmppkt[IP].dst = 'www.google.com'
icmppkt[IP].src = '192.168.56.101' # whatever is the source
icmppkt[IP].ttl = (4,30) # create multiple packets with different TTLs
# the icmppkt is a pack of pkts with ttl =4 to 30. They need to be unpacked

ans,unans = sr(icmppkt)

trcrt = []
#ans is a list to which sendpkt , response are appened fot each packet send
for snd,rcv in ans: 
	if rcv.src == icmppkt[IP].dst:
		break
	else:
		trcrt.append((snd.ttl,rcv.src))

for node in trcrt:
	print node[0],node[1]
