--porownanie wysokosci szczytow z OSM z  Numerycznym Modelem Terenu 100 m dla malopolski (CODGIK)

select distinct on(p.osm_id) p.osm_id, p.name, p.ele, m.h, to_number(p.ele, '9999.99') - m.h diff, p.way, st_transform(m.st_setsrid, 3857)
from planet_osm_point p, malopolska_nmt_geom m
where p.natural = 'peak'
and ST_DWithin(st_transform(m.st_setsrid, 3857), p.way, 100)
and p.ele is not null
order by p.osm_id, st_distance(st_transform(m.st_setsrid, 3857), p.way);
