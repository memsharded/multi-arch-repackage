import os

def run(command):
    ret = os.system(command)
    if ret != 0:
        raise Exception("Error in: %s" % command)

run("conan create driver user/testing -s arch=x86")
run("conan create driver user/testing -s arch=x86_64")

run("conan create installer user/testing -s arch=x86")
run("conan create installer user/testing -s arch=x86_64")