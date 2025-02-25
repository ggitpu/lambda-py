from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger(__name__)

class LambdaUrl(AbstractLambda):

    def validate_request(self, event) -> dict:
        """Validates the incoming request."""
        http_method = event.get("requestContext", {}).get("httpMethod", "")
        path = event.get("rawPath", "")

        if http_method == "GET" and path == "/hello":
            return {"valid": True}

        return {
            "valid": False,
            "statusCode": 400,
            "message": f"Invalid request {http_method} {path}"
        }

    def handle_request(self, event, context):
        """
        Processes the incoming event and returns the expected response.
        """
        validation_result = self.validate_request(event)
        if not validation_result["valid"]:
            return {
                "statusCode": validation_result["statusCode"],
                "message": validation_result["message"]
            }

        return {
            "statusCode": 200,
            "message": "Hello from Lambda"
        }


HANDLER = LambdaUrl()

def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)