#!/usr/bin/env python3
import json
import sys

def validate_egypt_payment_payload(payload):
    issues = []
    if payload.get("event") != "purchase":
        issues.append("Event must be 'purchase'.")
    ecom = payload.get("ecommerce", {})
    if ecom.get("currency") != "EGP":
        issues.append("Currency for Fawry/Instapay tracking must be EGP.")
    if ecom.get("payment_gateway") not in ["FAWRY_PAY", "INSTAPAY", "VODAFONE_CASH", "VALU"]:
        issues.append("Unrecognized Egyptian payment gateway.")

    return len(issues) == 0, issues

if __name__ == "__main__":
    sample = {"event": "purchase", "ecommerce": {"currency": "EGP", "payment_gateway": "FAWRY_PAY"}}
    ok, errs = validate_egypt_payment_payload(sample)
    print(f"Validation Status: {'PASS' if ok else 'FAIL'}")
