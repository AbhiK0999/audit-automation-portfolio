import pandas as pd

def reconcile(bank_file, ledger_file):
    bank = pd.read_csv(bank_file)
    ledger = pd.read_csv(ledger_file)

    bank['Amount'] = bank['Amount'].round(2)
    ledger['Amount'] = ledger['Amount'].round(2)

    matched = pd.merge(bank, ledger, on='Amount', how='inner')

    unmatched_bank = bank[~bank['Amount'].isin(matched['Amount'])]
    unmatched_ledger = ledger[~ledger['Amount'].isin(matched['Amount'])]

    return matched, unmatched_bank, unmatched_ledger

if __name__ == "__main__":
    matched, unmatched_bank, unmatched_ledger = reconcile(
        "bank_statement.csv",
        "ledger.csv"
    )

    print("Matched Transactions:")
    print(matched)

    print("\nUnmatched Bank Transactions:")
    print(unmatched_bank)

    print("\nUnmatched Ledger Transactions:")
    print(unmatched_ledger)

    matched.to_csv("matched.csv", index=False)
    unmatched_bank.to_csv("unmatched_bank.csv", index=False)
    unmatched_ledger.to_csv("unmatched_ledger.csv", index=False)
