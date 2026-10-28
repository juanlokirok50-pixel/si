@echo off
chcp 65001 > nul
cls
echo =====================================================================
echo           SUBIR REPOSITORIO DE TKINTER A GITHUB
echo =====================================================================
echo.

:: Verificar si Git está instalado
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo [!] No se encontro Git instalado en tu sistema.
    echo.
    echo Deseas instalar Git automaticamente ahora usando winget? (S/N)
    set /p INSTALAR="Opcion: "
    if /i "%INSTALAR%"=="S" (
        echo.
        echo Instalando Git, por favor espera un momento...
        winget install --id Git.Git -e --source winget --accept-source-agreements --accept-package-agreements
        echo.
        echo Instalacion finalizada. Por favor cierra y vuelve a abrir este archivo.
        pause
        exit /b
    ) else (
        echo Por favor instala Git desde https://git-scm.com/downloads y reintenta.
        pause
        exit /b
    )
)

echo [1/4] Inicializando repositorio Git local...
if not exist ".git" (
    git init
)

echo.
echo [2/4] Agregando todos los archivos de la carpeta...
git add .

echo.
echo [3/4] Creando commit inicial...
git commit -m "feat: catalogo completo de Tkinter con ejemplos practicos y aplicacion CRUD"

echo.
echo [4/4] Conectar y subir a GitHub
echo ---------------------------------------------------------------------
echo Instrucciones:
echo 1. Entra a https://github.com/new y crea un repositorio vacio.
echo 2. Copia la URL del repositorio (terminada en .git).
echo ---------------------------------------------------------------------
echo.
set /p REPO_URL="Pega aqui la URL de tu repositorio de GitHub: "

if "%REPO_URL%"=="" (
    echo No ingresaste ninguna URL. La operacion fue cancelada.
    pause
    exit /b
)

git branch -M main
git remote remove origin 2>nul
git remote add origin %REPO_URL%

echo.
echo Subiendo archivos a la rama main de GitHub...
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo =====================================================================
    echo   FELICIDADES: Tu repositorio ya esta publicado en GitHub!
    echo   URL: %REPO_URL%
    echo =====================================================================
) else (
    echo.
    echo [!] Hubo un detalle al subir. Asegurate de haber iniciado sesion
    echo     en GitHub con tu usuario o mediante GitHub Desktop / token.
)

echo.
pause
