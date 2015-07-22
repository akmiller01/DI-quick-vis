# -*- mode: python -*-

block_cipher = None


a = Analysis(['./qv/di-quick-vis.py'],
             pathex=['/home/alex/git/di-quick-vis'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             cipher=block_cipher)
pyz = PYZ(a.pure,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='di-quick-vis',
          debug=False,
          strip=None,
          upx=True,
          console=True )
