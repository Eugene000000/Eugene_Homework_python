import pytest
from StringUtils import StringUtils

SU = StringUtils()

@pytest.mark.parametrize("input_string, expected", [
    ("skypro", "Skypro"),
    ("  skypro", "  Skypro"),
    ("SKYPRO", "Skypro")
])
def test_capitalize_positive(input_string, expected):
    assert SU.capitilize(input_string) == expected
 
@pytest.mark.parametrize("input_string, expected", [
    ("", ""),
    ("  ", "  ")
])
def test_capitalize_negative(input_string, expected):
    assert SU.capitilize(input_string) == expected    

def test_to_list_should_return_list_with_indent():
    SU = StringUtils()
    res = SU.to_list("a,b,c,d")
    assert res == ["a", "b", "c", "d"]

def test_to_list_should_delete_colon():
    SU = StringUtils()
    res = SU.to_list("1:2:3", ":")
    assert res == ["1", "2", "3"]

def test_to_list_should_empty_string():
    SU = StringUtils()                 
    res = SU.to_list("")
    assert res == []    

def test_contains_should_identify_the_correct_capital_letter():
    SU = StringUtils()
    res = SU.contains("SkyPro", "S")
    assert res == True

def test_contains_should_identify_incorrect_letter():
    SU = StringUtils()
    res = SU.contains("SkyPro", "U")
    assert res == False    

def test_delete_symbol_correct():
    SU = StringUtils()
    res = SU.delete_symbol("SkyPro", "y")
    assert res == ("SkPro")

def test_delete_all_symbol_correct():
    SU = StringUtils()
    res = SU.delete_symbol("SkyPro", "Pro")
    assert res == ("Sky")

@pytest.mark.xfail
def test_delete_symbol_incorrect():
    SU = StringUtils()
    res = SU.delete_symbol("SkyPro", "Pro")
    assert res == ("Pro")      

def test_starts_with_correct_letter_pos():
    SU = StringUtils()
    res = SU.starts_with("SkyPro", "S")
    assert res == True

def test_starts_with_incorrect_letter_pos():
    SU = StringUtils()
    res = SU.starts_with("SkyPro", "I")
    assert res == False

def test_end_with_correct_letter_pos():
    SU = StringUtils()
    res = SU.end_with("SkyPro", "o")
    assert res == True
 
def test_end_with_incorrect_letter_negative_try():
    SU = StringUtils()
    res = SU.end_with("SkyPro", "S")
    assert res == False

def test_is_empty_with_indent_pos():
    SU = StringUtils()
    res = SU.is_empty(" ")
    assert res == True

def test_is_empty_without_indent_pos():
    SU = StringUtils()
    res = SU.is_empty("")
    assert res == True 

def test_is_empty_with_word_pos():
    SU = StringUtils()
    res = SU.is_empty("Sky")
    assert res == False
       
def test_list_to_string():
    SU = StringUtils()
    res = SU.list_to_string([1,2,3,4])
    assert res == "1, 2, 3, 4"


   
   



