# TwinCAT_TCP_IP_Server
This is a very simple test for TwinCAT TCP/IP Server with a Python TCP/IP client.

Components used:
CX5120 with TwinCAT TCP/IP installed (get TF6310 from https://www.beckhoff.com/english.asp?twincat/twincat_tcpip_server.htm)
EL2088 or other digital output card
TCP/IP client PC

![alt tag](https://puu.sh/rAjLc/58a5d20a95.png)

Since TwinCAT running in my CX5120 is the TwinCAT Runtime (XAR), the development of the code is in my TwinCAT Engineering (XAE) computer, with the CX5120 as the target computer.

The IP address of all computers are set as DHCP. That's why in the example, the IP address of the server is listed as '169.254.28.233'.

How to use:
1. Run the TwinCAT first
2. Run the client program
3. When it's connected, the terminal will print "PC connected", "out1 on", and "out2 on", and the LED light of the 2088 card will light up
