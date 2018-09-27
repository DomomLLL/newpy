def main():
    list = {}
    with open('/etc/passwd') as total:
        lines = total.readlines()
        for i in lines: 
            line = i.split(':')
            list_ = {'username': line[0],'homedir': line[5], 'shell': line[6]}
            print(list_)
main()
