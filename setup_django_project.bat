@echo off
echo Setting up Django project configuration...

echo # Django Templates > .prettierignore
echo templates/**/*.html >> .prettierignore
echo */templates/**/*.html >> .prettierignore
echo **/*templates/**/*.html >> .prettierignore
echo *.html >> .prettierignore
echo static/**/* >> .prettierignore
echo */static/**/* >> .prettierignore
echo *.py >> .prettierignore

mkdir .vscode
echo { > .vscode\settings.json
echo   "[django-html]": { >> .vscode\settings.json
echo     "editor.formatOnSave": false >> .vscode\settings.json
echo   }, >> .vscode\settings.json
echo   "[html]": { >> .vscode\settings.json
echo     "editor.formatOnSave": false >> .vscode\settings.json
echo   }, >> .vscode\settings.json
echo   "files.associations": { >> .vscode\settings.json
echo     "**/templates/**/*.html": "django-html" >> .vscode\settings.json
echo   } >> .vscode\settings.json
echo } >> .vscode\settings.json

echo Django project configuration complete!
pause
