

### subnet calculator ###
##########################################################
#               TITLE : SUBNET CALCULAOTR                #
#               AUTHOR : DURGA                           #
#               DATE  : 19-NOV-2012                      #
#               VERSION : 1.1v                           #
#               UPDATED on 22-APR-2013 frv3.3            #
##########################################################


def getuserIP():
  prefixLength = 0
  #ip = raw_input("enter IP address:")
  ip = input("enter IP address:")
  ipNew = ip.split('.')
  for i in range(len(ipNew)):
    if ipNew[i].isdigit() == False:
      print ("sorry Ips are numeric ??? Please enter valid IP")
      getuserIP()
    else:
      ipNew[i]= int(ipNew[i])
      if len(ipNew) < 4:
        print ("dude! IP add is 4 octets, enter complete IP")
        getuserIP()
      elif ipNew[i] > 255 or ipNew[i] < 0:
        print ("are you sure internet can accomodate that IP??? Please enter valid IP")
        getuserIP()
      else:
        continue

  while prefixLength < 32:
    print ("please enter prefix lenght less or equal to 32 bits")
    #prefixLength = int(raw_input("enter prefix-lenght(as in /x notation:"))
    prefixLength = int(input("enter prefix-lenght(as in /x notation:"))
    if prefixLength > 32:
      prefixLength = 0
      continue
    else:
      break

  return ipNew , prefixLength

def maskCal(mask):
  sub = []
  parOctet = int(('1' * (mask % 8)).ljust(8,'0'),2) # for the incomplete octet, put 1s and then padd with 0 for rest of characters
  for j in range(mask//8):
    sub.append(255) # 255 for each full octet
  if len(sub)< 4:
    sub.append(parOctet)
  while len(sub) < 4:
    sub.append(0)
  return sub

def networkSubnet(ip, mask):
  networkIP =[]
  for i in range(len(ip)):
    networkIP.append(ip[i] & mask[i])
  return networkIP

def hostRange(networkID,mask):
  wildCard = []
  firstHost = []
  broadCast = []
  lastHost = []
  for j in networkID:
    firstHost.append(j)
  for i in mask:
    wildCard.append(255-i)
  for k in range(len(networkID)):
    broadCast.append(networkID[k] + wildCard[k])
    lastHost.append(broadCast[k])
  firstHost[3] =+ 1
  lastHost[3] =lastHost[3]- 1
  return firstHost,lastHost,broadCast

def formatOutput(ip,Mask,NetworkIP,firstHost,lastHost,broadCast):
  for a in range(len(ip)):
    ip[a] = str(ip[a])
    Mask[a] = str(Mask[a])
    NetworkIP[a] = str(NetworkIP[a])
    firstHost[a] = str(firstHost[a])
    lastHost[a] = str(lastHost[a])
    broadCast[a] = str(broadCast[a])
  finalIP = '.'.join(ip)
  finalMask = '.'.join(Mask)
  finalNetworkIP = '.'.join(NetworkIP)
  finalfirstHost = '.'.join(firstHost)
  finallastHost = '.'.join(lastHost)
  finalbroadCast = '.'.join(broadCast)

  return finalIP,finalMask,finalNetworkIP,finalfirstHost,finallastHost,finalbroadCast


## main block ##
ip,mask = getuserIP()
Mask = maskCal(mask)
NetworkIP = networkSubnet(ip,Mask)
firstHost,lastHost,broadCast = hostRange(NetworkIP,Mask)
finalIP,finalMask,finalNetworkIP,finalfirstHost,finallastHost,finalbroadCast = formatOutput(ip,Mask,NetworkIP,firstHost,lastHost,broadCast)

print (" ******************************************* ")
print ("IP as entered by you " + (finalIP))
print ("mask:" + (finalMask))
print ("network IP:" + (finalNetworkIP))
print ("first host IP:" + (finalfirstHost))
print ("last host IP:" + (finallastHost))
print ("Broadcast IP:" + (finalbroadCast))
print ("number of hosts:" + str(2 ** (32-mask)-2))

