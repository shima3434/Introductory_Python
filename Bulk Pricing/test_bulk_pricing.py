#Names (Me, Partner): Shima Abdulla, Wilson Badillo

import bulk_pricing as gc

def test_get_cost_happy_path():
    'Some happy path cases to test the get_cost function'
    assert gc.get_cost(200) == 140
    assert gc.get_cost(3) == 2.25
    assert gc.get_cost(75) == 54
    assert gc.get_cost(1000) == 670

def test_get_cost_edge():
    'Some edge cases to test the get_cost function'
    assert gc.get_cost(0) == 0
    assert gc.get_cost(50) == 36
    assert gc.get_cost(100) == 70
    assert gc.get_cost(49) == 36.75