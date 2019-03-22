# -*- mode: python -*-

import sys
sys.setrecursionlimit(50000)

block_cipher = None

added_files = [
         ('.\\ui\\master.ui', 'ui' ),
         ('.\\ui\\fft_peak_analyser.ui', 'ui' ),
         ('.\\ui\\Picture_Video_Convert.ui', 'ui' ),
         ('.\\ui\\new_camera.ui', 'ui' ),
#         ('.\\ui\\register.ui', 'ui' ),
         ('.\\ui\\dialog.ui', 'ui' ),
         ('.\\ui\\Command_Line_Arguments.ui', 'ui' ),
#         ('.\\ui\\check_fft.ui', 'ui' ),
         ('.\\ui\\angle.ui', 'ui' ),
         ('.\\ui\\turn.ui', 'ui' ),
         ('.\\ui\\screen_size_dialog.ui', 'ui' ),
         ('.\\data\\demo_35_25_100_9.0909090909090909.avi', 'data' ),
         ('.\\data\\demi_35_25_100_9.0909090909090909.avi', 'data' ),
         ('.\\data\\window_icon.png', 'data' ),
#         ('.\\data\\ffmpeg_python', 'data\\ffmpeg_python'),
#         ('.\\data\\ffmpeg.exe', 'data' ),
#         ('C:\\Users\\Haarmeyer\\Desktop\\coherence_length_analyser\\dlls\\ueye_api.dll', 'dlls' ),
#         ('C:\\Users\\Haarmeyer\\Desktop\\coherence_length_analyser\\dlls\\ueye_api_64.dll', 'dlls' ),
#         ('C:\\Users\\Haarmeyer\\Desktop\\coherence_length_analyser\\dlls\\MediaInfo_i386.dll', 'dlls' ),
#         ('C:\\Users\\Haarmeyer\\Desktop\\coherence_length_analyser\\dlls\\MediaInfo.dll', 'dlls' ),
         ]


icon=".\\data\\window_icon.ico"
binaries=[
         (".\\binaries","."),
         ]

a = Analysis(['main.py'],
             pathex=['C:\\Users\\Haarmeyer\\Desktop\\coherence_length_analyser'],
             binaries=binaries,
             datas=added_files,
             hiddenimports=['numpy.core._dtype_ctypes','PySide2.QtXml'],#'PySide2.QtXml',
             hookspath=[".\\hooks\\"],
             runtime_hooks=[],
             excludes=['PyQt5'],#'PySide2'
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False
             )
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          icon=icon )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=['qwindows.dll','qwindowsvistastyle.dll'],
               name='main')
