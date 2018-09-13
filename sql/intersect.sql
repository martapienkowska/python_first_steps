

drop table if exists marta.intersect1;
create table marta.intersect1
as select distinct t1.osm_id, t2.osm_id id2, t2.way, t1.way w2
from planet_osm_line t1
join planet_osm_line t2
on St_intersects(t1.way, t2.way);
