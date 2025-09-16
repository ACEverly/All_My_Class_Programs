#Mary-Rose Tracy
#ID#:1001852753
#Professor Dr. Yonghe Liu
#CSE 4344-001-Computer Network Organization- Project 1
import mimetypes
import os
import socket
import threading
# Unique Web Server Configuration, testing local host, need port selection 8080, & files are stored 
WEB_DIRECTORY = './webroot'
SERVER_PORT = 8080
SERVER_HOST = '127.0.0.1'
# Ensure web directory exists
if not os.path.exists(WEB_DIRECTORY):
    os.makedirs(WEB_DIRECTORY)
index_html=os.path.join(WEB_DIRECTORY, "index.html") #Let's do the index.html pg
if not os.path.exists(index_html):
    with open(index_html,"w")as f:
        f.write("""
        <html>
        <head>
        <title>Welcome to the Internet Wonderland of Mary-Rose Tracy</title>
        <style>
            body { background-color: lightblue; font-family: Arial, sans-serif; }
            h1 { color: darkblue; }
        </style>
        </head>
        <body>
        <h1>Welcome to the Internet Wonderland of Mary-Rose Tracy</h1>
        
        <img src='imageMe.jpg' width='300'>
        <h2>Breaking: Scientists Discover the True Cure for All Diseases.</h2>
        <a href='https://www.youtube.com/watch?v=cpwKaIvzBT0' target='_blank'>
            <img src='misleadingpic.jpg' width='300'>
        </a>
        </body>
        </html>
        """)
error_404_html=os.path.join(WEB_DIRECTORY,"404.html") #get 404 error pg
if not os.path.exists(error_404_html):
    with open(error_404_html,"w")as f:
        f.write("""
        <html>
        <head>
        <title>404 - Oops, You Broke the Internet</title>
        <style>
            body { background-color: lightpink; font-family: 'Comic Sans MS', cursive, sans-serif; font-family: Arial, sans-serif; }
            h1 { color: red; }
        </style>
        </head>
        <body>
        <h1>Oops! You Have Ventured Into the Dark Void</h1>
        <p>This page is lost, just like your socks in the laundry. Try going back!</p><img src='travy.gif' width='300'>
        </body>
        </html>
        """)
# Generate an amusing page2.html
page2_html=os.path.join(WEB_DIRECTORY,"page2.html")
if not os.path.exists(page2_html):
    with open(page2_html,"w")as f:
        f.write("""
        <html>
        <head>
        <title>Welcome to Link's Secret Hideout - Page 2</title>
        <style>
            body { background-color: lightgreen; font-family: Comic Sans MS, cursive, sans-serif; font-family: Arial, sans-serif; }
        </style>
        </head>
        <body>
        <h1>Welcome to Page 2 - The Sequel Nobody Expected</h1>
        <p>Welcome, hero! You have discovered the legendary Link's secret hideout.</p><a href='https://www.youtube.com/watch?v=FPxY8lpYAUM' target='_blank'><img src='link1.jpg' width='400'></a>
        </body>
        </html>
        """)
def process_client_request(client_socket):
    #The digital gatekeeper: Takes client requests, serves files, redirects secrets, and hands out 404s like a bouncer at an exclusive club.
    try:
        request=client_socket.recv(2048).decode('utf-8')
        print(f"Incoming Request:\n{request}")
        if not request:
            client_socket.close()
            return
        request_line=request.split('\n')[0]
        requested_file=request_line.split()[1] if len(request_line.split()) > 1 else '/'
        if requested_file=='/':
            requested_file='/index.html'
        if requested_file=='/secret.html': #DO THE EASTER EGG/SECRET
            response="HTTP/1.1 301 Moved Permanently\r\n"
            response+="Location: /page2.html\r\n\r\n"
            client_socket.send(response.encode())
            client_socket.close()
            return
        file_path=WEB_DIRECTORY+requested_file
        if os.path.exists(file_path):
            with open(file_path,'rb')as f:
                content=f.read()
            content_type, _=mimetypes.guess_type(file_path)
            content_type=content_type if content_type else "application/octet-stream"
            response= f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\nContent-Length: {len(content)}\r\n\r\n"
            client_socket.send(response.encode()+content)
        else:
            with open(error_404_html, 'rb')as f: #error 404 pg
                content=f.read()
            response="HTTP/1.1 404 Not Found\r\n"
            response+="Content-Length: " + str(len(content)) + "\r\n\r\n"
            client_socket.send(response.encode() + content)
    except Exception as e:
        print(f"Request handling error: {e}")
    finally:
        client_socket.close()
def launch_server(): #Spinning up a web server that juggles multiple visitors like a circus act – no delays, no waiting!
    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    #accepts 8 connections 
    server_socket.listen(8)
    print(f"Web server is active at http://{SERVER_HOST}:{SERVER_PORT}")
    while True:
        client_socket, addr = server_socket.accept()
        print(f"New visitor from {addr}")
        threading.Thread(target=process_client_request,args=(client_socket,)).start()
if __name__ == "__main__":
    launch_server()
# This project was developed with the help of various online 
# resources that provided insights into Python networking, 
# HTTP status codes, and web development basics.
# Python Socket Programming:
# https://docs.python.org/3/library/socket.html
# - Used to establish server-client communication and handle 
#   HTTP requests over TCP connections.
# HTTP Status Codes:
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# - Helped in understanding how to correctly implement 
#   HTTP responses like 200 OK, 301 Redirect, and 404 Not Found.
# W3Schools HTML Basics:
# https://www.w3schools.com/html/html_basic.asp
# - Used as a reference for structuring the HTML pages 
#   served by the web server.
# https://www.youtube.com/watch?v=byL8VMEMC0M
# - tutorial on how to use wireshark