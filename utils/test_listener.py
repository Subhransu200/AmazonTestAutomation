import pytest
from datetime import datetime
import os
from utils.logger import setup_logger

# Setup logger
logger = setup_logger()

# Initialize counters
test_count = 0
passed_count = 0
failed_count = 0
skipped_count = 0
start_time = None

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    global test_count, passed_count, failed_count, skipped_count
    outcome = yield
    report = outcome.get_result()
    
    # Only process the actual test call, not setup/teardown
    if report.when == "call":
        # Get test name
        test_name = item.name
        
        # Get test duration
        duration = report.duration
        
        # Get test status
        status = report.outcome
        
        # Update counters
        test_count += 1
        
        if status == "passed":
            passed_count += 1
            logger.info(f"✅ Test PASSED: {test_name} (Duration: {duration:.2f}s)")
        elif status == "failed":
            failed_count += 1
            logger.error(f"❌ Test FAILED: {test_name} (Duration: {duration:.2f}s)")
            if report.longrepr:
                logger.error(f"Error: {report.longrepr}")
        elif status == "skipped":
            skipped_count += 1
            logger.warning(f"⚠️ Test SKIPPED: {test_name} (Duration: {duration:.2f}s)")

def pytest_sessionstart(session):
    global start_time, test_count, passed_count, failed_count, skipped_count
    start_time = datetime.now()
    logger.info(f"🚀 Test session started at {start_time}")
    # Reset counters at session start
    test_count = 0
    passed_count = 0
    failed_count = 0
    skipped_count = 0

def pytest_sessionfinish(session):
    global start_time, test_count, passed_count, failed_count, skipped_count
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    # Log summary
    logger.info("\n" + "="*50)
    logger.info("📊 Test Execution Summary")
    logger.info("="*50)
    logger.info(f"Total Tests: {test_count}")
    logger.info(f"Passed: {passed_count}")
    logger.info(f"Failed: {failed_count}")
    logger.info(f"Skipped: {skipped_count}")
    logger.info(f"Total Duration: {duration:.2f} seconds")
    logger.info("="*50)

def pytest_exception_interact(call, report):
    if report.failed:
        # Take screenshot on failure
        try:
            if hasattr(call, 'funcargs'):
                driver = call.funcargs.get('driver')
                if driver:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    screenshot_dir = os.path.join("reports", "screenshots")
                    os.makedirs(screenshot_dir, exist_ok=True)
                    screenshot_path = os.path.join(screenshot_dir, f"{report.node.name}_{timestamp}.png")
                    driver.save_screenshot(screenshot_path)
                    logger.info(f"Screenshot saved: {screenshot_path}")
        except Exception as e:
            logger.error(f"Failed to take screenshot: {str(e)}") 