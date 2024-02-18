import pandas # required for parsing excel and csv
import os # required for file handling
import argparse # required for parameter handling

def parse_and_print(filename: str, saccount: str, sdate: str, spayee: str, smemo: str, samount: str, output_dir: str):
    
    df=pandas.read_excel(filename)
    df.rename(columns={sdate: 'Date', spayee: 'Payee', smemo: 'Memo', samount:'Amount'}, inplace=True, errors="raise")
    grouped=df.groupby(saccount)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for name, group in grouped:
        subset = group[["Date","Payee","Memo","Amount"]]
        file_path = os.path.join(output_dir, f'{name}.csv')
        subset.to_csv(file_path, index=False)

def main():
    parser = argparse.ArgumentParser(description='Reads a Finanzguru XLSX Export File and writes one YNAB CSV import file per account.')
    parser.add_argument('-f', '--filename', type=str, help='The filename to read, default: export.xlsx', default='export.xlsx')
    parser.add_argument('-saccount', '--string_account', type=str, help='String for the Account column, default: Name Referenzkonto', default='Name Referenzkonto')
    parser.add_argument('-sdate', '--string_date', type=str, help='String for the Date column, default: Buchungstag', default='Buchungstag')
    parser.add_argument('-spayee', '--string_payee', type=str, help='String for the Payee column, default: Beguenstigter/Auftraggeber', default='Beguenstigter/Auftraggeber')
    parser.add_argument('-smemo', '--string_memo', type=str, help='String for the Memo column, default: Verwendungszweck', default='Verwendungszweck')
    parser.add_argument('-samount', '--string_amount', type=str, help='String for the Amount column, default: Betrag', default='Betrag')
    parser.add_argument('-o', '--output_dir', type=str, help='Path of the output directory, default: output_csv_files', default='output_csv_files')
    args = parser.parse_args()
    # Call the function with the provided filename and optional strings
    parse_and_print(args.filename, args.string_account, args.string_date, args.string_payee, args.string_memo, args.string_amount, args.output_dir)

if __name__ == "__main__":
    main()
