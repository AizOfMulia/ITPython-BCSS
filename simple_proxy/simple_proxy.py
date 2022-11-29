import socket
import threading

def main () -> None:
    PORT : int          =   55555
    BUFFER_SIZE : int   =   4096
    TARGET_ADDR : str   =   ""
    TARGET_PORT : int   =   80

    # Create a socket for the proxy server
    with socket.socket (socket.AF_INET, socket.SOCK_STREAM) as server:

        # Escape the "address already in use error" and allowing address to be freed and reuse.
        server.setsockopt (socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Bind the socket to localhost and proxy port
        server.bind (('', PORT))
        
        # Listen to incoming connection request
        server.listen (1)

        # Hack method: Using only one socket listener generate multiple connection with single listener via
        # offloading connection to other threads
        while True:

            # accept incoming connection request
            conn, addr  =   server.accept()

            print (f"[Proxy-conn] Connection established -> {addr}")
            data        =   conn.recv (BUFFER_SIZE)

            # Check if the connection is an empty connection
            if not data:
                break

            print (f"[Proxy-data] received -> {data}")

            # Offload the connection information to proxy forwarder via threading
            forwarding  =   threading.Thread (target=proxy_forwarder,
                                              args=(conn, data, TARGET_ADDR, TARGET_PORT, BUFFER_SIZE))

            # Start the threads
            forwarding.start()

def proxy_forwarder (connection ,
                     data : bytes,
                     TARGET_ADDR : str,
                     TARGET_PORT : int,
                     BUFFER_SIZE : int) -> None:

    # Create a socket for the proxy forwarder that will forward the connection and data to the target server
    with socket.socket (socket.AF_INET, socket.SOCK_STREAM) as forward:

        # Send a connect request to the target server
        forward.connect((TARGET_ADDR, TARGET_PORT))

        # Forward the data received from the proxy server to the target server
        forward.send (data)

        # Get the reply from the target server
        reply   =   forward.recv (BUFFER_SIZE)

        # Check if the target server is sending any empty replies to terminate connection
        if len(reply) <= 0:
            return

        print (f"[Proxy-Reply] received -> {reply}")

        # Forward the reply from the target server to the proxy server to display to user
        connection.send (reply)

if __name__ == "__main__":
    main ()
