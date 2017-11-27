#!/usr/bin/python3

import sys
import socket
import threading
import subprocess


class Netcat:
    def __init__(self, listener=False, target=None, port=None):
        self.listener = listener
        self.target = target or ''
        self.port = port

    @staticmethod
    def usage(cls):
        print(
        ''' 
        Usage: basic-netcat.py -t taget_host -p port
        -l --listen -listen on [host]:[port] for incoming connection
        -c initialize a command shell
        examples:
        basic-netcat.py -t 1.1.1.1 -p 55 -l -c
        basic-netcat.py -t 1.1.1.1 -p 55 -l
        echo \'abcdef\' | ./basic-netcat.py -t 1.1.1.1 -p 55
        '''
        )
        sys.exit(0)

    def _client_sender(self, target=None, port=None, buf=None):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((target,port))
            print("connected")
            send_stuff = True
            while send_stuff:
                if len(buf):
                    buf += '\n'
                    print("theres length here")
                    client.send(buf.encode())
                    client.close()
                    send_stuff = False

                else:
                    client.close()
                    # sys.exit(0)

        except:
            # add better error handling?
            client.close()
            print('[*] Exception! Exiting')
            sys.exit(0)

    def _server_loop(self, target=None, port=None):
        if not len(target):
            target = '127.0.0.1'

        global server
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((target,port))
        server.listen(5)
        loop = True

        while loop:
            client_socket, addr = server.accept()
            self._client_handler(client_socket)
            client_socket.close()
            loop = False

        client_socket.close()
        sys.exit(9)
    def _client_handler(self, client_socket=None):
    loop = True

        while loop:
            try:
                cmd_buffer = ''
                while '\n' not in cmd_buffer:
                    cmd_buffer += client_socket.recv(4096)
                    response = self._run_command(cmd_buffer)
                    client_socket.close()
                    loop = False

            except:
                print('[*] Session ended, exiting now')
                loop = False

    def _run_command(self, command=None):
        command = command.rstrip()
        print(command)
        try:
            #output = call([str(command)])
            pid = subprocess.call(str(command), shell=True)
            print pid

        except:
            output = "Failed to execute command\n"

        return output

    def netcat(self, target=None, port=None, listen=False, buf=None):
        if (not target) | (not port):
            self.usage(cls='err')

        if not listen and len(target) and port > 0 and buf:
            self._client_sender(target, port, buf)

        if listen:
            self._server_loop(target, port)

        self.usage(cls='err')
