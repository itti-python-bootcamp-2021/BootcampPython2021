import ftplib
import paramiko

FILE_NAME="subida_ficheros.py"

def subida_ftp():
    HOST_NAME="localhost"
    HOST_PORT=21
    USER_LOGIN="fpaniagua"
    USER_PASSWORD=""
    ftp = ftplib.FTP()
    response_connect = ftp.connect(host=HOST_NAME, port=HOST_PORT)#220 - OK
    print("Response connect:",response_connect)
    response_login = ftp.login(user=USER_LOGIN, passwd=USER_PASSWORD)
    print("Response login:",response_login)
    localfile=FILE_NAME
    remotefile=FILE_NAME
    with open(localfile, "rb") as file:
        ftp.storbinary('STOR %s' % remotefile, file)
        print("FICHERO SUBIDO CORRECTAMENTE")

#Utilizando el módulo paramiko 
#https://www.paramiko.org/
def subida_sftp():
    HOST_NAME="home426225617.1and1-data.host"
    HOST_PORT=22
    USER_LOGIN="u69909233-bc-python"
    USER_PASSWORD="bcPython2021@"

    transport = paramiko.Transport((HOST_NAME, HOST_PORT))
    transport.connect(username = USER_LOGIN, password = USER_PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(transport)

    localfile=FILE_NAME
    remotefile=FILE_NAME
    sftp.put(localfile, remotefile)
    sftp.close()
    transport.close()
    print("FICHERO SUBIDO CORRECTAMENTE")

if __name__ == '__main__':
    #subida_ftp()
    subida_sftp()
