# AI Insurance Verification Workflow

A Claude-assisted workflow that transforms unstructured insurance verification notes into standardized, review-ready information.

Live Demo Link : https://bsvmxdtunsms5x6rbjrsy5.streamlit.app/

<img width="1901" height="804" alt="image" src="https://github.com/user-attachments/assets/80e5f859-4a8b-4f31-9979-db92bcab7d6b" />




<img width="1232" height="428" alt="image" src="https://github.com/user-attachments/assets/811ffbc3-e97a-470b-a347-65d4f5c3713f" />




## Overview

Insurance verification teams often work with unstructured notes containing patient information, insurance details, eligibility information, deductibles, copays, referrals, and authorization requirements.

This project demonstrates how Claude can assist with this repetitive knowledge-work process by:

- Extracting relevant information
- Structuring unorganized notes
- Identifying missing or uncertain information
- Prioritizing items requiring human review
- Measuring potential workflow efficiency

The system follows a **human-in-the-loop** approach. AI assists with information preparation and organization, while final verification remains the responsibility of a human reviewer.

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
```

## Key Features

* Converts unstructured insurance notes into structured information
* Classifies information as `CONFIRMED`, `MISSING`, or `NEEDS_VERIFICATION`
* Detects incomplete and uncertain information
* Generates human-review action items
* Validates structured AI output using Python
* Supports processing multiple insurance notes
* Evaluates potential processing-time improvements
* Provides an interactive Streamlit operations dashboard
* Uses fictional data for all demonstrations

## Example

### Input

```text
Insurance Verification Note

Patient: Sarah Ahmed
DOB: 03/17/1998

Primary insurance: Blue Horizon Health
Member ID: BH458921
Group #: GRP7821
Plan: PPO

Coverage was checked through the payer portal and appears active.

Specialist copay is $40.
Deductible is $1,500, with $900 remaining.
Coinsurance is 20%.

The representative could not confirm whether prior authorization
is required for this particular procedure.

Referral requirement was not confirmed.
```

### AI-Assisted Output

| Field               | Value               | Status             |
| ------------------- | ------------------- | ------------------ |
| Patient             | Sarah Ahmed         | CONFIRMED          |
| Insurance           | Blue Horizon Health | CONFIRMED          |
| Member ID           | BH458921            | CONFIRMED          |
| Group Number        | GRP7821             | CONFIRMED          |
| Plan                | PPO                 | CONFIRMED          |
| Coverage            | Active              | CONFIRMED          |
| Deductible          | $1,500              | CONFIRMED          |
| Copay               | $40                 | CONFIRMED          |
| Coinsurance         | 20%                 | CONFIRMED          |
| Prior Authorization | Not confirmed       | NEEDS_VERIFICATION |
| Referral            | Not confirmed       | NEEDS_VERIFICATION |

The workflow also generates specific follow-up actions for information requiring human verification.

## Performance Evaluation

An illustrative benchmark was created using **4 fictional insurance verification notes** to demonstrate how workflow impact could be measured.

| Metric                              | Illustrative Result |
| ----------------------------------- | ------------------: |
| Notes evaluated                     |                   4 |
| Average manual processing time      |            8.25 min |
| Average AI-assisted processing time |            3.38 min |
| Average potential time saved        |                ~59% |
| Total manual processing time        |              33 min |
| Total AI-assisted processing time   |            13.5 min |
| Total potential time saved          |            19.5 min |

### Important

These timing figures are **simulated benchmark values** created for portfolio demonstration purposes. They are not production performance claims.

The evaluation framework is designed so that real operational timings could be substituted when the workflow is tested with actual users.

## Human-in-the-Loop Design

The workflow intentionally does not allow the AI to make unsupported assumptions.

For example:

```text
Prior Authorization
Value: Not confirmed
Status: NEEDS_VERIFICATION
```

Instead of assuming:

```text
Prior Authorization
Value: No
```

This reduces the risk of treating missing information as confirmed information.

The workflow therefore separates:

* **Confirmed information**
* **Missing information**
* **Information requiring verification**

## Technology

* Python
* Claude
* Prompt Engineering
* Pandas
* Streamlit
* JSON
* Git & GitHub

## Project Structure

```text
AI-Insurance-Verification/
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── input/
│   └── output/
│
├── evaluation/
│   ├── evaluation_results.csv
│   └── evaluate.py
│
├── prompts/
│   └── verification_prompt.txt
│
├── src/
│   ├── main.py
│   └── process_result.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Dashboard

The Streamlit dashboard provides an operational view of the workflow.

### Dashboard Metrics

* Notes processed
* Average time saved
* Average minutes saved per note
* Cases requiring human review
* Manual vs AI-assisted processing time
* Time saved by verification note
* Verification performance
* Human-review action items

Run the dashboard locally:

```bash
streamlit run dashboard/app.py
```

## AI Workflow

The core Claude workflow instructs the model to:

1. Extract information explicitly present in the note
2. Avoid inventing missing information
3. Normalize extracted information
4. Identify missing fields
5. Identify ambiguous information
6. Flag information requiring human verification
7. Generate a standardized verification summary
8. Return structured JSON

## Current Implementation

The Claude extraction stage is currently demonstrated through Claude's web interface.

Python handles:

* Structured-result processing
* Validation
* Multiple-note processing
* Performance evaluation
* Dashboard visualization

This approach allows the workflow to be demonstrated without requiring an API key.

## Future Improvements

* Claude API integration for end-to-end automation
* Batch processing of incoming verification notes
* Confidence scoring
* Additional validation rules
* Workflow usage and adoption tracking
* Exportable verification reports
* Integration with operational systems
* Real-user timing and accuracy evaluation

## Data Privacy

All patient and insurance information included in this repository is **fictional** and created solely for demonstration purposes.

No real patient records or protected health information are included.

## Design Principles

### Human Oversight

AI assists with repetitive information-processing tasks while humans remain responsible for final verification.

### Accuracy Over Assumptions

The workflow explicitly distinguishes between confirmed, missing, and uncertain information.

### Measurable Impact

The project includes an evaluation framework to measure processing time and potential operational impact.

### Reusable Workflows

The prompt, processing logic, and evaluation components are separated so the workflow can be adapted to similar knowledge-work processes.

## Disclaimer

This project is a portfolio demonstration and is not intended for real-world medical, insurance, clinical, or legal decision-making.
