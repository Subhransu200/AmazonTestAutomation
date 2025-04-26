# Python Test Automation Setup Script

Write-Host "Setting up Python test automation environment..."

# Create and activate virtual environment if it doesn't exist
if (-not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
}

# Activate virtual environment
Write-Host "Activating virtual environment..."
.\venv\Scripts\Activate

# Install Python dependencies
Write-Host "Installing Python dependencies..."
pip install -r requirements.txt

# Create necessary directories if they don't exist
$directories = @(
    "reports",
    "allure-results",
    "logs"
)

foreach ($dir in $directories) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir
    }
}

Write-Host "Setup completed successfully!" 