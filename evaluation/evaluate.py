import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

file_path = BASE_DIR / "evaluation" / "evaluation_results.csv"

df = pd.read_csv(file_path)

df["time_saved_minutes"] = (
    df["manual_time_minutes"]
    - df["ai_assisted_time_minutes"]
)

df["time_saved_percent"] = (
    df["time_saved_minutes"]
    / df["manual_time_minutes"]
    * 100
)

total_manual = df["manual_time_minutes"].sum()
total_ai = df["ai_assisted_time_minutes"].sum()
total_saved = df["time_saved_minutes"].sum()

average_manual = df["manual_time_minutes"].mean()
average_ai = df["ai_assisted_time_minutes"].mean()
average_saved_percent = df["time_saved_percent"].mean()

print("\nAI INSURANCE VERIFICATION EVALUATION")
print("=" * 40)

print(f"Notes tested: {len(df)}")

print(f"\nAverage manual time: {average_manual:.2f} minutes")
print(f"Average AI-assisted time: {average_ai:.2f} minutes")

print(f"\nAverage time saved: {average_saved_percent:.1f}%")

print(f"\nTotal manual time: {total_manual:.2f} minutes")
print(f"Total AI-assisted time: {total_ai:.2f} minutes")
print(f"Total time saved: {total_saved:.2f} minutes")

print("\nPer-note results:")
print(df[
    [
        "note_id",
        "manual_time_minutes",
        "ai_assisted_time_minutes",
        "time_saved_percent"
    ]
].to_string(index=False))