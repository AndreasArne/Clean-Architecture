from unittest.mock import patch

from fileinfo.logger import Logger

@patch("fileinfo.logger.datetime.datetime")
def test_log(mock_datetime):
    test_now = 123
    test_msg = "A test message"
    mock_datetime.now.return_value = test_now
    
    test_logger = Logger()
    test_logger.log(test_msg)
    
    assert test_logger.messages == [(test_now, test_msg)]