# Write your MySQL query statement below
select DISTINCT  p.email AS Email FROM Person p INNER JOIN PersoN p1 ON p.id <> p1.id WHERE p.email= p1.email