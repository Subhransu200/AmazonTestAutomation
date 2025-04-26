# Amazon Test Automation - Run Instructions

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Initial Setup](#initial-setup)
3. [Environment Configuration](#environment-configuration)
4. [Running Tests](#running-tests)
5. [Viewing Results](#viewing-results)
6. [Troubleshooting](#troubleshooting)
7. [Test Categories](#test-categories)

## Prerequisites

Before running the tests, ensure you have:
- Python 3.x installed
- Chrome browser installed
- PowerShell (for Windows)
- Git (optional)

## Initial Setup

1. Clone the repository:
```powershell
git clone https://github.com/Subhransu200/AmazonTestAutomation.git
cd AmazonTestAutomation
```

2. Create environment file:
```powershell
# Create .env file
New-Item -Path ".env" -ItemType "file"

# Add the following content to .env file:
@"
# Browser Settings
HEADLESS=false
NO_SANDBOX=false
IMPLICIT_WAIT=10

# Report Settings
SCREENSHOT_DIR=reports/screenshots

# Test Settings
BASE_URL=https://www.amazon.in
BROWSER=chrome
TIMEOUT=30

# Logging Settings
LOG_LEVEL=INFO
LOG_DIR=logs
"@ | Out-File -FilePath ".env" -Encoding UTF8
```

## Environment Configuration

Run the setup script to configure the environment:
```powershell
.\setup.ps1
```

This script will:
- Create a virtual environment
- Install required packages
- Set up necessary directories
- Configure test environment

## Running Tests

### Option 1: Using PowerShell Script

1. Run all tests:
```powershell
.\run_tests.ps1
```

2. Run specific test categories:
```powershell
# Smoke tests
.\run_tests.ps1 --tags=@smoke

# Functional tests
.\run_tests.ps1 --tags=@functional

# UI/UX tests
.\run_tests.ps1 --tags=@ui

# Integration tests
.\run_tests.ps1 --tags=@integration
```

### Option 2: Using Pytest Directly

1. Activate virtual environment:
```powershell
.\venv\Scripts\activate
```

2. Run tests:
```powershell
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_amazon.py

# Run with verbose output
python -m pytest -v

# Run with HTML report
python -m pytest --html=reports/report.html
```

## Viewing Results

After test execution, results are available in:

1. HTML Report:
   - Location: `reports/report.html`
   - Contains: Test summary, pass/fail status, execution time

2. Screenshots:
   - Location: `reports/screenshots/`
   - Generated: On test failures
   - Format: PNG files with timestamp

3. Logs:
   - Location: `logs/`
   - Contains: Detailed execution logs
   - Format: Text files with timestamp

## Troubleshooting

### Common Issues and Solutions

1. Virtual Environment Issues:
```powershell
# If virtual environment fails to activate
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

2. Dependencies Issues:
```powershell
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

3. Chrome Driver Issues:
```powershell
# Check Chrome version
(Get-Item (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe').'(Default)').VersionInfo.ProductVersion

# Update webdriver-manager
python -m pip install --upgrade webdriver-manager
```

4. Permission Issues:
- Run PowerShell as Administrator
- Check file permissions in project directory

## Test Categories

### Smoke Tests
- Basic functionality verification
- Core page loading
- Essential navigation

### Functional Tests
- Search functionality
- Category navigation
- Account operations
- Cart management

### UI/UX Tests
- Navigation menu layout
- Dropdown behavior
- Responsive design
- Element visibility

### Integration Tests
- Search and filter integration
- Cart integration
- Browser compatibility
- Cross-feature functionality

## Best Practices

1. Always run tests in a clean environment
2. Check logs for detailed error information
3. Review screenshots for visual verification
4. Keep test data separate from test code
5. Use appropriate waits instead of hard delays
6. Keep test cases independent

## Support

For additional help:
1. Check the troubleshooting section
2. Review the logs in `logs/` directory
3. Check test reports in `reports/` directory
4. Refer to the main README.md file 