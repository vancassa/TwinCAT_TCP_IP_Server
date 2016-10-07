# TwinCAT_TCP_IP_Server
This is a very simple test for TwinCAT TCP/IP Server with a Python TCP/IP client.

Components used:

1. CX5120 with TwinCAT TCP/IP installed (get TF6310 from https://www.beckhoff.com/english.asp?twincat/twincat_tcpip_server.htm)
2. EL2088 or other digital output card
3. TCP/IP client PC with Python installed

![alt tag](https://puu.sh/rAjLc/58a5d20a95.png)

Since TwinCAT running in my CX5120 is the TwinCAT Runtime (XAR), the development of the code is in my TwinCAT Engineering (XAE) computer, with the CX5120 as the target computer.

The IP address of all computers are set as DHCP. That's why in the example, the IP address of the server is listed as '169.254.28.233'.

How to use:

1. Run the TwinCAT first
2. Run the client program
3. When it's connected, the terminal will print "PC connected", "out1 on", and "out2 on", and the LED light of the 2088 card will light up

# How it works

What's happening inside the program:

1. The function block FB_SocketConnect will open the socket at the specific port.
2. When the Python client is run, it will connect to the socket and return "connected" in the terminal.
3. Every half a second (the timing can be changed), FB_SocketAccept will accept any incoming connection, and populate the variable 'hSocket' with the local address of the server and remote address of the client.
4. The function block FB_SocketSend and FB_SocketReceive use this 'hSocket' variable to send and receive data.


# Common errors

TwinCAT Error and Error ID are stored in the variable 'err' and 'errid' respectively. Some common errors found:

   * 8002 : Variable 'hSocket' is not populated with the correct address. The client should connect first, and TwinCAT calls the FB_SocketAccept after that. This will populate the variable 'hSocket'.
   * 8003 : The port is already opened. Reset Cold the program and Run again.  
   * 6 : I don't know. Seems like there's something wrong with the installation of TF6310.  
   
Python error:
   * Connection is refused: Make sure to disable the firewall of your server PC  
