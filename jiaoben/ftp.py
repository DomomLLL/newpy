from ftplib import FTP
ftp = FTP('172.25.2.203') 
ftp.login()
def ls():
    return ftp.retrlines('LIST')  
def Get(filename):
    comm = "RETR " + '{}'.format(filename)
    ftp.retrbinary(comm, open('{}'.format(filename),'wb').write)
def Set(path,filename):
    comm = "STOR " + '{}'.format(path)
    ftp.storbinary(comm,open('{}'.format(filename),'rb'))
Set('08-url-socket','qsbk.py')
