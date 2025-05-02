import unittest

# --- Lambda function ---
def lambda_handler(event, context=None):
    name = event.get("name", "World")
    return {
        "statusCode": 200,
        "body": f"Hello, {name}!"
    }

# --- Unit tests ---
class TestLambdaFunction(unittest.TestCase):

    def test_with_name(self):
        event = {"name": "Deepa"}
        result = lambda_handler(event)
        self.assertEqual(result["statusCode"], 200)
        self.assertEqual(result["body"], "Hello, Deepa!")

    def test_without_name(self):
        event = {}
        result = lambda_handler(event)
        self.assertEqual(result["statusCode"], 200)
        self.assertEqual(result["body"], "Hello, World!")

if __name__ == "__main__":
    unittest.main()
