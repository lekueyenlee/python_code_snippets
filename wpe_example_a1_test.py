'''  Question:  what is the difference b/w using the below
''      - from solution_wpe_1 import print_solutions()
''      - import solution_wpe_1 
''
''
'''

import pytest
import solution_wpe_1
from io import StringIO


def test_no_numbers(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('\n'))

    with pytest.raises(ZeroDivisionError):
        solution_wpe_1.print_solutions()
        captured_out, captured_err = capsys.readouterr()

        assert 'Smallest: None' in captured_out
        assert 'Largest: None' in captured_out


def test_five_numbers(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('10\n20\n30\n40\n50\n\n'))
    solution_wpe_1.print_solutions()
    captured_out, captured_err = capsys.readouterr()

    assert 'Smallest: 10' in captured_out
    assert 'Largest: 50' in captured_out
    assert 'Sum: 150' in captured_out
    assert 'Mean: 30.0' in captured_out
