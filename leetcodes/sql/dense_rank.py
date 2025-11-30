# Write your MySQL query statement below

sql = """
SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) AS 'rank' FROM Scores
"""

# pandas version

import pandas as pd

Scores = pd.DataFrame({"score": [4, 4, 3, 2, 1]})

result = (
    Scores.sort_values(
        by="score",
        ascending=False,
    )
    .reset_index(drop=True)
    .rank(method="dense", ascending=True, na_option="keep")
    .astype(int)
)
result = pd.DataFrame({"score": Scores["score"], "rank": result.iloc[:, 0]})
print(result)
