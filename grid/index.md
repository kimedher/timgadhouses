---
layout: page
title: Interactive Grid of Timgad
subtitle: The urban plan of Timgad, block by block, with house identifiers mapped to the streets.
permalink: /grid/
last_updated: 2026-07-06
---

Timgad was laid out on a strict rectilinear grid, two main streets crossing at right angles with regular rectangular blocks between them. Each block, called an *insula* in Latin, is identified here by a quadrant-based reference that locates it relative to the city's central axes. Individual houses are keyed to the insula they sit inside, so that a house identifier like `TIMG.SE.I20.H2` can be traced directly to its place in the city.

The viewer below is the current working version. It shows the city grid and the identifiers assigned to each block, based on the standardized system described in the [numbering rationale](#numbering-rationale) below. Blocks holding a house in the database appear in green and click through to that house's record; houses with full records in the [catalog](/houses/catalog/) are marked with a check.

<p style="margin: 2rem 0;">
  <a href="/grid/viewer.html" style="display: inline-block; background: var(--teal); color: white; padding: 0.8rem 1.4rem; border-radius: var(--radius); border: none; font-weight: 600; font-size: 0.95rem;">Open the full-screen grid &rarr;</a>
</p>

<iframe src="/grid/viewer.html" class="grid-viewer-frame" title="Interactive grid of Timgad"></iframe>

<h2 id="how-to-read-it">How to read the grid</h2>

The two main streets are the *cardo maximus*, which runs north to south, and the *decumanus maximus*, which runs east to west. Their intersection divides Timgad into four quadrants (NW, NE, SW, SE), and each insula is numbered outward from that intersection within its own quadrant. A house's position is recorded as a quadrant, insula number, and optional house suffix for multi-unit insulae, so a house can be placed unambiguously on the street grid regardless of its excavation label.

This is a working tool, not a finished publication. Identifiers will continue to be checked against the published excavation reports and archival plans through 2026. If you spot an error or have a correction, please email [km2133@student.ubc.ca](mailto:km2133@student.ubc.ca).

<h2 id="numbering-rationale">A note on the numbering system</h2>

This project catalogues Timgad's houses with a quadrant-based system, TIMG.{Quadrant}.I{n}.H{n}, anchored to the Cardo and Decumanus Maximus and radiating outward from their intersection. The method is adapted from Giuseppe Fiorelli's Region.Insula.Entrance system at Pompeii, formalized in the 1860s and codified in his *Descrizione di Pompei* (1875), the long-established disciplinary standard for referencing Roman urban architecture.

Adopting a Pompeian method for Timgad requires a word of explanation, because the "African Pompeii" framing imposed on Timgad in its earliest excavation record is one of the things this project pushes back on. Albert Ballu, in the late nineteenth century, explicitly invoked Fiorelli's Pompeii as a model, but what he actually implemented was a sequential 1-to-31 walking-order numbering that reflected his own itinerary through the site rather than the city's structure. That gesture, alongside the rhetorical branding of Timgad as Rome's African Pompeii, flattened Timgad into a colonial analogue and built that framing into the record from the start. Anissa Yelles's 2024 archival work has since documented this borrowing in detail.

The numerical grid system employed in this project uses Fiorelli's actual method rather than Ballu's derivative of it. Fiorelli's logic is spatial and structural. It anchors the reference system to the city's own defining axes, which at Timgad are the Cardo and Decumanus Maximus, not to any excavator's walking order or to a Pompeian analogue. Applying that logic on Timgad's own terms is a rejection of Ballu's framing, not a continuation of it. The underlying methodology travels well across Roman colonial cities precisely because it is spatially rigorous and hierarchically extensible, and using it makes Timgad's houses immediately legible to any Roman archaeologist without asking the city to pretend to be Pompeii.

A concordance spreadsheet keeps every TIMG identifier in translation with Ballu 1903, Ballu 1911, Germain 1969, Rebuffat 1969 and 1974, and Wilson 2001. Prior scholarship is preserved as a translation layer, not erased, so any existing citation can be resolved into the TIMG system and back again without information loss. The concordance is still in active development and will be published on this site once it has been through further review.

<div class="subsection-refs">
  <p>Ballu, Albert. 1897. <em>Les ruines de Timgad (antique Thamugadi)</em>. Paris: Ernest Leroux.</p>
  <p>Ballu, Albert. 1903. <em>Les ruines de Timgad (antique Thamugadi): Nouvelles découvertes</em>. Paris: Ernest Leroux.</p>
  <p>Fiorelli, Giuseppe. 1875. <em>Descrizione di Pompei</em>. Naples: Tipografia Italiana.</p>
  <p>Germain, Suzanne. 1969. <em>Les mosaïques de Timgad: Étude descriptive et analytique</em>. Paris: Éditions du Centre National de la Recherche Scientifique.</p>
  <p>Rebuffat, René. 1969. "Maisons à péristyle d'Afrique du Nord: Répertoire de plans publiés." <em>Mélanges de l'École française de Rome</em> 81 (2): 659–724.</p>
  <p>Wilson, Andrew I. 2001. "Timgad and Textile Production." In <em>Economies Beyond Agriculture in the Classical World</em>, edited by David J. Mattingly and John Salmon, 271–296. London: Routledge.</p>
  <p>Yelles, Anissa. 2024. "Timgad et les archives de fouilles: Relectures et perspectives." In <em>Rome, archéologie et histoire urbaine: trente ans après l'Urbs (1987)</em>, edited by C. Courrier, M. Tarpin, A. Vanel, and N. Tran, 485–508. Rome: École Française de Rome.</p>
</div>

<h2>Downloading the data</h2>

The underlying data for the grid will be published as GeoJSON and CSV under a Creative Commons license once the current audit is complete. For now, the data is in active flux and not distributed externally.

<div class="callout-warn">
  <p><strong>A note on the wet paint.</strong> This grid is a work in progress, and I've published it early on purpose. It pulls straight from the same database as the house catalog, so the blocks update whenever the data does, and right now the data is still moving. Numbers will shift, and some assignments will turn out to be wrong. I would rather fix things in the open than wait for perfect. Once the data settles, I will update this note to reflect its reliability as a stable version for future reference.</p>
</div>

{% include cite-block.html %}
