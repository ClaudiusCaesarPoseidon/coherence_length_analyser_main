import os
import sys
os.environ['path'] += os.pathsep + \
    os.path.abspath(os.path.join(".", "binaries"))
from coherence_length_analyser.lib import main_init
main_init.main_init()
from coherence_length_analyser.lib import functions
from coherence_length_analyser.modules.eigen_widgets import screen_size_dialog
from coherence_length_analyser.modules.eigen_widgets import Command_Line_Arguments
from coherence_length_analyser.modules.master import Master
from screeninfo import get_monitors
from distutils.util import strtobool as s2b
import argparse
from PySide2 import QtCore, QtWidgets, QtGui

VAL = functions.VAL
#white 55

h_size = get_monitors()[0].height
v_size = get_monitors()[0].width


class ScreenSizeError(RuntimeError):
    """Error raise if screen size is to small"""


def strtobool(string):
    return bool(s2b(string))


def main():
    global window
    global app
    app = QtWidgets.QApplication(sys.argv)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-win",
        "--windowed",
        help="show the program in windowed mode",
        action="store_true")
    parser.add_argument(
        "-b",
        "--borderless",
        help="show the program in borderless mode. Always True if windowed is False",
        action="store_true")
    parser.add_argument(
        "-min",
        "--minimised",
        help="do not show the program in fullscreen mode. Always False if borderless is True",
        action="store_true")
    parser.add_argument(
        "-ipy",
        "--ipython",
        help="shows the ipython console",
        action="store_true")
    parser.add_argument(
        "-con",
        "--console",
        help="shows the command line arguments console",
        action="store_true")
    parser.add_argument(
        "-set",
        "--settings",
        help="usese the saved settings and discards other arguments" +
             "saves arguments if False",
        action="store_true")
    args = parser.parse_args()
    if h_size < 800 or v_size < 1280:
        raise ScreenSizeError
    app.aboutToQuit.connect(app.deleteLater)
    app.setWindowIcon(
        QtGui.QIcon(
            functions.resource_path(
                os.path.join(
                    'data',
                    'window_icon.png'))))
    if 'idlelib.rpc' in sys.modules or args.console is True\
       and args.settings is False:
        windowed = False
        border = True
        fullscreen = True
        ipython = False
        dialog = Command_Line_Arguments()
        dialog.show()
        dialog.exec_()
        sys.argv.extend(dialog.text_list)
    args = parser.parse_args()
    border = not args.borderless
    windowed = args.windowed
    fullscreen = not args.minimised
    ipython = args.ipython
    tmp = {'border': border,
           'windowed': windowed,
           'fullscreen': fullscreen,
           'ipython': ipython}
    tmp = VAL(**tmp)
    temp_list = []
    for item in tmp.__dict__:
        temp_list.append('\t'.join([item, str(tmp.get(item))]))
    string = '\n'.join(temp_list)
    settings_path = os.path.join(os.path.expanduser("~"), "OUT",
                                 "coherence_length_analyser", "settings.cfg")
    try:
        with open(settings_path, "r+") as file:
            if args.settings is False:
                file.seek(0)
                file.write(string)
            else:
                if os.path.getsize(settings_path) == 0:
                    file.seek(0)
                    file.write(string)
                    file.seek(0)
                tmp = file.read()
                tmp = tmp.split('\n')
                tmp = [x.split('\t') for x in tmp]
                tmp = {k[0]: k[1] for k in tmp}
                tmp = VAL(**tmp)
                border = strtobool(tmp.border)
                windowed = strtobool(tmp.windowed)
                fullscreen = strtobool(tmp.fullscreen)
                ipython = strtobool(tmp.ipython)
    except FileNotFoundError:
        with open(settings_path, "w") as file:
            file.write(string)
    configured = {}
    configured['windowed'] = int(windowed)
    configured['border'] = int(border)
    configured['fullscreen'] = int(fullscreen)
    configured['ipython'] = ipython
    screen_rect = app.desktop().screenGeometry()
    width, height = screen_rect.width(), screen_rect.height()
    window = Master(configured)
    window.win_width, window.win_height = width, height
    window.raise_()
    if bool(configured['windowed']) is False:
        window.showFullScreen()
    else:
        if bool(configured['border']) is False:
            window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        if bool(configured['fullscreen']) is True:
            window.showMaximized()
        else:
            window.resize(int(window.win_width * 3 / 4),
                          int(window.win_height * 3 / 4))
            window.show()


if __name__ == '__main__':
    try:
        main()
    except ScreenSizeError:
        dialog = screen_size_dialog()
        dialog.show()
        dialog.exec_()
    finally:
        app.exec_()
