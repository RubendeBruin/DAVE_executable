call activate pyinstaller
rmdir dist /s
rmdir build /s
pip install C:/data/Dave/Public/DAVE --use-feature=in-tree-build
pyinstaller DAVEgui.spec
echo copy_in.bat
cd dist
cd DAVEgui
DAVE.exe
