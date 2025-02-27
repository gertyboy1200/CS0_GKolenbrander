"""Module to test important functions in main.py"""

import main

def test_odd_even():
    """Function to test odd_even function
    """
    number = 99999
    expected = "odd"
    ans = main.odd_even(number)
    assert (main.odd_even(number) ==
            ans), f"Expected: {expected}, but got: {ans}"

def test_odd_even2():
    """Function to test odd_even function"""
    assert (main.odd_even(200) ==
            "even"), f"Expected: even, but got: {main.odd_even(200)}"

def test_odd_even3():
    """Function to test odd_even function"""
    assert (main.odd_even(400) ==
            "even"), f"Expected: even, but got: {main.odd_even(400)}"

def test_odd_even4():
    """Function to test odd_even function"""
    assert (main.odd_even(561) ==
            "odd"), f"Expected: odd, but got: {main.odd_even(561)}"

def test_answer():
    """ FUntion to test answer function"""
    assert(main.answer(40) == "Bob"), f"Expected: Bob but got: {main.answer(40)}"

def test_answer2():
    """ FUntion to test answer function"""
    assert(main.answer(55) == "Alice"), f"Expected: Alice but got: {main.answer(55)}"

def test_answer():
    """ FUntion to test answer function"""
    assert(main.answer(99999) == "Alice"), f"Expected: Alice but got: {main.answer(99999)}"