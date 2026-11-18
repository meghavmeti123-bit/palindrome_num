from palindrome import palindrome

def test_palindrome():
    result = palindrome("madam")
    assert result == "Palindrome"

def test_not_palindrome():
    result = palindrome("hello")
    assert result == "Not Palindrome"

def test_number_palindrome():
    result = palindrome("121")
    assert result == "Palindrome"