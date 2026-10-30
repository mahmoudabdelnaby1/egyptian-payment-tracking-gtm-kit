/**
 * Fawry & Instapay Asynchronous Payment Completion dataLayer Listener
 */
window.addEventListener("message", function(e) {
  if (e.data && e.data.status === "PAID" && e.data.gateway === "FAWRY") {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      event: "purchase",
      ecommerce: {
        transaction_id: e.data.referenceNumber,
        value: parseFloat(e.data.amount),
        currency: "EGP",
        payment_gateway: "FAWRY_PAY",
        items: e.data.items || []
      }
    });
  }
});
