from batch_calculator import process_calculation

def test_process_calculation():
    assert process_calculation("*", 4, 3) == ("OK", 12.0, "")
