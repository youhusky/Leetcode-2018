#
# [601] Human Traffic of Stadium
#
# https://leetcode.com/problems/human-traffic-of-stadium/description/
#
# database
# Hard (33.67%)
# Total Accepted:    4.7K
# Total Submissions: 14K
# Testcase Example:  '{"headers": {"stadium": ["id", "date", "people"]}, "rows": {"stadium": [[1, "2017-01-01", 10], [2, "2017-01-02", 109], [3, "2017-01-03", 150], [4, "2017-01-04", 99], [5, "2017-01-05", 145], [6, "2017-01-06", 1455], [7, "2017-01-07", 199], [8, "2017-01-08", 188]]}}'
#
# X city built a new stadium, each day many people visit it and the stats are
# saved as these columns: id, date, people
# 
# Please write a query to display the records which have 3 or more consecutive
# rows and the  amount of people more than 100(inclusive).
# 
# ⁠
# For example, the table stadium:
# 
# +------+------------+-----------+
# | id   | date       | people    |
# +------+------------+-----------+
# | 1    | 2017-01-01 | 10        |
# | 2    | 2017-01-02 | 109       |
# | 3    | 2017-01-03 | 150       |
# | 4    | 2017-01-04 | 99        |
# | 5    | 2017-01-05 | 145       |
# | 6    | 2017-01-06 | 1455      |
# | 7    | 2017-01-07 | 199       |
# | 8    | 2017-01-08 | 188       |
# +------+------------+-----------+
# 
# 
# For the sample data above, the output is:
# 
# 
# +------+------------+-----------+
# | id   | date       | people    |
# +------+------------+-----------+
# | 5    | 2017-01-05 | 145       |
# | 6    | 2017-01-06 | 1455      |
# | 7    | 2017-01-07 | 199       |
# | 8    | 2017-01-08 | 188       |
# +------+------------+-----------+
# 
# 
# Note:
# Each day only have one row record, and the dates are increasing with id
# increasing.
# ⁠
#
SELECT t.* FROM stadium t
    LEFT JOIN stadium p1 ON t.id - 1 = p1.id
    LEFT JOIN stadium p2 ON t.id - 2 = p2.id
    LEFT JOIN stadium n1 ON t.id + 1 = n1.id
    LEFT JOIN stadium n2 ON t.id + 2 = n2.id
WHERE (t.people >= 100 AND p1.people >= 100 AND p2.people >= 100)
     OR (t.people >= 100 AND n1.people >= 100 AND n2.people >= 100)
     OR (t.people >= 100 AND n1.people >= 100 AND p1.people >= 100)
ORDER BY id;
