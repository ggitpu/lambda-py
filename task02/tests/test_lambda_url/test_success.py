from tests.test_lambda_url import LambdaUrlLambdaTestCase

class TestSuccess(LambdaUrlLambdaTestCase):

    def test_success(self):
        event = {
            "requestContext": {"httpMethod": "GET"},
            "rawPath": "/hello"
        }
        expected_response = {
            "statusCode": 200,
            "message": "Hello from Lambda"
        }

        self.assertEqual(self.HANDLER.handle_request(event, {}), expected_response)