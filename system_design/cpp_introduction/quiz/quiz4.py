import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:

    # Your code starts here
    def classify_income(income):
        if income < 20000:
            return "Low Salary"
        elif income <= 50000:
            return "Average Salary"
        else:
            return "High Salary"

    accounts["category"] = accounts["income"].apply(lambda x: classify_income(x))
    result = (
        accounts.groupby("category")
        .agg({"account_id": "count"})
        .rename(columns={"account_id": "accounts_count"})
    )
    if "Low Salary" not in result.index:
        result.loc["Low Salary"] = 0
    if "Average Salary" not in result.index:
        result.loc["Average Salary"] = 0
    if "High Salary" not in result.index:
        result.loc["High Salary"] = 0
    result = result.loc[["Low Salary", "Average Salary", "High Salary"], :]
    return result

    # Your code ends here


accounts1 = pd.DataFrame(
    {"account_id": [3, 2, 8, 6], "income": [108939, 12747, 87709, 91796]}
)
accounts2 = pd.DataFrame({"account_id": [1, 2, 3], "income": [15000, 30000, 51000]})

print(count_salary_categories(accounts1))
print(count_salary_categories(accounts2))
