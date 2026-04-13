---
title: "Blue Sea 7610 SI-ACR Wiring Research"
category: sources
source-type: ai-research-report
ingested: 2026-04-13
tags: [Blue-Sea, ACR, batteries, electrical, dual-battery]
---

# Blue Sea 7610 SI-ACR Wiring Research

**Files covered:**
- raw/Blue Sea 7610 Wiring.md
- raw/How to connect the ground for SI-ACR 7610.md

## Summary

Comprehensive technical breakdown of the Blue Sea 7610 SI-ACR terminals, operational logic (combine/isolate voltage thresholds and timing), LED status indicators, and wiring best practices. Ground terminal wiring covers required parts (female quick-connect spades, waterproof inline fuse holder, ATC fuses, marine wire). The Blue Sea 7610 file appears to be a thorough, technically accurate reference document.

## Key Takeaways

- Studs A and B are interchangeable (dual sensing)
- GND terminal requires mandatory 10–15A inline fuse — fire hazard without it
- SI terminal must connect to crank-only circuit, not ignition-run circuit
- Combine threshold: 13.6V (30 sec) or 13.0V (90 sec)
- Isolate threshold: 12.75V (30 sec) or 12.35V (10 sec)
- Under-voltage lockout at 9.5V — ACR won't combine if either battery is this low
- Fast blinking LED = lockout condition; slow blinking = start isolation active

## Contradictions / Surprises

> **AI-generated but well-sourced** — cites Blue Sea Systems owner's manual directly. Cross-check wiring against the actual physical manual that comes with the unit before installing.

## Pages Updated

- [[battery-management]]
