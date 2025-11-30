import pandas as pd

sql = """
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT DISTINCT e.salary
      FROM Employee e
      WHERE N = (
          SELECT COUNT(DISTINCT salary)
          FROM Employee
          WHERE salary >= e.salary
      )
      LIMIT 1
  );
END
"""

# pandas version

Employee = pd.DataFrame({"id": [1, 2, 3, 4, 5], "salary": [100, 200, 300, 400, 500]})
# get the nth highest salary
N = 2
result = Employee.sort_values(by="salary", ascending=False).iloc[N - 1]

result_talbe = pd.DataFrame({"Nth Highest Salary": result.iloc[1]}, index=[0])

print(result_talbe)
