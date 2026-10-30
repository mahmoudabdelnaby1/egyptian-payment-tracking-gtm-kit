"""
Unit tests for Egyptian Payment Reconciler
"""
import unittest
from src.reconcile_payments import reconcile_transactions

class TestReconcilePayments(unittest.TestCase):
    def test_reconciliation_logic(self):
        ga4 = [{"order_id": "O1", "value": 100}, {"order_id": "O2", "value": 200}]
        settled = [{"order_id": "O1", "amount": 100, "status": "SUCCESS", "gateway": "paymob"}]
        
        res = reconcile_transactions(ga4, settled)
        self.assertEqual(res["matched_count"], 1)
        self.assertEqual(res["unsettled_count"], 1)
        self.assertEqual(res["match_rate_pct"], 50.0)

if __name__ == "__main__":
    unittest.main()
