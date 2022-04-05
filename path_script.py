import os


def mkdir_and_ingore_exist(path):
    if os.path.exist(path):
        return True
    try:
        os.mkdir(path)
    except:
        return False
