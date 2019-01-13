import note

def test_make_option():
    options = {
        "OptionA": "ActionA",
        "OptionB": "ActionB",
        "OptionC": "ActionC"
    }
    expectedOptionString =  'OptionA: ActionA\nOptionB: ActionB\nOptionC: ActionC\n'
    assert note.makeOptions(options) == expectedOptionString

def test_get_mode():
    options = {
        "1": "Read",
        "2": "Delete",
        "3": "Append"
    }
    assert note.getMode("2", options) == "w"