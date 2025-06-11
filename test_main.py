from main import load_penguin_data

def test_penguin_data_shape():
    """Test that penguin dataset has expected shape"""
    shape = load_penguin_data()
    assert shape == (344, 7), f"Expected (344, 7), got {shape}"
