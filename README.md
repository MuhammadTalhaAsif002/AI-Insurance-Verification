# AI Insurance Verification Workflow

A Claude-assisted workflow that transforms unstructured insurance verification notes into standardized, review-ready information.

## Overview

Insurance verification teams often work with unstructured notes containing patient information, insurance details, eligibility information, deductibles, copays, referrals, and authorization requirements.

This project demonstrates how Claude can assist with this repetitive knowledge-work process by:

- Extracting relevant information
- Structuring unorganized notes
- Identifying missing or uncertain information
- Prioritizing items requiring human review
- Measuring potential workflow efficiency

The system follows a **human-in-the-loop** approach. AI assists with information preparation and organization, while final verification remains the responsibility of a human reviewer.

---

## Workflow

```text
Unstructured Insurance Note
            ↓
       Claude AI
            ↓
   Information Extraction
            ↓
     Structured JSON
            ↓
       Validation
            ↓
      Human Review
            ↓
   Performance Evaluation
            ↓
      Operations Dashboard
