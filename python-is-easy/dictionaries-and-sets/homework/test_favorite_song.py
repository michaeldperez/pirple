from favorite_song import *
import pytest

@pytest.mark.parametrize("key, value, expected", [
    ("Title", "AnyTime (Extended Mix)", True),
    ("Album", "SPRS031", True),
    ("Genre", "Future House", True),
    ("ReleaseDate", "2014-08-04", True),
    ("Label", "Spinnin' Records (SPRS)", True),
    ("Country", "Netherlands", True),
    ("VideoLink", "https://youtu.be/qzNQLKgaLi0", True),
    ("DurationInSeconds", 247, True),
    ("DurationInMinutes", 4.57, True),
    ("Label", "Confession", False),
    ("NonExistantKey", "NonExistantValue", False)
])
def test_keyguess(key, value, expected):
    assert keyguess(key, value) == expected
