import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from validate_datalayer import validate_egypt_payment_payload

class TestDatalayer(unittest.TestCase):
    def test_val(self):
        sample = {"event": "purchase", "ecommerce": {"currency": "EGP", "payment_gateway": "INSTAPAY"}}
        ok, _ = validate_egypt_payment_payload(sample)
        self.assertTrue(ok)

if __name__ == "__main__":
    unittest.main()
