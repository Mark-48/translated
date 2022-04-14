import pytest
from main import splited_txt, splited_words

def test_split_text():
    assert splited_txt("Hello World !") == ['Hello', 'World', '!']


def test_split_words():
    assert splited_words('Hello') == ['H', 'e', 'l', 'l', 'o' ]