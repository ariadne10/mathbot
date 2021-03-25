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
    sum_row = df.sum(axis=0)
    print(sum_row)

# Only show values that are greater than 25
    df = pd.read_excel(spreadsheet_file, sheet_name, header=1)
    df = df[[player, value]].where(df[value] > 25)
    df = df.dropna()

# Organize from largest to smallest
    df = df.sort_values(by='THIS WEEK', ascending=False).head(70)

# Weekly fees value are inserted into a row at the bottom of winners list
    data = [{player: 'Fees', value: 5000}]
    df.loc[99] = list(data[0].values())
# Zane's profit value is inserted into a row at the bottom of winners list
    data = [{player: 'Zane', value: 5000}]
    df.loc[100] = list(data[0].values())
# Austin's profit value is inserted into a row at the bottom of winners list
    data = [{player: 'Austin', value: 5000}]
    df.loc[101] = list(data[0].values())
# Ryan's profit value is inserted into a row at the bottom of winners list
    data = [{player: 'Ryan', value: 5000}]
    df.loc[102] = list(data[0].values())

    print(df)

# If losers value is greater than the winner value that it needs to satisfy then it copies that number

# The difference of the losers value is then used to help satisfy the next winners value below

# Print date of payout
