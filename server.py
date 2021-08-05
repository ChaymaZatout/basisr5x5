import configparser
import pickle
import socket
from queue import Queue
from threading import Thread

CONFIG_PATH = "server.ini"
MAX_BUFFER_SIZE = 64


class Server:
    def __init__(self, queue: Queue):
        config = configparser.ConfigParser()
        config.read(CONFIG_PATH)
        self.__host = config["DEFAULT"]["HOST"]
        self.__port = int(config["DEFAULT"]["PORT"])
        self.socket_ = socket.socket()
        self.socket_.bind((self.__host, self.__port))
        self.client_ = None
        self.queue = queue
        self.status = False
        self.thread = Thread(target=self.__start_server_callback, daemon=True)

    def __read_data(self):
        buffer = b''
        while True:

            response = self.client_.recv(MAX_BUFFER_SIZE)
            if len(response) == 0:
                buffer = b''
                self.status = False
                break
            buffer += response
            if len(response) < MAX_BUFFER_SIZE or response.endswith(b'.'):
                break
        return buffer

    def __start_server_callback(self):
        # wait for a connection and accept the first connection attempt
        while True:
            if not self.status:
                print('listening')
                self.__listen()
                print('accepted')

            buffer = self.__read_data()
            if len(buffer) == 0:
                continue
            self.fill_queue(buffer)

        print("Close")
        self.client_.close()
        self.socket_.close()

    def fill_queue(self, buffer):
        for data in buffer.split(b'.'):
            try:
                if len(data) > 0:
                    self.queue.put(pickle.loads(data + b'.'))
            except Exception as e:
                print(e)

    def __listen(self):
        self.socket_.listen()
        self.client_, _ = self.socket_.accept()
        self.status = True

    def start_server(self):
        self.thread.start()
