# -*- mode: python ; coding: utf-8 -*-
import sys

block_cipher = None


a = Analysis(['converter/__main__.py'],
             pathex=[],
             binaries=[],
             datas=[
                ("converter/data/mappings/", "./mappings"),
                ("converter/data/forms/", "./forms"),
             ],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe_args = [
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    []
]

if sys.platform != 'darwin':
    splash = Splash('splashfile.png',
                    binaries=a.binaries,
                    datas=a.datas,
                    text_pos=None,
                    text_size=12,
                    minify_script=True)

    exe_args[-1:-1] = [splash, splash.binaries]

exe = EXE(*exe_args,
          name='converter',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None)
