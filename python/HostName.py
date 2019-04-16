#Program to get the name of the host on which the routine is running.

import  socket
hostName = socket.gethostname()
print("Host name is= ", hostName)


