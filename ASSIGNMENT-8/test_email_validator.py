"""
Comprehensive test cases for is_valid_email function
Generated using AI to cover all edge cases and requirements
"""
import unittest
from Q1 import is_valid_email


class TestEmailValidator(unittest.TestCase):
    """Test cases for email validation function"""
    
    # Valid email test cases
    def test_valid_emails(self):
        """Test cases for valid emails"""
        valid_emails = [
            "user@example.com",
            "test.email@domain.co.uk",
            "name@example.org",
            "user123@test.com",
            "first.last@example.com",
            "a@b.co",
            "user.name@domain.example.com",
            "simple@test.com",
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email), 
                              f"'{email}' should be valid")
    
    # Invalid: Missing @ or .
    def test_missing_at_symbol(self):
        """Test cases for emails without @ symbol"""
        invalid_emails = [
            "userexample.com",
            "test.emaildomain.com",
            "noatsymbol.com",
            "justtext",
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email), 
                               f"'{email}' should be invalid (no @)")
    
    def test_missing_dot(self):
        """Test cases for emails without . in domain"""
        invalid_emails = [
            "user@example",
            "test@domain",
            "email@nodot",
            "user@com",
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email), 
                               f"'{email}' should be invalid (no .)")
    
    def test_no_dot_after_at(self):
        """Test cases for emails with dot before @ but not after"""
        invalid_emails = [
            "user.name@example",
            "test.email@domain",
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email), 
                               f"'{email}' should be invalid (no . after @)")
    
    # Invalid: Multiple @ symbols
    def test_multiple_at_symbols(self):
        """Test cases for emails with multiple @ symbols"""
        invalid_emails = [
            "user@@example.com",
            "test@email@domain.com",
            "@@example.com",
            "user@test@example.com",
            "user@@@example.com",
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email), 
                               f"'{email}' should be invalid (multiple @)")
    
    # Invalid: Starting with special characters
    def test_starts_with_special_characters(self):
        """Test cases for emails starting with special characters"""
        invalid_emails = [
            "@example.com",
            ".user@example.com",
            "_user@example.com",
            "-user@example.com",
            "+user@example.com",
            "%user@example.com",
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email), 
                               f"'{email}' should be invalid (starts with special char)")
    
    # Invalid: Ending with special characters
    def test_ends_with_special_characters(self):
        """Test cases for emails ending with special characters"""
        invalid_emails = [
            "user@example.com.",
            "user@example.com_",
            "user@example.com-",
            "user@example.com@",
            "user@example.",
            "user@example_",
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email), 
                               f"'{email}' should be invalid (ends with special char)")
    
    # Invalid: Invalid characters after @
    def test_invalid_characters_after_at(self):
        """Test cases for emails with invalid characters after @ (only . and A-z allowed)"""
        invalid_emails = [
            "user@123example.com",  # Numbers not allowed after @
            "user@example123.com",  # Numbers not allowed after @
            "user@example.com123",  # Numbers not allowed
            "user@test_email.com",  # Underscore not allowed after @
            "user@test-email.com",  # Hyphen not allowed after @
            "user@test+email.com",  # Plus not allowed after @
            "user@test%email.com",  # Percent not allowed after @
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email), 
                               f"'{email}' should be invalid (invalid chars after @)")
    
    # Edge cases
    def test_empty_string(self):
        """Test empty string"""
        self.assertFalse(is_valid_email(""))
    
    def test_only_at_symbol(self):
        """Test string with only @"""
        self.assertFalse(is_valid_email("@"))
    
    def test_only_dot(self):
        """Test string with only ."""
        self.assertFalse(is_valid_email("."))
    
    def test_at_and_dot_only(self):
        """Test string with only @ and ."""
        self.assertFalse(is_valid_email("@."))
    
    def test_single_character_before_at(self):
        """Test valid single character before @"""
        self.assertTrue(is_valid_email("a@b.co"))
    
    def test_multiple_dots_after_at(self):
        """Test multiple dots after @ (should be valid if format is correct)"""
        valid_emails = [
            "user@example.co.uk",
            "test@sub.domain.example.com",
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email), 
                              f"'{email}' should be valid")


if __name__ == '__main__':
    unittest.main()

