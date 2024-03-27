# -*- mode: python ; coding: utf-8 -*-

arquivos = [
('./res2.json', '.'), ('./cal2.json', '.'), ('./banco_dados.py', '.'), ('./config_cal.py', '.'),
('./calc_incert.py', '.'), ('./conv_num.py', '.'), ('./fun_gerais.py', '.'), ('./arqelx_7.py', '.'),
('./registro_medicao.py', '.')
]

block_cipher = None


a = Analysis(
    ['inicio.py'],
    pathex=[],
    binaries=[],
    datas=arquivos,
    hiddenimports=['json', 'copy', 'scipy', 'time', 'pandas', 'os', 'datetime'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='inicio',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='inicio',
)
