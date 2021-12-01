import pytest

# we want to have pytest assert introspection in the helpers
pytest.register_assert_rewrite('lib.endpoints.one')
pytest.register_assert_rewrite('lib.endpoints.three')