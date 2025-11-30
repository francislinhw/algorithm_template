# https://leetcode.com/problems/combine-two-tables/?envType=problem-list-v2&envId=database
# Write your MySQL query statement below

import pandas as pd


sql = """
WITH MERGED AS (
    SELECT     
    p.firstName,
    p.lastName,
    a.city,
    a.state FROM Person p
    LEFT JOIN Address a ON a.personId = p.personId
)
SELECT firstName, lastName, city, state FROM 
"""

# pandas version

Person = pd.DataFrame()
Address = pd.DataFrame()

result = pd.merge(Person, Address, on="personId", how="left")
print(result)
