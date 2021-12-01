from lib.endpoints.one import One
from lib.endpoints.three import Three


def test_one():
    assert 'ABC' == 'DBA'


def test_two():
    one = One()
    three = Three()
    one.assert_these_are_equal('ABC', 'DFG')
    three.assert_string_is_four('ABC')




