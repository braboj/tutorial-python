# testing_unittest_mock

```python
# Framework: unittest (with mocks)
# ----------------------------------
#
# Mock HTTP calls while testing payment processing logic.

# Example: unittest mock test cases

import unittest
from unittest.mock import patch, Mock

import requests


def process_payment(payment_data):
    # Make an HTTP request to process the payment
    response = requests.post("https://payment-api.com/process", json=payment_data)
    return response.status_code


class TestPaymentProcessor(unittest.TestCase):

    @patch('requests.post')
    def test_process_payment_success(self, mock_post):
        # Configure the mock object to return a successful response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        # Test the process_payment function
        payment_data = {"amount": 100, "card": "1234-5678-9012-3456"}
        result = process_payment(payment_data)

        # Assertions
        self.assertEqual(result, 200)
        mock_post.assert_called_once_with("https://payment-api.com/process", json=payment_data)


if __name__ == '__main__':
    unittest.main()
```
