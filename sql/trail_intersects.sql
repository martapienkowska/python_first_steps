drop table if exists sel_id;
create temporary table sel_id as
select distinct -osm_id trail, way, tags -> 'route_name' tag from planet_osm_line where osm_id < 0;

select distinct t1.trail trail1, t2.trail trail2, t1.tag tag1, t2.tag tag2, t1.way geom1, t2.way geom2 from sel_id t1
join sel_id t2
on St_intersects(t1.way, t2.way)
and t1.trail <> t2.trail;
