import re
rfun = r'''(?P<hostname>\S*).+\"\s(?P<dsda>\d+)\s(?P<daxiao>\d+)'''
with open('access_log') as f:
    hostname = []
    daxiao = []
    for i in f:
        q = re.match(rfun,'{}'.format(i))
        if q != None:
            w = q.groupdict()
        print(w)
        hostname.append(w['hostname'])
        daxiao.append(w['daxiao'])
    print(hostname)
    p = []
    for j in daxiao:
        o = int(j)
        p.append(o)
    print(sum(p))
