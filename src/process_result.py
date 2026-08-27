import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_DIR = BASE_DIR / "data" / "input"
OUTPUT_DIR = BASE_DIR / "data" / "output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def validate_result(result):
    required_fields = [
        "patient_name",
        "date_of_birth",
        "insurance_provider",
        "member_id",
        "coverage_status",
        "deductible",
        "copay",
        "coinsurance",
        "human_review_required",
        "review_items"
    ]

    return [
        field for field in required_fields
        if field not in result
    ]


def create_summary(result):
    return {
        "patient": result["patient_name"]["value"],
        "insurance": result["insurance_provider"]["value"],
        "member_id": result["member_id"]["value"],
        "coverage": result["coverage_status"]["value"],
        "human_review_required": result["human_review_required"],
        "review_items": result["review_items"]
    }


def process_file(input_file):

    output_file = OUTPUT_DIR / f"{input_file.stem}.json"

    if not output_file.exists():
        print(f"⚠️ JSON not found for {input_file.name}")
        return

    with open(output_file, "r", encoding="utf-8") as file:
        result = json.load(file)

    missing_fields = validate_result(result)

    if missing_fields:
        print(f"❌ {input_file.name} - Validation failed")
        print(f"Missing: {missing_fields}")
        return

    summary = create_summary(result)

    print(f"\n✅ {input_file.name}")
    print(f"Patient: {summary['patient']}")
    print(f"Insurance: {summary['insurance']}")
    print(f"Coverage: {summary['coverage']}")
    print(f"Human review: {summary['human_review_required']}")

    if summary["review_items"]:
        print("Review items:")
        for item in summary["review_items"]:
            print(f"  - {item}")


def main():

    print("AI Insurance Verification Workflow")
    print("==================================")

    input_files = sorted(INPUT_DIR.glob("*.txt"))

    print(f"Found {len(input_files)} insurance notes.")

    for input_file in input_files:
        process_file(input_file)


if __name__ == "__main__":
    main()