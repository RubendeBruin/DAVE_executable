cd copy_these_in_after_creation
xcopy /E /I * ..\dist\DAVEgui /s
cd ..

cd dist
cd DAVEgui
copy C:\Users\beneden\Miniconda3\Library\bin\tbbmalloc.dll .
copy C:\Users\beneden\Miniconda3\Library\bin\libiomp5md.dll .


