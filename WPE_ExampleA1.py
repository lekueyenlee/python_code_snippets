'''  Coding Exercise from Weekly Python Exercise
Getting input from the user
"while" loops
Converting data from strings to integers
Working with lists
The built-in "sum" function
The built-in "len" function
'''

import sys
import pytest
from io import StringIO

list_numbers = []

user_input = input("Enter a number : ")


def get_output(in_list): 
    print("Sum of integers: " + str(sum(in_list)))
    print("Average value: " + str(sum(in_list)/len(in_list)))
    print("Max value: " + str(max(in_list)))
    print("Min value: " + str(min(in_list)))


while (user_input != ''): 
    list_numbers.append(int(user_input))
    user_input = input("Enter a number : ")

get_output(list_numbers)


#import pytest
#from solution import print_solutions
#from io import StringIO
#mp = monkeypatch
#caps = capsys

def test_no_numbers(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('\n'))

    with pytest.raises(ZeroDivisionError):
        get_output(list_numbers)
        captured_out, captured_err = capsys.readouterr()

        assert 'Smallest: None' in captured_out
        assert 'Largest: None' in captured_out


def test_five_numbers(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('10\n20\n30\n40\n50\n\n'))

    get_output(list_numbers)
    captured_out, captured_err = capsys.readouterr()

    assert 'Smallest: 10' in captured_out
    assert 'Largest: 50' in captured_out
    assert 'Sum: 150' in captured_out
    assert 'Mean: 30.0' in captured_out

#test_no_numbers()
#test_five_numbers(monkeypatch, capsys)

sys.exit()


