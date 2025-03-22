# visualize how key features from your dataset to understand how attack traffic differs from normal traffic.
# To understand the raw distribution 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load Datset
train_df = pd.read_csv("UNSW_NB15_training-set.csv")
test_df = pd.read_csv("UNSW_NB15_testing-set.csv")

# Convert categorical values to numeric (if needed)
train_df['label'] = train_df['label'].astype(int)
test_df['label'] = test_df['label'].astype(int)

# Feature selection (example: packet size, duration)
features_to_plot = ['sbytes', 'dbytes', 'dur', 'sinpkt']

# Plot distributions for normal vs attack traffic
for feature in features_to_plot:
    plt.figure(figsize=(8, 5))
    sns.histplot(train_df, x=feature, hue="label", bins=50, kde=True)
    plt.title(f"Distribution of {feature} for Normal vs Attack Traffic")
    plt.xlabel(feature)
    plt.ylabel("Count")
    plt.legend(title="Traffic Type", labels=["Normal (0)", "Attack (1)"])
    plt.show()
