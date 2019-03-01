import os
import sys

# adds the the path of the binaries to PATH
os.environ['path'] += os.pathsep + \
    os.path.abspath(os.path.join(".", "binaries"))
from coherence_length_analyser.lib import main_init

# sets some values needed for the programm
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
h_size = get_monitors()[0].height
v_size = get_monitors()[0].width


class ScreenSizeError(RuntimeError):
    """Error raise if screen size is to small"""


def strtobool(string):
    """Converts a string to Truth value if possible, else raises error"""
    if string == "True":
        return bool(s2b(string))
    elif string == "False":
        return bool(s2b(string))
    else:
        raise ValueError("Invalid Input")


def main():
    global window
    global programm
    programm = QtWidgets.QApplication(sys.argv)

    # raises error if screen is to small
    if h_size < 800 or v_size < 1280:
        raise ScreenSizeError

    # adds command line arguments
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

    # sets the taskbar icon and makes shure the programm is closed
    programm.aboutToQuit.connect(programm.deleteLater)
    programm.setWindowIcon(
        QtGui.QIcon(
            functions.resource_path(
                os.path.join(
                    'data',
                    'window_icon.png'))))

    # sets the command line arguments through a dialog
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

    # parses sys.argv according to the command line arguments
    args = parser.parse_args()
    border = not args.borderless
    windowed = args.windowed
    fullscreen = not args.minimised
    ipython = args.ipython

    # converts the command line arguments to a class
    tmp = {'border': border,
           'windowed': windowed,
           'fullscreen': fullscreen,
           'ipython': ipython}
    tmp = VAL(**tmp)

    # converts the command line arguments class to string for writing to file
    temp_list = []
    for item in tmp.__dict__:
        temp_list.append('\t'.join([item, str(tmp.get(item))]))
    string = '\n'.join(temp_list)

    # writes the arguemts to file or reads the content of the file according
    # to the settings command line argument
    settings_path = os.path.join(os.path.expanduser("~"), "OUT",
                                 "coherence_length_analyser", "settings.cfg")
    try:
        # opens the settings file
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
        # creates the settings file if it does not exist
        with open(settings_path, "w") as file:
            file.write(string)

    # create a dictonary from the settings
    configured = VAL()
    configured['windowed'] = windowed
    configured['border'] = border
    configured['fullscreen'] = fullscreen
    configured['ipython'] = ipython

    # sets the geometry of the programm
    screen_rect = programm.desktop().screenGeometry()
    width, height = screen_rect.width(), screen_rect.height()
    window = Master(configured)
    window.win_width, window.win_height = width, height
    window.raise_()
    # shows the programm according to the settings
    if configured['windowed'] is False:
        window.showFullScreen()
    else:
        if configured['border'] is False:
            window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        if configured['fullscreen'] is True:
            window.showMaximized()
        else:
            window.resize(int(window.win_width * 3 / 4),
                          int(window.win_height * 3 / 4))
            window.show()


if __name__ == '__main__':
    try:
        # execute main
        main()
    except ScreenSizeError:
        # except when screen is to small
        dialog = screen_size_dialog()
        dialog.show()
        dialog.exec_()
    finally:
        # always execute the programm
        programm.exec_()
