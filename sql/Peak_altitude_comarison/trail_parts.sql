select tt.* from
(select unnest(parts) as w_id from planet_osm_rels where id=1593519) t
join planet_osm_ways tt on t.w_id = tt.id;