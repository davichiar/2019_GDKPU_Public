import socket
 
HOST = '192.168.0.8'
PORT = 9009
 
def getFileFromServer(filename):
    data_transferred = 0
 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST,PORT))
        sock.sendall(filename.encode())
 
        data = sock.recv(1024)
        if not data:
            return
 
        with open('download/' + filename, 'wb') as f:
            try:
                while  data:
                    f.write(data)
                    data_transferred += len(data)
                    data = sock.recv(1024)
            except Exception as e:
                print(e)
 
    print('파일[%s] 전송종료. 전송량 [%d]' %(filename, data_transferred))
 
filename = input('다운로드 받은 파일이름을 입력하세요:')
getFileFromServer(filename)
