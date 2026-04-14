"""
Application to generate OTP (One Time Password)
"""

import random


def generate_otp():
    """Generates a 6-digit OTP using the random module and returns it"""
    otp = random.randint(100000, 999999)
    return otp


if __name__ == "__main__":
    print("Your OTP is:", generate_otp())
