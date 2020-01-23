# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['..\\CallClientWin.py'],
             pathex=['ChatRoomClient.py', 'chatroomclient01.py', 'chatroomclient02.py', 'creatroom.py', 'E:\\python practice\\PyInstaller-3.5\\PyInstaller-3.5\\CallClientWin'],
             binaries=[],
             datas=[],
             hiddenimports=['sys', 'os', 'PyQt5', 'json', 'socket'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='CallClientWin',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
