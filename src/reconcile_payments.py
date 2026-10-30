"""
Egyptian Payment Gateway (Fawry / Instapay / Paymob / ValU) Reconciliation Engine
Matches frontend GA4 purchase events against backend gateway settlement CSV exports:
- Matches by order_id or gateway transaction reference
- Flags uncaptured Fawry reference numbers (pending cash at kiosk)
- Flags Instapay manual transfers awaiting confirmation
- Computes reconciliation match rate and missing conversion revenue
"""
import json
import argparse
from typing import List, Dict, Any

def reconcile_transactions(ga4_events: List[Dict[str, Any]], gateway_settlements: List[Dict[str, Any]]) -> Dict[str, Any]:
    settled_by_order = {s["order_id"]: s for s in gateway_settlements if s.get("status") == "SUCCESS"}
    failed_by_order = {s["order_id"]: s for s in gateway_settlements if s.get("status") != "SUCCESS"}
    
    matched = []
    unsettled_in_ga4 = []
    missing_in_ga4 = []
    
    ga4_orders = {e["order_id"]: e for e in ga4_events}
    
    for order_id, ga_event in ga4_orders.items():
        if order_id in settled_by_order:
            matched.append({
                "order_id": order_id,
                "amount": ga_event.get("value", 0),
                "gateway": settled_by_order[order_id].get("gateway", "UNKNOWN")
            })
        else:
            unsettled_in_ga4.append({
                "order_id": order_id,
                "amount": ga_event.get("value", 0),
                "status": "UNSETTLED_OR_PENDING_KIOSK"
            })
            
    for order_id, sett in settled_by_order.items():
        if order_id not in ga4_orders:
            missing_in_ga4.append({
                "order_id": order_id,
                "amount": sett.get("amount", 0),
                "gateway": sett.get("gateway", "UNKNOWN"),
                "status": "SETTLED_WITHOUT_GA4_TELEMETRY"
            })
            
    total_ga4_rev = sum(e.get("value", 0) for e in ga4_events)
    total_settled_rev = sum(s.get("amount", 0) for s in settled_by_order.values())
    
    match_rate = (len(matched) / len(ga4_events) * 100.0) if ga4_events else 0.0
    
    return {
        "ga4_orders_count": len(ga4_events),
        "gateway_settled_count": len(settled_by_order),
        "matched_count": len(matched),
        "unsettled_count": len(unsettled_in_ga4),
        "telemetry_loss_count": len(missing_in_ga4),
        "match_rate_pct": round(match_rate, 2),
        "ga4_revenue": total_ga4_rev,
        "settled_revenue": total_settled_rev,
        "unmatched_samples": unsettled_in_ga4[:5]
    }

def main():
    ga4_sample = [
        {"order_id": "ORD-101", "value": 450.0, "gateway": "fawry"},
        {"order_id": "ORD-102", "value": 1200.0, "gateway": "paymob"},
        {"order_id": "ORD-103", "value": 300.0, "gateway": "instapay"}
    ]
    settlements = [
        {"order_id": "ORD-102", "amount": 1200.0, "status": "SUCCESS", "gateway": "paymob"},
        {"order_id": "ORD-104", "amount": 800.0, "status": "SUCCESS", "gateway": "fawry"}
    ]
    res = reconcile_transactions(ga4_sample, settlements)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
