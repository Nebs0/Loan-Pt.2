#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 21:39:27 2023

@author: nebiyousamuel
"""

def compute_monthly_repayment(PV, r, n):
    # Convert annual percentage rate (APR) to monthly interest rate
    monthly_interest_rate = r / (12 * 100)
    
    # Calculate the monthly repayment amount
    numerator = monthly_interest_rate * PV
    denominator = 1 - (1 + monthly_interest_rate)**-n
    Pmt = numerator / denominator
    
    return Pmt

# Input values
PV = 12000
r = 7.45
n = 48

# Compute the monthly repayment amount
monthly_repayment = compute_monthly_repayment(PV, r, n)

print(f"The monthly repayment amount is: ${monthly_repayment:.2f}")
