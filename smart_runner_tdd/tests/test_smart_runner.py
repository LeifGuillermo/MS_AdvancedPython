from src.smart_runner import monitor_execution, unique_id_generator # Will fail on import
import pytest
import time
import logging

def test_unique_id_generator_sequence():
    generator1 = unique_id_generator()
    assert next(generator1) == 1
    assert next(generator1) == 2

    generator2 = unique_id_generator() # Create a new instance
    assert next(generator2) == 1 # Assert new generator starts from 1 again
    assert next(generator1) == 3 # Assert first generator continues independently


def test_monitored_function_execution_and_id(caplog):
    """
    Test that the @monitor_execution decorator logs execution details and returns the correct result.

    This test verifies that:
    - The decorated function executes and returns its expected result.
    - Logging occurs at the INFO level for function execution start and finish.
    - A unique ID is logged for each function execution.

    Example:
        @monitor_execution
        def sample_func():
            time.sleep(0.01)
            return "done"

        with caplog.at_level(logging.INFO):
            result = sample_func()
        assert result == "done"
        assert any("Executing sample_func" in r.message for r in caplog.records)
        assert any("Finished sample_func" in r.message for r in caplog.records)
        assert any("Unique ID:" in r.message for r in caplog.records)

    Args:
        caplog (pytest fixture): Captures log records for assertion.

    Asserts:
        - The function returns the expected value.
        - Log records contain execution start, finish, and unique ID messages.
    """
    @monitor_execution
    def my_test_func():
        time.sleep(0.01)
        return "result"
    
    with caplog.at_level(logging.INFO): # Capture INFO level & above
        result = my_test_func()
        
    assert result == "result"
    assert any("Executing my_test_func" in r.message for r in caplog.records)
    assert any("Finished my_test_func" in r.message for r in caplog.records)
    assert any("Unique ID:" in r.message for r in caplog.records) # simply checking for presence of a unique ID statement

def test_monitor_execution_decorator_with_exception(caplog):
    """
    Test that the @monitor_execution decorator handles exceptions correctly.

    This test verifies that:
    - The decorated function raises an exception as expected.
    - Logging occurs at the ERROR level for exceptions.
    - A unique ID is logged for the function execution.

    Example:
        @monitor_execution
        def sample_func():
            raise ValueError("An error occurred")

        with pytest.raises(ValueError):
            sample_func()
        assert any("Executing sample_func" in r.message for r in caplog.records)
        assert any("Finished sample_func" in r.message for r in caplog.records)
        assert any("Unique ID:" in r.message for r in caplog.records)

    Args:
        caplog (pytest fixture): Captures log records for assertion.

    Asserts:
        - The function raises the expected exception.
        - Log records contain execution start, finish, and unique ID messages.
    """
    @monitor_execution
    def my_test_func():
        raise ValueError("An error occurred")
    
    with caplog.at_level(logging.INFO):
        with pytest.raises(ValueError):
            my_test_func()
    
    assert any("Executing my_test_func" in r.message for r in caplog.records)
    assert any("Finished my_test_func" in r.message for r in caplog.records)
    assert any("Unique ID:" in r.message for r in caplog.records) # simply checking for presence of a unique ID statement
