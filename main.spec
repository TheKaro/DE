# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src\\main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('maps/level.txt', 'maps/level.txt'),
        ('assets/images/big_pellet.png', 'assets/images/big_pellet.png'),
        ('assets/images/pellet.png', 'assets/images/pellet.png'),
        ('assets/images/ghost_blue.png', 'assets/images/ghost_blue.png'),
        ('assets/images/ghost_orange.png', 'assets/images/ghost_orange.png'),
        ('assets/images/ghost_pink.png', 'assets/images/ghost_pink.png'),
        ('assets/images/ghost_red.png', 'assets/images/ghost_red.png'),
        ('assets/images/wall.png', 'assets/images/wall.png'),
        ('assets/sounds/chomp.wav', 'assets/sounds/chomp.wav'),
        ('assets/sounds/death.wav', 'assets/sounds/death.wav'),
        ('assets/sounds/eatfruit.wav', 'assets/sounds/eatfruit.wav'),
        ('hook-pkgutil.py', 'hook-pkgutil.py'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
