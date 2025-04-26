# PowerShell script for running Behave tests on Windows

Write-Host "Setting up virtual environment..."
python -m venv venv
.\venv\Scripts\Activate.ps1

Write-Host "Installing dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt

Write-Host "Running Behave tests..."
behave features/ --format pretty --format allure_behave.formatter:AllureFormatter -o allure-results

Write-Host "Generating Allure report..."
allure generate allure-results -o allure-report --clean

Write-Host "Tests completed. Reports available in allure-report/" 