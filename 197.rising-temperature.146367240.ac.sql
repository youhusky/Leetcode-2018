#
# [197] Rising Temperature
#
# https://leetcode.com/problems/rising-temperature/description/
#
# database
# Easy (31.01%)
# Total Accepted:    44.8K
# Total Submissions: 144.4K
# Testcase Example:  '{"headers": {"Weather": ["Id", "Date", "Temperature"]}, "rows": {"Weather": [[1, "2015-01-01", 10], [2, "2015-01-02", 25], [3, "2015-01-03", 20], [4, "2015-01-04", 30]]}}'
#
# Given a Weather table, write a SQL query to find all dates' Ids with higher
# temperature compared to its previous (yesterday's) dates.
# 
# 
# +---------+------------+------------------+
# | Id(INT) | Date(DATE) | Temperature(INT) |
# +---------+------------+------------------+
# |       1 | 2015-01-01 |               10 |
# |       2 | 2015-01-02 |               25 |
# |       3 | 2015-01-03 |               20 |
# |       4 | 2015-01-04 |               30 |
# +---------+------------+------------------+
# 
# 
# For example, return the following Ids for the above Weather table:
# 
# +----+
# | Id |
# +----+
# |  2 |
# |  4 |
# +----+
# 
#
SELECT wt1.Id 
FROM Weather wt1, Weather wt2
WHERE wt1.Temperature > wt2.Temperature AND 
      TO_DAYS(wt1.DATE)-TO_DAYS(wt2.DATE)=1;
