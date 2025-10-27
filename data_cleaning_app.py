import os
import pandas as pd
import re
from datetime import datetime

# create a function to normalize the date
def normalize_date(date_str):
    """Convert multiple date formats into YYYY-MM-DD."""
    if not date_str:
        return None

    date_str = date_str.strip()

    # Common known formats
    known_formats = [
        "%m/%d/%Y", "%Y-%m-%d", "%m-%d-%Y",
        "%b %d %Y", "%B %d %Y", "%d %B %Y"
    ]

    for fmt in known_formats:
        try:
            return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue

    # If we get here, try automatic fuzzy parsing
    try:
        parsed = pd.to_datetime(date_str, errors="coerce")
        if pd.notna(parsed):
            return parsed.strftime("%Y-%m-%d")
    except Exception:
        pass

    return None


def preprocess_lines(lines):
    """Combine split names, remove junk lines, normalize spacing."""
    cleaned = []
    buffer = ""

    for line in lines:
        line = line.strip()

        # Skip notes or labeled text
        if not line or "Labeled" in line or line.lower().startswith("total"):
            continue

        # Merge split provider names (Engel-\nHughes or MT\nWASHINGT\nON)
        if line.endswith("-") or re.match(r"^[A-Z]{1,2}$", line):
            buffer += line.replace("-", "") + " "
            continue

        if buffer:
            line = buffer + line
            buffer = ""

        # Collapse multiple spaces
        line = re.sub(r"\s+", " ", line)

        cleaned.append(line)

    return cleaned


def parse_records(lines):
    """Extract structured payment info from cleaned text lines."""
    records = []
    current_date = None

    for line in lines:
        # Detect dates in various formats
        if re.match(r"^(\d{1,2}/\d{1,2}/\d{4}|\d{4}-\d{1,2}-\d{1,2}|[A-Za-z]+\s\d{1,2}\s\d{4})$", line):
            current_date = normalize_date(line)
            continue

        if not current_date:
            continue

        parts = line.split()
        if len(parts) < 3:
            continue

        # Find numeric tokens
        nums = [p for p in parts if re.match(r"^\$?\d+(\.\d+)?$", p)]
        if len(nums) < 2:
            continue

        # Extract main fields
        if len(parts) >= 6:
            provider = " ".join(parts[:-5])
            charge, paid, insurance, parent, balance = parts[-5:]
        elif len(parts) == 5:
            provider, charge, paid, insurance, parent = parts
            balance = 0
        elif len(parts) == 4:
            provider, charge, paid, insurance = parts
            parent, balance = 0, 0
        else:
            continue

        try:
            charge = float(charge.replace(",", "").replace("$", ""))
            paid = float(paid.replace(",", "").replace("$", ""))
            parent = float(str(parent).replace(",", "").replace("$", ""))
            balance = float(str(balance).replace(",", "").replace("$", ""))
        except ValueError:
            continue

        records.append({
            "Date": current_date,
            "Provider": provider.replace("-", "").strip(),
            "Charge": charge,
            "Paid": paid,
            "Insurance": insurance.strip(),
            "Parent Portion": parent,
            "Balance": balance
        })

    return records


def clean_payment_data(input_file):
    """Main function: process text file and export Excel."""
    with open(input_file, "r", encoding="utf-8") as f:
        raw_lines = f.readlines()

    lines = preprocess_lines(raw_lines)
    records = parse_records(lines)

    if not records:
        print("❌ No valid records found — check formatting.")
        return

    df = pd.DataFrame(records)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.sort_values(by="Date", ascending=False)

    output_file = os.path.splitext(input_file)[0] + "_autofixed.xlsx"
    df.to_excel(output_file, index=False)
    print(f"✅ Cleaned data saved to: {output_file}")
    print(f"📊 {len(df)} valid records exported.")


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    print("📂 Current folder:", script_dir)

    txt_files = [f for f in os.listdir(script_dir) if f.lower().endswith(".txt")]

    if not txt_files:
        print("❌ No .txt files found. Place them in the same folder as this script.")
    else:
        print("\n📄 Available text files:")
        for i, f in enumerate(txt_files, start=1):
            print(f"{i}. {f}")

        while True:
            choice = input("\nEnter the number of the file to clean: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(txt_files):
                chosen = txt_files[int(choice) - 1]
                print(f"\n🔍 Auto-cleaning and normalizing dates: {chosen}\n")
                clean_payment_data(chosen)
                break
            else:
                print("❌ Invalid choice. Try again.")

