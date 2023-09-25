import pytest
@pytest.mark.parametrize("input, expected", [
    ("22 lb", 10),
    ("50 kg", 50),
    ("22.1 lb", 10),
    ("22 lx", None),
    ("22lb", None),
    ("352 oz", 10),
    ("22", None),
    ("lbs", None),
    ("22 pounds", 10),
    ("22 lbs", 10),
    ("22 kgs", 22),
    ("-10 kg", -10),
    ("0 kg", 0),
    ("", None),
    ("44 lb" , 20),
    ])
def test_parse_weight_input(input, expected):
    from weight_entry import parse_weight_input
    answer = parse_weight_input(input)
    assert answer == expected

@pytest.mark.parametrize("input, expected", [
    ((0.1, 0.2), 0.3)
    ])
def test_add(input, expected):
    from weight_entry import add
    answer = add(input[0], input[1])
    assert answer == pytest.approx(expected)
    
