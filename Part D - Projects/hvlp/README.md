## Project Setup

1. Checkout from http://server.hilscherdtc.local:81/svn/hilscherdtc_embedded/SVNPlayground/Education/bgeorgiev/hvlp_protocol

![img.png](assets/project_checkout.png)

2. Go to the project folder

![img.png](assets/project_folder.png)

3. Open a new console and type `python broker.py <IP ADDR> <PORT>` to start the broker. If omitted 
the default IP is 127.0.0.1 and the default port is 65432.

![img.png](assets/broker_start.png)

4. Open a new console and type `python client.py <SERVER ADDR> <PORT>` to start the client. If
omitted the default server address is 127.0.0.1 and the default port s 65432.

![img.png](assets/client_start.png)

5. Type `open' in the client console to open a TCP connection

6. Type `connect` in the client console to connect to the broker

![img.png](assets/connect.png)

7. Type `subscribe test` in the client console to subscribe to a topic

![img.png](assets/subscribe.png)

8. Repeat steps 4-6 to add a second client

![img.png](assets/two_clients.png)

9. Type publish test 1

![img.png](assets/publish.png)

10. Type `quit` in a client console to exit the program

1Type help in the client console for more commands

![img.png](assets/help.png)


 

