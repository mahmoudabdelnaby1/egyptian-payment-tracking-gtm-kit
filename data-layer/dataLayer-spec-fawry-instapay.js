/**
 * Egyptian Payment Gateway (Fawry/Instapay) Tracking GTM Kit
 * File: data-layer/dataLayer-spec-fawry-instapay.js
 */

(function() {
  'use strict';
  const config = {
    name: "egyptian-payment-tracking-gtm-kit",
    subNiche: "reporting",
    version: "1.0.0"
  };

  function init() {
    console.log("Initialized " + config.name);
  }

  if (typeof document !== 'undefined') {
    document.addEventListener('DOMContentLoaded', init);
  } else if (typeof module !== 'undefined' && module.exports) {
    module.exports = config;
  }
})();
