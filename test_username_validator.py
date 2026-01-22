import pytest

class CreditCardValidator:
    """Test suite for credit_card_validator function"""

    def Test_visa_card(self):
        """Test for a valid Visa number"""
        assert credit_card_validator("4539578763621486") == True

    def Test_visa_card_length_to_short(self):
        """Test the length of a Visa number thats one too short"""
        assert credit_card_validator("424422687364335") == False

    def Test_visa_card_length_to_long(self):
        """Test the length of Visa number thats one too long"""
        assert credit_card_validator("45395787636214868") == False


'------------------------------------------------------------------------------'


def Test_MasterCard_card(self):
    """Test for a valid MasterCard number"""
    assert credit_card_validator("5555555555554444") == True


def Test_MasterCard_card_length_to_short(self):
    """Test the length of a MasterCard number that's one too short"""
    assert credit_card_validator("529153543723745") == False


def Test_MasterCard_card_length_to_long(self):
    """Test the length of MasterCard number that's one too long"""
    assert credit_card_validator("55555555555544440") == False


'-----------------------------------------------------------------------------'


def Test_AmericanExpress_card(self):
    """Test for a valid AmericanExpress number"""
    assert credit_card_validator("378282246310005") == True


def Test_AmericanExpress_card_length_to_short(self):
    """Test the length of a AmericanExpress number thats one too short"""
    assert credit_card_validator("3782822463100059") == False


def Test_AmericanExpress_card_length_to_long(self):
    """Test the length of AmericanExpress number thats one too long"""
    assert credit_card_validator("3782822463100052") == False


'-----------------------------------------------------------------------------'
def Test_Empty_input(self):
    """Test for an empty input"""
    assert credit_card_validator() == False

def Test_Empty_string(self):
    """Test for an empty string"""
    assert credit_card_validator("") == False

def Test_Unsupported_prfix_16(self):
    """Test for an unsupported prfix for 16 digits"""
    assert credit_card_validator("6897756347522484") == False

def Test_Unsupported_prfix_15(self):
    """Test for an unsupported prfix for 15 digits"""
    assert credit_card_validator("765989089194046") == False
