import socket, sys

HOST = '127.0.0.1' # the local host
PORT = 6001 # The same port as used by the server
ADDR=(HOST,PORT)

class MayaTools:
    def SendCommand(self, command):
        command = "python(\"" + self.compressCommandToOneLine(command) + "\");"
        print command
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect(ADDR)
            client.send(command)
            client.close()
        except Exception, e:
            print >>sys.stderr,("Unable to connect to Maya: Exception type is %s. In Maya run following MEL command: commandPort -name \":6001\";" % (e))

    def compressCommandToOneLine(self, command):
        result = ""
        for line in command.split("\n"):
            if line.strip():
                if not line.strip().startswith('#'):
                    if line.find('#') != -1:
                        line = line[:line.index('#')].strip()
                    result += line + ";"
        return result
