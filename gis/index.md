---
layout: page
title: GIS
subtitle: The city, digitized block by block.
permalink: /gis/
last_updated: 2026-08-07
---

## The live map

Every feature below was drawn in QGIS from georeferenced satellite imagery, checked against the historical excavation plans, and exported directly from the project's spatial database. The map grows as digitization proceeds: the base city (insulae, roads, gates, baths, public and religious buildings) is complete, and houses appear one by one as their walls are traced. The houses visible now are only the first of many. Timgad preserves well over a hundred; 73 have excavation records substantial enough to catalog, and those are being traced first. Grey dashed blocks are not yet digitized. Zoom in on a traced house and its courts, mosaics, and water features draw on top of the imagery.

<p style="margin: 2rem 0;">
  <a href="/gis/viewer.html" style="display: inline-block; background: var(--teal); color: white; padding: 0.8rem 1.4rem; border-radius: var(--radius); border: none; font-weight: 600; font-size: 0.95rem;">Open the full-screen map &rarr;</a>
</p>

<iframe src="/gis/viewer.html" class="grid-viewer-frame" title="Live GIS map of Timgad"></iframe>

Click any feature for its identification, French name, dating, and certainty level; traced houses link through to their records in the [catalog](/houses/catalog/). Public building identifications follow the published excavation literature (Ballu, Boeswillwald–Cagnat–Ballu, Gsell, Germain); dates and attributions marked *uncertain* are flagged in the data itself, in keeping with the project's [methods](/methods/).

## How this map is made

The workflow runs from QGIS to the web with no hand-editing: features are digitized block by block over georeferenced satellite imagery (with the Ballu, Cagnat, and Boeswillwald plans as control), stored in a single GeoPackage database, and exported to the open GeoJSON files that power this page. The same database drives the [house catalog](/houses/catalog/) and the [interactive grid](/grid/), so the map, the catalog, and the grid stay consistent with one another as the work proceeds.

Current focus: tracing the walls of the 73 houses with usable excavation records, following the digitizing protocol in the project methods. The remaining houses known only from the city plan will follow.

*Treat anything on this page as in-progress visualization rather than a final research output. Spatial data will be released alongside the database when the digitization phase is complete.*
