import pytest

@pytest.mark.simulacao
@pytest.mark.cadastro
class TestSimulacao():
    def test_simulacao_1(self):
        assert 1 == 1

    def test_simulacao_2(self):
        assert 2 == 2