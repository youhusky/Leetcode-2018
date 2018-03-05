#
# [182] Duplicate Emails
#
# https://leetcode.com/problems/duplicate-emails/description/
#
# database
# Easy (44.55%)
# Total Accepted:    60.4K
# Total Submissions: 135.6K
# Testcase Example:  '{"headers": {"Person": ["Id", "Email"]}, "rows": {"Person": [[1, "a@b.com"], [2, "c@d.com"], [3, "a@b.com"]]}}'
#
# 
# Write a SQL query to find all duplicate emails in a table named Person.
# 
# 
# +----+---------+
# | Id | Email   |
# +----+---------+
# | 1  | a@b.com |
# | 2  | c@d.com |
# | 3  | a@b.com |
# +----+---------+
# 
# 
# For example, your query should return the following for the above table:
# 
# +---------+
# | Email   |
# +---------+
# | a@b.com |
# +---------+
# 
# 
# Note: All emails are in lowercase.
#
# Write your MySQL query statement below
select Email
from Person
group by Email
having count(Email) > 1;
