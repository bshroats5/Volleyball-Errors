# data for EKU Volleyball

# Load the data
import gspread
import pandas as pd
import matplotlib.pyplot as plt

gc = gspread.service_account(filename="G:\My Drive\eku-volleyball-ee9b3ab669dc.json")
sh = gc.open_by_key('13-EHOL6j4ZpvZoMnQy2W1k3XQnhtMbv1KgKy3fCYyxk')
worksheet = sh.sheet1
data = worksheet.get_all_records()
df = pd.DataFrame(data)

# Average errors per match
average_errors_per_match = df['# of Errors'].mean()

# Average errors in wins
df_wins = df[df['Result'] == 'W']
average_errors_in_wins = df_wins['# of Errors'].mean()

# Average errors in losses
df_losses = df[df['Result'] == 'L']
average_errors_in_losses = df_losses['# of Errors'].mean()

# Average errors in home matches
df_home = df[df['Home or Away'] == 'Home']
average_errors_in_home = df_home['# of Errors'].mean()

# Average errors in away matches
df_away = df[df['Home or Away'] == 'Away']
average_errors_in_away = df_away['# of Errors'].mean()

# Data to plot
n_matches = [len(df), len(df_wins), len(df_losses), len(df_home), len(df_away)]
avg_errors = [average_errors_per_match, average_errors_in_wins, average_errors_in_losses, average_errors_in_home,
              average_errors_in_away]

# Create a bar plot
plt.bar(team_names, error_counts, color='maroon')

# Create plot
plt.bar(range(len(n_matches)), avg_errors, tick_label=['Total', 'Wins', 'Losses', 'Home', 'Away'])
plt.ylabel('Average Errors')
plt.title('Average Errors per Match Type')
plt.show()
