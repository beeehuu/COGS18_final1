from my_module.pokegame_functions import *

def test_r_grass():
    assert r_grass() in grass

def test_QA():
    assert QA("Hello?", "yes")
    
    question = "Hello?"
    answer = "yes"
    test_ = QA("Hello?", "yes")
    assert isinstance(test_, QA)
    
    assert test_.question =="Hello?"
    assert test_.answer =="yes"
             

def test_end_chat():
    assert isinstance(end_chat('a'), bool)
    assert end_chat('quit') == True
    assert callable(end_chat)    

def test_str_combiner():
    assert callable(string_concatenator)
    assert isinstance(string_concatenator('hello', 'world', ' '), str)
    assert string_concatenator('hello', 'world', ' ') == 'hello world'
    

def test_everything():
    test_r_grass()
    test_QA()
    test_end_chat()
    test_str_combiner()
