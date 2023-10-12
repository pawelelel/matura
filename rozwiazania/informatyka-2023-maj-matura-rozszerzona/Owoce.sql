select count(*) from

(
SELECT dostawa_porzeczek, data from Owoce
where dostawa_porzeczek > dostawa_malin and dostawa_porzeczek > dostawa_truskawek
order by dostawa_porzeczek DESC
)
)