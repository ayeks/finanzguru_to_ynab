# Finanzguru to YNAB

A Python script for parsing Finanzguru XLSX export files and generating individual YNAB CSV import files per account.

## Installation

Clone this repo and install it with:

```bash
pip install .
```

## Usage

Go to your Finanzguru app and export your transactions. Copy the file into the directory where this script is located. Rename it to `export.xlsx` if you want to use the defaults.

Run it locally and how the help:

```bash
% finanzguru_to_ynab -h
usage: finanzguru_to_ynab [-h] [-f FILENAME] [-saccount STRING_ACCOUNT] [-sdate STRING_DATE]
                          [-spayee STRING_PAYEE] [-smemo STRING_MEMO] [-samount STRING_AMOUNT]
                          [-o OUTPUT_DIR]

Reads a Finanzguru XLSX Export File and writes one YNAB CSV import file per account.

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        The filename to read, default: export.xlsx
  -saccount STRING_ACCOUNT, --string_account STRING_ACCOUNT
                        String for the Account column, default: Name Referenzkonto
  -sdate STRING_DATE, --string_date STRING_DATE
                        String for the Date column, default: Buchungstag
  -spayee STRING_PAYEE, --string_payee STRING_PAYEE
                        String for the Payee column, default: Beguenstigter/Auftraggeber
  -smemo STRING_MEMO, --string_memo STRING_MEMO
                        String for the Memo column, default: Verwendungszweck
  -samount STRING_AMOUNT, --string_amount STRING_AMOUNT
                        String for the Amount column, default: Betrag
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
                        Path of the output directory, default: output_csv_files
```

Run it with the default settings:

```bash
finanzguru_to_ynab
```

Or run the python script directly:

```bash
python finanzguru_to_ynab/run.py -f export.xlsx -saccount "Account" -sdate "Date" -spayee "Payee" -smemo "Memo" -samount "Amount" -o "output_dir"
```

In YNAB you can import each account specific CSV file afterwards.

## Options

Explain the available options and parameters. Include default values and how users can customize the behavior of your project.

- `-f`, --filename: The filename to read. Default: `export.xlsx`
- `-saccount`: String for the Account column. Default: `Name Referenzkonto`
- `-sdate`: String for the Date column. Default: `Buchungstag`
- `-spayee`: String for the Payee column. Default: `Beguenstigter/Auftraggeber`
- `-smemo`: String for the Memo column. Default: `Verwendungszweck`
- `-samount`: String for the Amount column. Default: `Betrag`
- `-o`: Path of the output directory, default: `output_csv_files`

## Testing

Explain how to run tests and include any test coverage information.

```bash
% pytest
============================================ test session starts ============================================
platform darwin -- Python 3.9.6, pytest-8.0.1, pluggy-1.4.0
rootdir: /Users/lars/git/finanzguru-to-ynab
collected 1 item                                                                                            

tests/test_run.py .                                                                                   [100%]

============================================= 1 passed in 0.42s =============================================
```

## Contributing

Provide guidelines for contributions. Include information about how to report issues, submit feature requests, and contribute to the codebase.


