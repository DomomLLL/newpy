import pymysql
class MySql():
    def __init__(self, host = 'localhost', user = 'root', passwd = '',db = 'itcast'):
        self.coon = pymysql.connect(host = host,
                               user = user,
                               password = passwd,
                               db = db)
        self.cur = self.coon.cursor()
    def i(self, sid, sname, cid):
        self.cur.execute("insert into student values({},'{}',{})".format(sid,sname,cid))
        self.coon.commit()
    
    def d(self,sid):
        self.cur.execute("delete from student where sid=%d;"%(sid))
        self.coon.commit()
    def u(self, x, y):
        self.cur.execute("update student set cid=%d where sname ='%s';"%(x,y))
        self.coon.commit()
    def __del__(self):
        self.cur.close()
        self.coon.close()
    def s(self):
        a = self.cur.fetchone()
        return a
u = MySql()
u.d(11)


