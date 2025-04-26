import pytest
import os
import shutil
from behave.__main__ import main as behave_main
from utils.logger import setup_logger

logger = setup_logger()

def test_run_behave():
    logger.info("Running Behave tests via Pytest")
    
    # Create allure-results directory if it doesn't exist
    allure_results_dir = os.path.join(os.getcwd(), "allure-results")
    
    # Remove existing directory or file
    if os.path.exists(allure_results_dir):
        if os.path.isdir(allure_results_dir):
            shutil.rmtree(allure_results_dir)
        else:
            os.remove(allure_results_dir)
    
    # Create fresh directory
    os.makedirs(allure_results_dir, exist_ok=True)
    
    # Set proper permissions
    os.chmod(allure_results_dir, 0o777)
    
    behave_args = [
        "features/",
        "--format", "pretty",
        "--format", f"allure_behave.formatter:AllureFormatter",
        "--outfile", allure_results_dir,
        "--no-capture",
        "--no-skipped"
    ]
    exit_code = behave_main(behave_args)
    assert exit_code == 0, "Behave tests failed" 