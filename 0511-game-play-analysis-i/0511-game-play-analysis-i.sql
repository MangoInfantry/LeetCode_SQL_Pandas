# Write your MySQL query statement below
# activity table -> group by player_id -> event_date 최솟값 min

select player_id, min(event_date) as first_login from activity group by player_id