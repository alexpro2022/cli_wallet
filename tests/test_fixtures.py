def test_mock_input_fixture(mock_input):
    INPUT_VALUE = "test_mock"
    mock_input(INPUT_VALUE)
    assert input("") == INPUT_VALUE
