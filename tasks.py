from ape import project, config
import pytest

@project.test
def test(project, test_runner):
    config.BROWNIE_PROJECT = project
    pytest.main(["-x"])