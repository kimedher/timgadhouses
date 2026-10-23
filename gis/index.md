---
layout: page
title: City Map
subtitle: The city, digitized block by block.
permalink: /gis/
last_updated: 2026-10-22
---

## The live map

Every feature below was drawn in QGIS from georeferenced satellite imagery, checked against the historical excavation plans, and exported directly from the project's spatial database. The map grows in two tiers. The base city is mapped: the blocks of the grid (shaded yellow), the roads, the gates, the baths, and the public and religious buildings. The houses go on as they are drawn, each in blue over its block, and they are only the first of the {{ site.data.houses.count }} houses in the [catalog](/houses/catalog/). Zoom in on a drawn house and its courts, mosaics and paving, stairs, basins and wells, and workshops come up over the imagery.

<p style="margin: 2rem 0;">
  <a href="/gis/viewer.html" style="display: inline-block; background: var(--teal); color: white; padding: 0.8rem 1.4rem; border-radius: var(--radius); border: none; font-weight: 600; font-size: 0.95rem;">Open the full-screen map &rarr;</a>
</p>

<iframe src="/gis/viewer.html" class="grid-viewer-frame" title="Live GIS map of Timgad"></iframe>

Click any feature for its identification, French name, dating, and certainty level; drawn houses link through to their records in the [catalog](/houses/catalog/). Public building identifications follow the published excavation literature (Ballu, Boeswillwald–Cagnat–Ballu, Gsell, Germain); dates and attributions marked *uncertain* are flagged in the data itself, in keeping with the project's [methods](/methods/).

## How this map is made

The workflow runs from QGIS to the web with no hand-editing: features are digitized block by block over georeferenced satellite imagery (with the Ballu, Cagnat, and Boeswillwald plans as control), stored in a single GeoPackage database, and exported to the open GeoJSON files that power this page. The same database drives the [house catalog](/houses/catalog/) and the [interactive grid](/grid/), so the map, the catalog, and the grid stay consistent with one another as the work proceeds.

Current focus: drawing the houses with usable excavation records one by one, following the digitizing protocol in the project methods. Each house goes onto the map once its drawing is finished, and the houses known only from the city plan will follow.

*Treat anything on this page as in-progress visualization rather than a final research output. Spatial data will be released alongside the database when the digitization phase is complete.*
