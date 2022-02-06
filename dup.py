import subprocess as sbp
import pip

class DAP:
    def __init__(self) -> None:
        self.__update_py_pkg()

    def __update_py_pkg(self):
        pkgs = eval(str(sbp.run("pip3 list -o --format=json", shell=True,
                         stdout=sbp.PIPE).stdout, encoding='utf-8'))
        for pkg in pkgs:
            sbp.run("pip3 install --upgrade " + pkg['name'], shell=True)

if __name__ == '__main__':
    DAP()