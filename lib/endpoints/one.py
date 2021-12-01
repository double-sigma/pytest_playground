from lib.two import Two


class One:
    def assert_these_are_equal(self, a, b):
        two = Two()
        two.assert_these_are_equal_too(a, b)


