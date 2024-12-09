import pytest
from StringUtils import StringUtils

SU = StringUtils

def test_1_capitiliz_pos():
    SU = StringUtils()
    res = SU.capitilize("sky")
    assert res == "Sky"

def test_2_capitiliz_neg():
    SU = StringUtils()
    res = SU.capitilize("sky")
    assert res == "0ky"    

def test_3_trim_pos():
    SU = StringUtils()
    res = SU.trim("   sky")
    assert res == "sky" 

def test_4_trim_neg():
    SU = StringUtils()
    res = SU.trim("sky   ")
    assert res == "sky"       

def test_5_trim_neg():
    SU = StringUtils()
    res = SU.trim("sky   ")
    assert res == "sky"

def test_6_to_list_pos():
    SU = StringUtils()
    res = SU.to_list("a,b,c,d")
    assert res == ["a", "b", "c", "d"]

def test_7_to_list_pos():
    SU = StringUtils()
    res = SU.to_list("1:2:3", ":")
    assert res == ["1", "2", "3"]

def test_8_to_list_pos():
    SU = StringUtils()                 # Провал. Нет пустой строки при выходе
    res = SU.to_list("")
    assert res == [""]    

def test_9_contains_pos():
    SU = StringUtils()
    res = SU.contains("SkyPro", "S")
    assert res == True

def test_10_contains_pos():
    SU = StringUtils()
    res = SU.contains("SkyPro", "U")
    assert res == False    

def test_11_contains_neg():
    SU = StringUtils()
    res = SU.contains("SkyPro", "1")
    assert res == True

def test_12_delete_symbol_pos():
    SU = StringUtils()
    res = SU.delete_symbol("SkyPro", "y")
    assert res == ("SkPro")

def test_13_delete_symbol_pos():
    SU = StringUtils()
    res = SU.delete_symbol("SkyPro", "Pro")
    assert res == ("Sky")

def test_14_delete_symbol_neg():
    SU = StringUtils()
    res = SU.delete_symbol("SkyPro", "Pro")
    assert res == ("Pro")      

def test_15_starts_with_pos():
    SU = StringUtils()
    res = SU.starts_with("SkyPro", "S")
    assert res == True

def test_16_starts_with_pos():
    SU = StringUtils()
    res = SU.starts_with("SkyPro", "I")
    assert res == False

def test_17_starts_with_neg():
    SU = StringUtils()
    res = SU.starts_with("SkyPro", "I")
    assert res == True  

def test_18_end_with_pos():
    SU = StringUtils()
    res = SU.end_with("SkyPro", "o")
    assert res == True

def test_19_end_with_pos():
    SU = StringUtils()
    res = SU.end_with("SkyPro", "S")
    assert res == False 

def test_20_end_with_neg():
    SU = StringUtils()
    res = SU.end_with("SkyPro", "S")
    assert res == True

def test_21_is_empty_pos():
    SU = StringUtils()
    res = SU.is_empty(" ")
    assert res == True

def test_22_is_empty_pos():
    SU = StringUtils()
    res = SU.is_empty("")
    assert res == True 

def test_23_is_empty_pos():
    SU = StringUtils()
    res = SU.is_empty("Sky")
    assert res == False

def test_24_is_empty_neg():
    SU = StringUtils()
    res = SU.is_empty("Sky")
    assert res == True         

def test_25_list_to_string_pos():
    SU = StringUtils()
    res = SU.list_to_string([1,2,3,4])
    assert res == "1, 2, 3, 4"

def test_26_list_to_string_pos():
    SU = StringUtils()
    res = SU.list_to_string(["Sky", "Pro"])
    assert res == "Sky, Pro"

def test_27_list_to_string_pos():
    SU = StringUtils()
    res = SU.list_to_string(["Sky", "Pro"], "-")
    assert res == "Sky-Pro"

def test_27_list_to_string_pos():
    SU = StringUtils()
    res = SU.list_to_string(["Sky", "Pro"], "-")
    assert res == "SkyPro"

   
   



