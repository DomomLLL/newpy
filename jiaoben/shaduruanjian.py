import os
def main(path):
    total = os.listdir(path)
    for every_name in total:
        if os.path.isfile(every_name):
            with open(every_name) as every_content:
                for content in every_content:
                    if 'milomilomilo' in content:
                        print(every_name)
main('/mnt/share')
