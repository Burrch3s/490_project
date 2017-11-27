#!/usr/bin/python3

import sys
import socket
import threading
import subprocess

#TODO: fix lame broad try/excepts
#TODO: send stuff until ctrl-c then close connection

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
            # print("connected")
            send_stuff = True
            while send_stuff:
                if len(buf):
                    buf += '\n'
                    print("theres length here")
                    client.send(buf.encode())

                    if 'quit' in buf:
                        send_stuff = False
                        client.close()
                        print('[*] Client quit the session!!')
                        sys.exit(0)

                else:
                    send_stuff = False
                    client.close()
                    print('[*] Client quit the session!')
                    sys.exit(0)

                # buf = raw_input()
                send_stuff = False
                return

        except Exception as e: 
            print(e)
            # add better error handling?
            client.close()
            print('[*] Exception! Exiting')
            sys.exit(0)

    def _server_loop(self, target=None, port=None):
        if not len(target):
            target = '0.0.0.0'

        global server
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((target,port))
        server.listen(5)
        loop = True

        while loop:
            client_socket, addr = server.accept()

            if client_socket:
                self._client_handler(client_socket)
            # self._client_handler(client_socket)
            # client_socket.close()
            # loop = False

        client_socket.close()
        sys.exit(9)
    def _client_handler(self, client_socket=None):
        loop = True

        while loop:
            try:
                cmd_buffer = ''
                while '\n' not in cmd_buffer:
                    cmd_buffer += client_socket.recv(4096)

                    # if 'quit' in cmd_buffer:
                    #     client_socket.close()
                    #     print('[*] Client closed session!!')
                    #     sys.exit(0)
                    #
                    # else:
                    if cmd_buffer:
                        response = self._run_command(cmd_buffer)

                    else:
                        return
                    # client_socket.close()
                    # loop = False

            except Exception as e:
                print(e)
                print('[*] Session ended, exiting now')
                loop = False
                client_socket.close()
                sys.exit(0)

            loop = False
            return

    def _run_command(self, command=None):
        command = command.rstrip()
        print(command)
        try:
            #output = call([str(command)])
            pid = subprocess.call(str(command), shell=True)
            print pid

        except Exception as e:
            print(e)
            output = "Failed to execute command\n"
            return output

        return


    def netcat(self, target=None, port=None, listen=False, buf=None):
        if (not port):
            self.usage(cls='err')

        if not listen and len(target) and port > 0 and buf:
            self._client_sender(target, port, buf)

        if listen:
            self._server_loop(target, port)

        return 0
        # self.usage(cls='err')
