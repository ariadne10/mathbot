# Import previous weeks excel sheet
import pandas as pd

spreadsheet_file = pd.ExcelFile('/Users/ryanmelink/Downloads/PA2284400_BettorBalance.xlsx')
worksheets = spreadsheet_file.sheet_names
appended_data = []


for sheet_name in worksheets:
    value = "THIS WEEK"
    player = "AGENT"

# Only show values that are less than -25
    df = pd.read_excel(spreadsheet_file, sheet_name, header=1)
    df = df[[player, value]].where(df[value] < - 25)
    df = df.dropna()

# Drop 'Grand Total' row
    df = df.drop(df.index[[0]])

# Drop 'Total' / Last row
    df.drop(df.tail(1).index, inplace=True)

# Organize from smallest to largest
    df = df.sort_values(by='THIS WEEK', ascending=False).head(70)

# Turn all negative numbers to positive
    df['THIS WEEK'] = df['THIS WEEK'].abs()

    print(df)

# Add losers values to satisfy winners values starting from top of each list
    column_number = 2
    total = df.iloc[:, column_number - 1:column_number].sum()
    print(total)


# Only show values that are greater than 25
    df = pd.read_excel(spreadsheet_file, sheet_name, header=1)
    df = df[[player, value]].where(df[value] > 25)
    df = df.dropna()

# Organize from largest to smallest
    df = df.sort_values(by='THIS WEEK', ascending=False).head(70)

# Weekly fees value are inserted into a row at the bottom of winners list
    data = [{player: 'Fees', value: 800}]
    df.loc[99] = list(data[0].values())
# greg profit value is inserted into a row at the bottom of winners list
    data = [{player: 'greg', value: 3000}]
    df.loc[100] = list(data[0].values())
# steve profit value is inserted into a row at the bottom of winners list
    data = [{player: 'steve', value: 3000}]
    df.loc[101] = list(data[0].values())
# mike profit value is inserted into a row at the bottom of winners list
    data = [{player: 'mike', value: 3000}]
    df.loc[102] = list(data[0].values())

    print(df)

    column_number = 2
    total = df.iloc[:, column_number - 1:column_number].sum()
    print(total)

# If losers value is greater than the winner value that it needs to satisfy then it copies that number

# The difference of the losers value is then used to help satisfy the next winners value below

# Print date of payout
