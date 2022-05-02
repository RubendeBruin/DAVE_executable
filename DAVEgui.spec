# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


hidden = []

# VTK
hidden.extend(['vtkmodules','vtkmodules.all','vtkmodules.qt.QVTKRenderWindowInteractor','vtkmodules.util','vtkmodules.util.numpy_support','vtkmodules.numpy_interface', 'vtkmodules.numpy_interface.dataset_adapter'])

# pyo3d
hidden.append('pyo3d')

# DAVEgui
hidden.append('DAVE.marine')
hidden.append('DAVE.io.orcaflex')
hidden.append('DAVE.solvers.ballast')
hidden.append('DAVE_timeline.gui.helpers')
hidden.append('DAVE_timeline.gui.helpers.flow_layout')

a = Analysis(['DAVEgui.py'],
             pathex=['C:\\data\\Dave\\standalone'],
             binaries=[],
			 datas=[('DAVE.ico','.'),
			 (r'C:\python\miniconda3\envs\pyinstaller\Lib\site-packages\vedo\fonts\*','./Vedo/fonts'),
			 (r'C:\python\miniconda3\envs\pyinstaller\Lib\site-packages\vedo\textures\*','./Vedo/textures'),
			 (r'C:\python\miniconda3\envs\pyinstaller\Lib\site-packages\DAVE\resources\*','./DAVE/resources'),
			 ],
             hiddenimports=hidden,
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
          [],
          exclude_binaries=True,
          name='DAVE',
		  icon = 'DAVE.ico',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='DAVEgui')
