# Egyptian Payment Gateway (Fawry/Instapay) Tracking GTM Kit

> Track Fawry, Instapay, and Vodafone Cash transactions accurately in GA4 and Meta CAPI without broken checkout attribution.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: TEMPLATE_FRAMEWORK](https://img.shields.io/badge/Format-TEMPLATE--FRAMEWORK-green.svg)](#)
[![Tier: 1](https://img.shields.io/badge/Tier-1-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**BOTH** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Create a specialized tracking toolkit for Egyptian payment gateways (Fawry, Instapay, Paymob, Vodafone Cash): 1) Data Layer specification distinguishing 'payment_initiated' vs 'payment_confirmed', 2) Ready-to-import GTM container JSON with custom variables and triggers, 3) Python reconciliation script (`reconcile_payments.py`) matching bank transaction logs to order numbers, 4) Implementation guide for WooCommerce and custom checkouts.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `data-layer/dataLayer-spec-fawry-instapay.js`
- `docs/egyptian-payment-tracking-guide.md`
- `docs/implementation-guide-woocommerce.md`
- `gtm/gtm-egypt-payments-container.json`
- `LICENSE`
- `README.md`
- `scripts/dataLayer_payment_listener.js`
- `src/reconcile_payments.py`
- `src/validate_datalayer.py`
- `templates/fawry-instapay-gtm-container.json`
- `tests/test_reconciler.py`
- `tests/test_reconciliation.py`
- `tests/test_validator.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python src/reconcile_payments.py --help
```

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "reporting",
  "repository": "egyptian-payment-tracking-gtm-kit",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Asynchronous Payment Handshake:** Cash-at-kiosk (Fawry) and Instapay transfers do not finalize immediately; requires server-side webhook listener to confirm purchase events.
- **Iframe Checkout Sandboxing:** Hosted payment redirect pages require postMessage listener bridges to trigger GTM dataLayer events on parent merchant window.
- **EGP Currency & Decimal Precision:** Ensures Fawry fee surcharges and decimal places are calculated accurately in e-commerce purchase payloads.

---

## 📚 Primary Documentation & Verifiable References

- [Fawry Pay Merchant Integration & Webhook Guide](https://developer.fawry.com/) - Official API documentation for Fawry reference codes and status callbacks.
- [Paymob API Documentation & Webhook Verification](https://docs.paymob.com/) - Technical guide for verifying HMAC signatures on payment callbacks.
- [Google Tag Manager Client-Side Data Layer Guide](https://developers.google.com/tag-platform/tag-manager/datalayer) - Standard purchase event payload implementation.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
