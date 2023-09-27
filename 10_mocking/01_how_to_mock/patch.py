import random
from unittest.mock import Mock, patch

# mocking replace some code fragment to allow testing it
# When it's used?
# - code working depends on many independent factors
# - result of the code is not predictible
# - real case object is hard to configure
# - testing rare behavior of the code (ex. unusual error)

# 1. mock directly
# random.choice = Mock(return_value='xyz')
# print(random.choice())

# 2. mock with patch directly
for i in range(3):
    print(random.randint(1, 6))

with patch('random.randint') as mock_random:
    mock_random.return_value = 5

    for i in range(3):
        print(random.randint(1, 6))


# 3. mock with patch decorator
def get_value():
    return random.randint(0, 9)


@patch('random.randint')
def test_get_value(mock_random):
    mock_random.return_value = 3
    result = get_value()
    assert result == 3
    assert mock_random.call_count == 1

    result = get_value()
    assert mock_random.call_count == 2

test_get_value()
