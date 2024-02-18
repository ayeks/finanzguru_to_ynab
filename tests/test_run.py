import os
import pandas as pd
import pytest
from finanzguru_to_ynab.run import parse_and_print

@pytest.fixture
def sample_data(tmpdir):
    # Create a sample Excel file for testing
    filename = os.path.join(tmpdir, 'test_data.xlsx')
    df = pd.DataFrame({
        'Buchungstag': ['2022-01-01', '2022-01-01', '2022-01-02'],
        'Beguenstigter/Auftraggeber': ['Payee1', 'Payee2', 'Payee1'],
        'Verwendungszweck': ['Memo1', 'Memo2', 'Memo3'],
        'Betrag': [100, 150, 200],
        'Name Referenzkonto': ['Account1', 'Account2', 'Account1']
    })
    df.to_excel(filename, index=False)
    return filename

def test_parse_and_print(sample_data):
    # Set up
    saccount = 'Name Referenzkonto'
    sdate = 'Buchungstag'
    spayee = 'Beguenstigter/Auftraggeber'
    smemo = 'Verwendungszweck'
    samount = 'Betrag'
    odir = 'output_test'

    # Call the function
    parse_and_print(sample_data, saccount, sdate, spayee, smemo, samount, odir)

    # Check if output files are created
    assert os.path.exists(odir)

    # Check if individual output files are created for each account
    assert os.path.exists(os.path.join(odir, 'Account1.csv'))
    assert os.path.exists(os.path.join(odir, 'Account2.csv'))

    # Check the content of the output files
    df_account1 = pd.read_csv(os.path.join(odir, 'Account1.csv'))
    df_account2 = pd.read_csv(os.path.join(odir, 'Account2.csv'))

    assert len(df_account1) == 2  # Number of entries for Account1
    assert len(df_account2) == 1  # Number of entries for Account2

    # Add more specific checks based on your requirements
    # For example, check specific values in the DataFrames
    assert df_account1['Amount'].sum() == 300
    assert 'Memo1' in df_account1['Memo'].values
