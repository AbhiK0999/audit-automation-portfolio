import pandas as pd

def detect_duplicates(file_path):
    df = pd.read_csv(file_path)

    df['Invoice Number'] = df['Invoice Number'].astype(str).str.strip()
    df['Amount'] = df['Amount'].round(2)

    duplicates = df[df.duplicated(
        subset=['Invoice Number', 'Invoice Date', 'Amount'],
        keep=False
    )]

    return duplicates

if __name__ == "__main__":
    file = "sample_invoices.csv"
    result = detect_duplicates(file)

    if result.empty:
        print("No duplicate invoices found.")
    else:
        print("Duplicate invoices detected:")
        print(result)
        result.to_csv("duplicate_output.csv", index=False)
