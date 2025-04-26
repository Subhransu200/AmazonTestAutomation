# Amazon Test Automation Framework

A comprehensive test automation framework for Amazon.in using Python, Selenium, and Pytest.

## Test Categories

### Smoke Tests
- Hamburger menu functionality
- Basic navigation
- Core page loading

### Functional Tests
- Search functionality
- Category navigation
- Account navigation
- Cart operations

### UI/UX Tests
- Navigation menu layout
- Dropdown behavior
- Responsive design
- Element visibility

### Integration Tests
- Search and filter integration
- Cart integration
- Browser compatibility

## Prerequisites

1. Python 3.x
2. Chrome Browser
3. PowerShell (for Windows)
4. Git (optional)

## Project Structure

```
AutomationScript/
├── tests/
│   ├── test_amazon.py          # Main test file
│   ├── test_runner.py          # Test runner
│   ├── conftest.py             # Pytest fixtures
│   └── base_test.py            # Base test class
├── features/
│   ├── amazon_navigation.feature  # Navigation scenarios
│   ├── amazon_core.feature        # Core functionality
│   └── steps/
│       └── amazon_core_steps.py   # Step definitions
├── pages/
│   ├── amazon_page.py          # Amazon page object
│   └── base_page.py            # Base page object
├── utils/
│   ├── logger.py               # Logging utility
│   ├── driver_factory.py       # WebDriver setup
│   └── selenium_utils.py       # Selenium utilities
├── config/
│   ├── config.py               # Configuration
│   └── environment.py          # Environment settings
├── support/
│   ├── hooks.py                # Test hooks
│   └── env.py                  # Environment setup
├── reports/                    # Test reports
├── logs/                       # Log files
├── run_tests.ps1               # Test runner script
├── setup.ps1                   # Setup script
└── requirements.txt            # Dependencies
```

## Setup Instructions

1. Clone the repository:
```powershell
git clone <repository-url>
cd AutomationScript
```

2. Run the setup script:
```powershell
.\setup.ps1
```

This will:
- Create a virtual environment
- Install required packages
- Set up necessary directories

## Running Tests

### Using PowerShell Script
```powershell
# Run all tests
.\run_tests.ps1

# Run with specific options
.\run_tests.ps1 --tags=@smoke
.\run_tests.ps1 --tags=@functional
.\run_tests.ps1 --tags=@ui
.\run_tests.ps1 --tags=@integration
```

### Using Pytest Directly
```powershell
# Activate virtual environment
.\venv\Scripts\activate

# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_amazon.py

# Run with verbose output
python -m pytest -v

# Run with HTML report
python -m pytest --html=reports/report.html
```

## Test Reports

After test execution, reports are generated in:
- HTML Report: `reports/report.html`
- Screenshots: `reports/screenshots/` (on test failures)
- Logs: `logs/`

## Troubleshooting

### Common Issues

1. **Virtual Environment Issues**
```powershell
# If virtual environment fails to activate
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

2. **Chrome Driver Issues**
```powershell
# Check Chrome version
(Get-Item (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe').'(Default)').VersionInfo.ProductVersion
```

3. **Permission Issues**
- Run PowerShell as Administrator
- Check file permissions in project directory

4. **Dependencies Issues**
```powershell
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Environment Variables

Create a `.env` file in the project root with:
```
HEADLESS=false
NO_SANDBOX=false
IMPLICIT_WAIT=10
SCREENSHOT_DIR=reports/screenshots
```