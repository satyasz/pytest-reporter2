================
pytest-reporter2
================

Modified version of pytest-reporter

This supports xdist_group and loadgroup from pytest-xdist

For example:

--- tests\test_first.py ---

class TestA:

	@pytest.mark.xdist_group("group1")
	def test2():
		pass
		
--- Run as ---

pytest tests\test_first --dist loadgroup

