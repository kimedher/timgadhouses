---
layout: page
title: Interactive Grid of Timgad
subtitle: The urban plan of Timgad, block by block, with house identifiers mapped to the streets.
permalink: /grid/
show_citation: true
last_updated: 2026-04-18
published: false
---

Timgad was laid out on a strict rectilinear grid, two main streets crossing at right angles with regular rectangular blocks between them. Each block, called an *insula* in Latin, is identified here by its coordinates on that grid. Individual houses are keyed to the insula they sit inside, so that a house identifier like `TIMGAD-C3D5-H01` can be traced directly to its place in the city.

The viewer below is the current working version. It shows the city grid and the identifiers assigned to each block, based on the standardized system described in the [numbering rationale](#numbering-rationale) below. As individual house records are added to the database, they will be linked from their insula.

<p style="margin: 2rem 0;">
  <a href="/grid/viewer.html" style="display: inline-block; background: var(--teal); color: white; padding: 0.8rem 1.4rem; border-radius: var(--radius); border: none; font-weight: 600; font-size: 0.95rem;">Open the full-screen grid &rarr;</a>
</p>

<iframe src="/grid/viewer.html" class="grid-viewer-frame" title="Interactive grid of Timgad"></iframe>

<h2 id="how-to-read-it">How to read the grid</h2>

The two main streets are the *cardo maximus*, which runs north to south, and the *decumanus maximus*, which runs east to west. Secondary cardines and decumani divide the rest of the city into insulae. A house's position is recorded as its cardine and decumanus coordinates, followed by a house number within that insula, so a house can be placed unambiguously on the street grid even when the block itself has no surviving street label.

This is a working tool, not a finished publication. Identifiers will continue to be checked against the published excavation reports and archival plans through 2026. If you spot an error or have a correction, please [get in touch](/cite/).

<h2 id="numbering-rationale">Numbering rationale</h2>

The identifier system is designed to be stable, location-based, and independent of excavation-era labels, which are inconsistent across a century of French reports. Each insula gets coordinates. Each house gets a two-digit suffix assigned in a consistent order within its insula. Full documentation of the system, including edge cases and how it reconciles with earlier labels, will live on the Methods page as the site grows. For now, the short version is that the identifier tells you where the house is, not when it was excavated or by whom.

<h2>Downloading the data</h2>

The underlying data for the grid will be published as GeoJSON and CSV under a Creative Commons license once the current audit is complete. Until then, if you need the data for research or teaching, please [email Kim directly](mailto:kimedher@gmail.com) and she will share the current working version with appropriate caveats about its provisional status.
