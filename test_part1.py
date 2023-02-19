import unittest
from autograder import runGrader



class TestQ1(unittest.TestCase):

    def test_q(self):
        result = runGrader(['-q', 'q1'])
        assert result['q1'] == 2


class TestQ2(unittest.TestCase):
    
    def test_q(self):
        result = runGrader(['-q', 'q2'])
        assert result['q2'] == 2


class TestQ3(unittest.TestCase):
    
    def test_q(self):
        result = runGrader(['-q', 'q3'])
        assert result['q3'] == 2


class TestQ5HalfCredit(unittest.TestCase):
    
    def test_q(self):
        result = runGrader(['-q', 'q5'])
        assert result['q5'] >= 1


class TestQ5FullCredit(unittest.TestCase):

    def test_q(self):
        result = runGrader(['-q', 'q5'])
        assert result['q5'] == 2
