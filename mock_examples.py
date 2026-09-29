from unittest.mock import Mock, MagicMock

# Create a mock that can be called and has dynamic attributes
mock_api = Mock()

# Access nested attributes that don't exist yet
# Mock automatically creates them as new mocks
response = mock_api.fetch_user(123)
data = mock_api.users.get_by_id(user_id=456)

# Show that the nested mocks were created
print(f"mock_api.fetch_user exists: {mock_api.fetch_user}")
print(f"mock_api.users exists: {mock_api.users}")
print(f"mock_api.users.get_by_id exists: {mock_api.users.get_by_id}")

# Show they were called
print(f"fetch_user called: {mock_api.fetch_user.called}")
print(f"users.get_by_id called: {mock_api.users.get_by_id.called}")

try:
    expected_result = 123
    mock_api.fetch_user.assert_called_with(expected_result)
    print(f"✅ Assert called with {expected_result} passed")
except AssertionError as e:
    print(f"❌ Assert called with {expected_result} failed: {e}")

try:
    expected_result = 456
    mock_api.fetch_user.assert_called_with(expected_result)
    print(f"✅ Assert called with {expected_result} passed")
except AssertionError as e:
    print(f"❌ Assert called with {expected_result} failed: {e}")


# Regular Mock without magic methods pre-configured
regular_mock = Mock()

# Regular Mock: len() fails without configuration
try:
    length = len(regular_mock)
    print(f"✅ Regular Mock len(): {length}")
except TypeError as e:
    print(f"❌ Regular Mock len() ERROR: {e}")


# MagicMock: len() works out of the box
magic_mock = MagicMock()
try:
    length = len(magic_mock)
    print(f"✅ Magic Mock len(): {length}")
except TypeError as e:
    print(f"❌ Magic Mock len() ERROR: {e}")

from unittest.mock import patch
import requests

# Original module
# myapp.py
def fetch_user(user_id):
    """Calls an external API"""
    return requests.get(f"https://api.example.com/users/{user_id}")

def get_user_name(user_id):
    """Uses fetch_user internally"""
    user_data = fetch_user(user_id)
    return user_data["name"]

# Test file
@patch('myapp.fetch_user')  # Patch where it's LOOKED UP (myapp.py), not where defined
def test_get_user_name(mock_fetch):
    # Inside the function, fetch_user is replaced with mock_fetch
    mock_fetch.return_value = {"name": "Matty"}
    
    result = get_user_name(1)
    
    assert result == "Matty"
    mock_fetch.assert_called_once_with(1)

# After the function ends, fetch_user is restored

from unittest.mock import Mock, MagicMock

# Create a mock that can be called and has dynamic attributes
mock_service = Mock()

# Set up side_effect to raise an exception when called
def make_error():
    """Factory function that creates an error"""
    return Exception("Operation failed 😔")

mock_service.process.side_effect = make_error()

# Access nested attributes that don't exist yet
# Mock automatically creates them as new mocks
try:
    result = mock_service.process("data")
except Exception as e:
    print(f"Exception raised: {e}")