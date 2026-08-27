import json
from pathlib import Path

import pandas as pd
import streamlit as st


# -----------------------------
# Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

CSV_FILE = BASE_DIR / "evaluation" / "evaluation_results.csv"
OUTPUT_DIR = BASE_DIR / "data" / "output"


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Insurance Verification",
    page_icon="🏥",
    layout="wide"
)


# -----------------------------
# Load Data
# -----------------------------

df = pd.read_csv(CSV_FILE)

df["time_saved_minutes"] = (
    df["manual_time_minutes"]
    - df["ai_assisted_time_minutes"]
)

df["time_saved_percent"] = (
    df["time_saved_minutes"]
    / df["manual_time_minutes"]
    * 100
)


# -----------------------------
# Header
# -----------------------------

st.title("AI Insurance Verification")
st.caption(
    "Claude-assisted workflow for structured insurance verification "
    "and human-review prioritization"
)

st.info(
    "Portfolio demonstration using fictional insurance data. "
    "No real patient information is used."
)


# -----------------------------
# KPI Calculations
# -----------------------------

notes_processed = len(df)

avg_manual = df["manual_time_minutes"].mean()
avg_ai = df["ai_assisted_time_minutes"].mean()

avg_saved = df["time_saved_percent"].mean()

avg_minutes_saved = df["time_saved_minutes"].mean()

review_rate = (
    df["review_required"].astype(str).str.lower().eq("true").mean()
    * 100
)


# -----------------------------
# KPI Cards
# -----------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Notes Processed",
    notes_processed
)

col2.metric(
    "Average Time Saved",
    f"{avg_saved:.1f}%"
)

col3.metric(
    "Minutes Saved / Note",
    f"{avg_minutes_saved:.2f}"
)

col4.metric(
    "Human Review Rate",
    f"{review_rate:.0f}%"
)


st.divider()


# -----------------------------
# Processing Time Chart
# -----------------------------

st.subheader("Processing Time")

chart_data = df[
    [
        "note_id",
        "manual_time_minutes",
        "ai_assisted_time_minutes"
    ]
].set_index("note_id")

# st.bar_chart(chart_data)
# st.bar_chart(chart_data)
st.bar_chart(
    chart_data,
    stack=False
)

# -----------------------------
# Time Saved Chart
# -----------------------------

st.subheader("Time Saved by Verification Note")

time_saved_data = df[
    [
        "note_id",
        "time_saved_percent"
    ]
].set_index("note_id")

st.bar_chart(time_saved_data)


# -----------------------------
# Detailed Results
# -----------------------------

st.subheader("Verification Performance")

display_df = df[
    [
        "note_id",
        "manual_time_minutes",
        "ai_assisted_time_minutes",
        "time_saved_minutes",
        "time_saved_percent",
        "review_required",
        "issues_detected"
    ]
].copy()

display_df.columns = [
    "Note",
    "Manual Time (min)",
    "AI-Assisted Time (min)",
    "Time Saved (min)",
    "Time Saved (%)",
    "Human Review",
    "Issues Detected"
]

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)


# -----------------------------
# Review Items
# -----------------------------

st.subheader("Human Review Items")

json_files = sorted(OUTPUT_DIR.glob("*.json"))

for json_file in json_files:

    with open(json_file, "r", encoding="utf-8") as file:
        result = json.load(file)

    review_items = result.get("review_items", [])

    with st.expander(json_file.stem):

        if review_items:

            for item in review_items:
                st.warning(item)

        else:
            st.success("No additional review items.")


# -----------------------------
# Methodology
# -----------------------------

st.divider()

st.subheader("Workflow")

st.markdown(
    """
    **Unstructured Note → Claude Extraction → Structured Data → "
    "Validation → Human Review → Performance Measurement**
    """
)

st.caption(
    "This is a portfolio demonstration. AI-generated results are "
    "intended to assist human reviewers, not replace professional "
    "insurance verification."
)
