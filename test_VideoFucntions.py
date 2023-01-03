from HelperFunctions import *

TestDir = 'C:\\Users\\Kyle\\Desktop\\testHelpers'

def test_StandardAssert():
    assert 1==1

def test_TextFileRead():
    assert readFile(TestDir+'\\test1.txt') == ["test"]
def test_TextFileRead2():
    assert readFile(TestDir+'\\test2.txt') == ["test two"]

def test_GetSecondsBasedOnTimeStamp():
    assert GetSecondsBasedOnTimeStamp("00:00:10") == 10
def test_GetSecondsBasedOnTimeStamp2():
    assert GetSecondsBasedOnTimeStamp("00:01:59") == 119
def test_GetSecondsBasedOnTimeStamp3():
    assert GetSecondsBasedOnTimeStamp("01:00:60") == 3660
def test_GetSecondsBasedOnTimeStamp4():
    assert GetSecondsBasedOnTimeStamp("00:00:00") == 0
def test_GetSecondsBasedOnTimeStamp5():
    assert GetSecondsBasedOnTimeStamp("10:00:00") == 36000
