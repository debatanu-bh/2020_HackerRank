from UnitTest import mathProblem

import pytest
@pytest.mark.parametrize('a,b,c',[(2,3,5),(3,4,7)])
def test_add(a,b,c):
    assert mathProblem.add(a,b)==c
    # assert mathProblem.add(7,3)==10
    # assert mathProblem.add ( 7, 4 ) == 11
    # assert mathProblem.add ( 7, 13 ) == 20
    # assert mathProblem.add ( 7, 30 ) == 37
    # assert mathProblem.add ( 7, 3 ) == 10
    # assert mathProblem.add ( 7, 3 ) == 10
def test_multi():
    assert mathProblem.multi(1,2)==2
    assert mathProblem.multi(1,3)==3

