@echo off
chcp 65001 >nul

@REM REM Перевірка наявності файлу requirements.txt в папці env
if exist "env\requirements.txt" (
    echo Видаляємо старий файл requirements.txt...
    del "env\requirements.txt"
)

REM Створення нового файлу requirements.txt
echo Створюємо новий файл requirements.txt...
pip freeze > env\requirements.txt
echo requirements.txt створено та оновлено.

pause
