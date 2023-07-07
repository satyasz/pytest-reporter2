# pytest-reporter2

Modified version of pytest-reporter

<b>Supports:</b>
- xdist_group and loadgroup from pytest-xdist

<b>Example:</b>

> tests\test_first.py

    class TestA:

        @pytest.mark.xdist_group("group1")
        def test1():
            pass
		
> Run as

    pytest tests\test_first --dist loadgroup

