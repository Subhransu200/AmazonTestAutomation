# Set the working directory to the project root
Set-Location $PSScriptRoot

# Create necessary directories
if (-not (Test-Path "reports")) {
    New-Item -ItemType Directory -Path "reports"
    New-Item -ItemType Directory -Path "reports/screenshots"
}

# Check if Python is installed
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed. Please install Python 3.x first." -ForegroundColor Red
    exit 1
}

# Check if virtual environment exists, if not create it
if (-not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
.\venv\Scripts\Activate

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

# Run the tests
Write-Host "Running Python tests..." -ForegroundColor Green
pytest tests/test_amazon.py `
    --html=reports/report.html `
    --self-contained-html `
    -v

# Check if tests were successful
if ($LASTEXITCODE -eq 0) {
    Write-Host "All tests passed successfully!" -ForegroundColor Green
} else {
    Write-Host "Some tests failed. Please check the reports directory for details." -ForegroundColor Red
}

# Open the report
$reportPath = "reports/report.html"
if (Test-Path $reportPath) {
    Start-Process $reportPath
}

# Deactivate virtual environment
deactivate 