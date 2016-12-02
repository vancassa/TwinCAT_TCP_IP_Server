# TwinCAT_TCP_IP_Server
A function block for receiving and sending data using TF6310 TwinCAT TCP/IP Server. TwinCAT version used: v3.1.4020

## Usage

1. Install TF6310 TwinCAT TCP/IP Server from https://www.beckhoff.com/english.asp?twincat/twincat_tcpip_server.htm
2. Install Python3.
3. Run the TwinCAT program first.
4. Run the client Python program.
5. Send 'On1' to turn on bVar1, and 'On2' to turn on bVar2, otherwise to turn off both. TwinCAT will echo back all commands.

## How it works

What's happening inside the function block FB_TcpServer:

1. The function block FB_SocketConnect will open the socket at the specific port.
2. Python client will then need to connect to the host and the port. 
3. Every half a second (the timing can be changed), FB_SocketAccept will accept any incoming connection, and populate the variable 'hSocket' with the local address of the server and remote address of the client.
4. The function block FB_SocketSend and FB_SocketReceive use this 'hSocket' variable to send and receive data.


## State machine

![alt tag](https://puu.sh/sBxgh/a6d8de1c9a.png)

## Common errors

TwinCAT Error and Error ID are stored in the variable 'err' and 'errid' respectively. Some common errors found:

   * 8002 : Variable 'hSocket' is not populated with the correct address. The sequence is for the TwinCAT to call FB_SocketListen, the Python client to connect, and TwinCAT calls the FB_SocketAccept after that. This will populate the variable 'hSocket'. If FB_SocketAccept is called before the Python client trying to connect, it will throw 8002 error.
   * 8003 : The port is already opened. Reset Cold the TwinCAT program and Run again.  
   * 6 : I don't know. Seems like there's something wrong with the installation of TF6310. Uninstall, reinstall, make sure that TcpIpServer.exe is running in your Task Manager processes.
   
Python error:
   * Connection is refused: Make sure to disable the firewall of your server PC  
