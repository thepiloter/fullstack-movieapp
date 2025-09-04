@echo off
echo Starting Movie App with Docker Compose...
echo.

REM Check if Docker is running
docker version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Docker is not running or not installed.
    echo Please start Docker Desktop and try again.
    pause
    exit /b 1
)

REM Build and start the application
echo Building and starting the application...
docker-compose up --build -d

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo   Movie App is now running!
    echo ========================================
    echo.
    echo Web Application: http://localhost:8000
    echo Admin Panel: http://localhost:8000/admin
    echo   Username: admin
    echo   Password: admin123
    echo.
    echo To stop the application, run:
    echo   docker-compose down
    echo.
    echo Opening browser...
    start http://localhost:8000
) else (
    echo.
    echo Error: Failed to start the application.
    echo Please check the Docker logs for more information.
)

pause
