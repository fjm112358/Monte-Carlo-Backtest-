# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 00:19:49 2026

@author: Dylan
"""

#results table
results_df = pd.DataFrame(results)

#Plotiing results 
table_df = results_df.copy()

table_df["Threshold"] = table_df["Threshold"].map(
    lambda x: f"{x:.2f}"
    )
table_df["Sum of Trade Returns"] = table_df["Sum of Trade Returns"].map(
    lambda x: f"{x * 100:.2f}%"
    )
table_df["Average Trade Return"] = table_df["Average Trade Return"].map(
    lambda x: f"{x * 100:.2f}%"
    )
table_df["Win Rate(%)"] = table_df["Win Rate(%)"].map(
    lambda x: f"{x * 100:.2f}%"
    )

fig, ax = plt.subplots(figsize=(12, 4))
ax.axis("off")
table = ax.table(
    cellText=table_df.values,
    colLabels=table_df.columns,
    cellLoc="center",
    loc="center"
)
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1, 2)

plt.tight_layout()
plt.show()