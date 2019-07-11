
import os

def disk_usage(path):
    '''
    返回输入path的文件夹大小
    '''
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):       #构成所有子文件夹
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)

    print('{0:<7}'.format(total), path)
    return total

path = os.path.abspath('D:\python')
disk_usage(path)