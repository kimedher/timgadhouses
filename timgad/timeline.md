---
layout: page
title: A Timeline of Excavation
subtitle: Who excavated what part of Timgad, when, and what they published about it. 1870s through the present.
permalink: /timgad/timeline/
last_updated: 2026-04-20
---

<figure class="image-panel">
  <img src="/assets/images/timgad-1922-aerial.jpg" alt="An aerial black and white photograph of Timgad taken in 1922 showing the rectilinear grid of insulae, the Capitol columns rising above the forum area, and the semicircular theatre visible at the bottom centre. The excavated city contrasts with the open ground surrounding it.">
  <figcaption>Timgad seen from above on 16 April 1922, partway through Albert Ballu's long directorship. ETH Library Zürich, Image Archive (Ans_05341-031-AL-FL), <a href="https://commons.wikimedia.org/wiki/File:Timgad_from_above_1922.tif">public domain, via Wikimedia Commons</a>.</figcaption>
</figure>

<p class="timeline-lede">
Timgad has been excavated for nearly 150 years, across three rather different political landscapes. This timeline lays out the scholarly record in a single view: the directors who ran each campaign, the publications that shaped how the city has been read, and the house-by-house discoveries that built the domestic corpus. Hover or tap any event for detail.
</p>

<p class="timeline-note">
<svg class="timeline-note-icon" viewBox="0 0 16 16" width="14" height="14" aria-hidden="true">
  <path d="M11.3 1.7a1 1 0 0 1 1.4 0l1.6 1.6a1 1 0 0 1 0 1.4L5.5 13.5 2 14l.5-3.5L11.3 1.7z" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="10" y1="3" x2="13" y2="6" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
</svg>
<span>The timeline is continuously updated as new scholarship is read and catalogued. Omissions and corrections are inevitable on a record this long, and readers who spot one are warmly invited to be in touch.</span>
</p>

<div class="timeline-controls">
  <div class="timeline-filter" role="group" aria-label="Filter events by type">
    <button type="button" class="tf-chip tf-chip--all is-active" data-filter="all">
      <span class="tf-swatch tf-swatch--all"></span>All events
    </button>
    <button type="button" class="tf-chip" data-filter="campaign">
      <span class="tf-swatch tf-swatch--campaign"></span>Excavation campaigns
    </button>
    <button type="button" class="tf-chip" data-filter="discovery">
      <span class="tf-swatch tf-swatch--discovery"></span>House discoveries
    </button>
    <button type="button" class="tf-chip" data-filter="publication">
      <span class="tf-swatch tf-swatch--publication"></span>Publications
    </button>
    <button type="button" class="tf-chip" data-filter="context">
      <span class="tf-swatch tf-swatch--context"></span>Context
    </button>
  </div>
</div>

<div class="timeline-viz-wrap" id="timeline-viz-wrap">
  <svg id="timeline-svg" class="timeline-svg" viewBox="0 0 1180 340" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Horizontal chronological timeline of Timgad excavations, 1870 to present">
    <!-- Dynamically populated by JS -->
  </svg>
  <div class="timeline-hover" id="timeline-hover" aria-live="polite"></div>
</div>
<div class="timeline-actions">
  <span class="timeline-scroll-hint">Scroll the timeline horizontally to see the full span.</span>
  <button type="button" class="timeline-expand-btn" id="timeline-expand-btn" aria-label="Open timeline in fullscreen">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <polyline points="15 3 21 3 21 9"></polyline>
      <polyline points="9 21 3 21 3 15"></polyline>
      <line x1="21" y1="3" x2="14" y2="10"></line>
      <line x1="3" y1="21" x2="10" y2="14"></line>
    </svg>
    <span>Expand</span>
  </button>
</div>

<script>
(function() {
  var btn = document.getElementById('timeline-expand-btn');
  var wrap = document.getElementById('timeline-viz-wrap');
  if (!btn || !wrap) return;
  var canFullscreen = !!(wrap.requestFullscreen || wrap.webkitRequestFullscreen);
  if (!canFullscreen) {
    /* iPhone Safari and other engines without element-level fullscreen:
       fall back to opening the current page in a new tab, where pinch-zoom
       and the horizontal scroll are the native reading experience. */
    btn.addEventListener('click', function() {
      window.open(window.location.href, '_blank', 'noopener');
    });
    return;
  }
  btn.addEventListener('click', function() {
    if (document.fullscreenElement || document.webkitFullscreenElement) {
      (document.exitFullscreen || document.webkitExitFullscreen).call(document);
    } else {
      var req = wrap.requestFullscreen || wrap.webkitRequestFullscreen;
      var p = req.call(wrap);
      if (p && p.catch) p.catch(function() {
        window.open(window.location.href, '_blank', 'noopener');
      });
    }
  });
})();
</script>

<div class="timeline-detail" id="timeline-detail">
  <div class="td-empty">
    <p><strong>Select an event above</strong> to read its description, the houses or buildings it uncovered, and the source citation. Or scroll down for the full chronological list.</p>
  </div>
</div>

<h2 class="timeline-h2">Full chronology</h2>

<div class="timeline-list" id="timeline-list">
  <!-- Dynamically populated by JS -->
</div>

<h2 class="timeline-h2">Scholarly reliance chain</h2>

<p>Later work builds on earlier work, but not uniformly. The most reliable early plans come from Ballu's 1897 and 1911 monographs. The Boeswillwald, Cagnat, and Ballu 1905 synthesis pulled this material together for a wider audience. Christofle's 1927 to 1936 reports added new excavations rather than reproducing Ballu's. Courtois's 1951 synthesis is frequently cited but its plans are often schematic or conjectural, and Rebuffat (1969, p. 676) warned specifically against treating them as precise. Germain's 1969 mosaic corpus and Rebuffat's 1969 peristyle catalog standardized the comparative record. Modern digital work by Wilson, Dufton, Rezkallah, and Yelles now reads the colonial-era archive against itself, correcting and contextualizing it rather than taking it on faith.</p>

<h2 class="timeline-h2">Notes on reliability</h2>

<p>Rezkallah (2020) confirms that the southeastern quarter of Timgad has no prior surveys of record. The 12 houses in Rebuffat's catalog have standardized 1:500 plans and are the most reliable comparative base. Five further houses are known from Ballu's 1911 monograph but not in Rebuffat (Maisons 25, 27, 38, 72, 73). The largest documented house, the Maison à l'ouest des Thermes des Filadelfes at roughly 2,469 square meters, was excavated in 1921 and 1922. Andrew Wilson (2001) identified at least 22 fullonicae, twice the number attested at Pompeii, concentrated in the northeastern quarter. Amraoui (2018) has since revised that figure downward to 12 fullonicae under stricter identification criteria, of which only five can be precisely located today (Bande NW, Ilots 11, 21, 30, 32).</p>

<style>
/* ========================================================================
   Timeline of Excavation, scoped styles
   ======================================================================== */

.timeline-lede {
  font-size: 1.05rem;
  color: var(--text);
  margin: 1rem 0 0.5rem;
  line-height: 1.7;
}

.timeline-note {
  font-size: 0.82rem;
  font-style: italic;
  color: var(--text-muted);
  line-height: 1.55;
  margin: 0 0 2rem;
  padding: 0.55rem 0 0.55rem 0.9rem;
  border-left: 2px solid var(--terracotta);
  background: rgba(199, 123, 90, 0.04);
  border-radius: 0 3px 3px 0;
  display: flex;
  align-items: flex-start;
  gap: 0.55rem;
  max-width: 720px;
}

.timeline-note-icon {
  color: var(--terracotta-deep, var(--terracotta));
  flex-shrink: 0;
  margin-top: 0.15rem;
}

/* Filters */
.timeline-controls {
  display: flex;
  justify-content: center;
  margin: 1rem auto 1.4rem;
  max-width: var(--max-wide);
}

.timeline-filter {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  justify-content: center;
  background: var(--bg-soft);
  border: 1px solid var(--hairline);
  border-radius: 999px;
  padding: 0.4rem;
}

.tf-chip {
  font-family: var(--sans);
  font-size: 0.78rem;
  font-weight: 500;
  letter-spacing: 0.02em;
  color: var(--text-muted);
  background: transparent;
  border: 1px solid transparent;
  padding: 0.42rem 0.9rem;
  border-radius: 999px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s;
}

.tf-chip:hover {
  color: var(--text);
  background: #fff;
}

.tf-chip.is-active {
  background: var(--text);
  color: #fff;
  border-color: var(--text);
}

.tf-chip.is-active .tf-swatch {
  box-shadow: 0 0 0 2px rgba(255, 255, 255, 0.25);
}

.tf-swatch {
  display: inline-block;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--text-muted);
}

.tf-swatch--all         { background: linear-gradient(135deg, var(--teal), var(--terracotta)); }
.tf-swatch--campaign    { background: var(--teal); }
.tf-swatch--discovery   { background: var(--terracotta); }
.tf-swatch--publication { background: var(--baby-blue-deep); }
.tf-swatch--context     { background: var(--text-muted); }

/* Main visualization.
   The SVG is rendered at a wider-than-native 1600px so the labels and bars
   come in at a comfortable reading size. The wrap stays within the page
   reading column and scrolls horizontally to expose the rest of the SVG. */
.timeline-viz-wrap {
  position: relative;
  max-width: var(--max-content);
  margin: 0 auto 0.6rem;
  background: #fff;
  border: 1px solid var(--hairline);
  border-radius: 8px;
  padding: 1rem 0.6rem 0.6rem;
  box-shadow: 0 1px 2px rgba(31, 41, 51, 0.03);
  overflow-x: auto;
  overflow-y: hidden;
  -webkit-overflow-scrolling: touch;
}

.timeline-svg {
  width: 1600px;
  min-width: 1600px;
  height: auto;
  display: block;
  font-family: var(--sans);
  user-select: none;
}

.timeline-actions {
  max-width: var(--max-content);
  margin: 0 auto 1.4rem;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  gap: 1rem;
  font-family: var(--sans);
  font-size: 0.78rem;
}

.timeline-expand-btn {
  background: transparent;
  border: 1px solid var(--hairline);
  color: var(--teal-dark);
  padding: 0.4rem 0.85rem;
  border-radius: var(--radius);
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  font-family: var(--sans);
  font-size: 0.78rem;
  font-weight: 500;
  letter-spacing: 0.03em;
  text-decoration: none;
  transition: background 0.15s, color 0.15s, border-color 0.15s;
}

.timeline-expand-btn:hover {
  background: rgba(27, 107, 111, 0.08);
  border-color: var(--teal);
  color: var(--teal-dark);
}

.timeline-expand-btn svg {
  flex: 0 0 auto;
}

.timeline-scroll-hint {
  font-family: var(--sans);
  font-size: 0.74rem;
  color: var(--text-muted);
  letter-spacing: 0.02em;
  margin: 0;
}

/* Fullscreen styling: when the wrap enters browser fullscreen, push the SVG
   bigger so it fills the screen width, and let the wrap take the full height. */
.timeline-viz-wrap:fullscreen,
.timeline-viz-wrap:-webkit-full-screen {
  background: var(--bg);
  max-width: none;
  width: 100vw;
  height: 100vh;
  border-radius: 0;
  border: none;
  margin: 0;
  padding: 2rem 1.5rem;
  box-sizing: border-box;
  display: flex;
  align-items: center;
  overflow-x: auto;
  overflow-y: hidden;
}
.timeline-viz-wrap:fullscreen .timeline-svg,
.timeline-viz-wrap:-webkit-full-screen .timeline-svg {
  width: 2400px;
  min-width: 2400px;
  height: auto;
  margin: auto;
}

.timeline-svg text { fill: var(--text); }
.timeline-svg .tl-year-label {
  font-size: 11px;
  font-weight: 500;
  fill: var(--text-muted);
}
.timeline-svg .tl-era-label {
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  fill: var(--text);
  fill-opacity: 0.7;
  paint-order: stroke;
  stroke: var(--bg);
  stroke-width: 3px;
  stroke-linejoin: round;
}
.timeline-svg .tl-director-label {
  font-size: 11px;
  font-weight: 600;
  fill: #fff;
}
.timeline-svg .tl-director-sub {
  font-size: 9px;
  font-weight: 500;
  fill: rgba(255, 255, 255, 0.8);
}
.timeline-svg .tl-director-label-outside {
  font-size: 11px;
  font-weight: 600;
  fill: var(--text);
}
.timeline-svg .tl-director-sub-outside {
  font-size: 9px;
  font-weight: 500;
  fill: var(--text-muted);
}
.timeline-svg .tl-era-band { opacity: 0.35; }
.timeline-svg .tl-decade-line {
  stroke: var(--hairline);
  stroke-width: 1;
  opacity: 0.6;
}
.timeline-svg .tl-axis-line {
  stroke: var(--text);
  stroke-width: 1;
  opacity: 0.25;
}
.timeline-svg .tl-director-bar {
  transition: opacity 0.2s;
}
.timeline-svg .tl-event-dot {
  cursor: pointer;
  transition: transform 0.18s, filter 0.18s, opacity 0.25s;
  transform-origin: center;
  transform-box: fill-box;
}
.timeline-svg .tl-event-dot:hover,
.timeline-svg .tl-event-dot.is-hover,
.timeline-svg .tl-event-dot.is-selected {
  transform: scale(1.55);
  filter: drop-shadow(0 2px 4px rgba(31, 41, 51, 0.28));
}
.timeline-svg .tl-event-dot.is-dim {
  opacity: 0.18;
}
.timeline-svg .tl-event-line {
  stroke-width: 1;
  opacity: 0.35;
  transition: opacity 0.2s;
}
.timeline-svg .tl-event-line.is-dim { opacity: 0.08; }

/* Floating hover label */
.timeline-hover {
  position: absolute;
  background: var(--text);
  color: #fff;
  padding: 0.5rem 0.75rem;
  font-size: 0.75rem;
  border-radius: 4px;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.15s;
  z-index: 5;
  max-width: 240px;
  line-height: 1.4;
  box-shadow: 0 3px 12px rgba(31, 41, 51, 0.2);
}
.timeline-hover.is-visible { opacity: 1; }
.timeline-hover .th-year {
  font-weight: 700;
  font-size: 0.7rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--baby-blue);
  margin-bottom: 0.2rem;
}

/* Detail panel */
.timeline-detail {
  max-width: 780px;
  margin: 0 auto 3rem;
  background: var(--bg-soft);
  border-left: 4px solid var(--teal);
  padding: 1.2rem 1.4rem;
  border-radius: 4px;
  min-height: 100px;
}
.timeline-detail .td-empty { color: var(--text-muted); font-size: 0.9rem; }
.timeline-detail .td-empty p { margin: 0; }

.timeline-detail .td-card .td-year {
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-bottom: 0.35rem;
}
.timeline-detail .td-card .td-type-badge {
  display: inline-block;
  padding: 0.15rem 0.55rem;
  border-radius: 999px;
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  margin-left: 0.5rem;
  vertical-align: middle;
  color: #fff;
}
.timeline-detail .td-card .td-title {
  font-size: 1.15rem;
  font-weight: 600;
  margin: 0 0 0.3rem;
  color: var(--text);
  line-height: 1.3;
}
.timeline-detail .td-card .td-person {
  font-size: 0.85rem;
  color: var(--terracotta-deep);
  font-weight: 500;
  margin-bottom: 0.6rem;
}
.timeline-detail .td-card .td-desc {
  font-size: 0.92rem;
  line-height: 1.55;
  margin: 0.5rem 0;
  color: var(--text);
}
.timeline-detail .td-card .td-houses {
  font-size: 0.82rem;
  color: var(--text-muted);
  margin: 0.5rem 0;
  font-style: italic;
}
.timeline-detail .td-card .td-source {
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-top: 0.6rem;
  padding-top: 0.5rem;
  border-top: 1px solid var(--hairline);
}

.td-type-campaign    { background: var(--teal); }
.td-type-discovery   { background: var(--terracotta); }
.td-type-publication { background: var(--baby-blue-deep); }
.td-type-context     { background: var(--text-muted); }

/* Full list (decade-grouped cards) */
.timeline-h2 {
  max-width: var(--max-content);
  margin: 3rem auto 1rem;
  padding: 0 1rem;
}

.timeline-list {
  max-width: var(--max-content);
  margin: 0 auto 2rem;
  padding: 0 1rem;
}

.tl-decade {
  margin-bottom: 2.2rem;
  position: relative;
}

.tl-decade-heading {
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--teal-dark);
  margin: 0 0 1rem;
  padding-bottom: 0.4rem;
  border-bottom: 2px solid var(--hairline);
  letter-spacing: -0.02em;
}

.tl-decade-events {
  display: grid;
  gap: 0.9rem;
}

.tl-event {
  display: grid;
  grid-template-columns: 80px 1fr;
  gap: 1rem;
  padding: 0.9rem 1rem;
  background: #fff;
  border: 1px solid var(--hairline);
  border-left: 4px solid var(--text-muted);
  border-radius: 4px;
  transition: all 0.2s;
  scroll-margin-top: 90px;
}
.tl-event:hover, .tl-event.is-highlight {
  box-shadow: 0 2px 10px rgba(31, 41, 51, 0.08);
  transform: translateY(-1px);
}
.tl-event.is-highlight {
  background: var(--baby-blue-soft);
}
.tl-event.is-dim {
  opacity: 0.35;
  filter: grayscale(0.5);
}
.tl-event[data-type="campaign"]    { border-left-color: var(--teal); }
.tl-event[data-type="discovery"]   { border-left-color: var(--terracotta); }
.tl-event[data-type="publication"] { border-left-color: var(--baby-blue-deep); }
.tl-event[data-type="context"]     { border-left-color: var(--text-muted); }

.tl-event .tl-e-year {
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--text-muted);
  font-variant-numeric: tabular-nums;
  padding-top: 0.12rem;
}

.tl-event .tl-e-body {
  min-width: 0;
}
.tl-event .tl-e-title {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text);
  margin: 0 0 0.15rem;
  line-height: 1.35;
}
.tl-event .tl-e-person {
  font-size: 0.82rem;
  color: var(--terracotta-deep);
  margin: 0 0 0.25rem;
  font-weight: 500;
}
.tl-event .tl-e-desc {
  font-size: 0.88rem;
  color: var(--text);
  margin: 0.2rem 0 0;
  line-height: 1.55;
}
.tl-event .tl-e-meta {
  font-size: 0.75rem;
  color: var(--text-muted);
  margin-top: 0.4rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1rem;
}
.tl-event .tl-e-meta em { font-style: italic; }

/* Responsive */
@media (max-width: 720px) {
  .timeline-actions {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.6rem;
  }
  .timeline-filter { font-size: 0.7rem; }
  .tf-chip { padding: 0.35rem 0.7rem; font-size: 0.72rem; }
  .tl-event {
    grid-template-columns: 60px 1fr;
    gap: 0.7rem;
    padding: 0.7rem 0.8rem;
  }
  .tl-event .tl-e-year { font-size: 0.85rem; }
  .tl-event .tl-e-title { font-size: 0.94rem; }
  .tl-event .tl-e-desc { font-size: 0.82rem; }
  .timeline-detail { padding: 1rem; }
}
</style>

<script>
(function () {
  'use strict';

  // ====================================================================
  // DATA
  // ====================================================================

  const ERAS = [
    {
      start: 1875, end: 1962,
      label: 'French Colonial (occupation begins 1830)',
      color: '#C77B5A',
      y: 100, height: 24
    },
    {
      start: 1962, end: 2030,
      label: 'Post-Independence',
      color: '#8FBDCF',
      y: 100, height: 24
    }
  ];

  const DIRECTORS = [
    {
      start: 1890, end: 1926,
      name: 'Albert Ballu',
      sub: 'with René Cagnat',
      color: '#104A4D',
      row: 0
    },
    {
      start: 1927, end: 1936,
      name: 'Marcel Christofle',
      sub: '',
      color: '#1B6B6F',
      row: 1
    },
    {
      start: 1938, end: 1956,
      name: 'Jean Lassus',
      sub: 'with the Godets',
      color: '#4F8AA0',
      row: 2
    }
  ];

  const EVENTS = [
    {
      year: 1875, title: 'Masqueray opens the first excavations',
      person: 'Émile Masqueray',
      type: 'campaign',
      desc: 'Working with a battalion of soldiers, Masqueray carries out the first excavations at the site. Among the finds is a portion of the inscription known as the Album municipal of Timgad. He also produces an early sector by sector description of the visible city, working from what was still largely a buried site.',
      houses: 'Album municipal inscription; sector by sector description',
      source: 'Masqueray 1876; Yelles 2024'
    },
    {
      year: 1880, title: 'Initial reconnaissance of the site',
      person: 'Gen. de Beylié; Cdt. Playfair',
      type: 'campaign',
      desc: 'First scholarly identification of the ruins on the Aurès plain as Roman Thamugadi. Playfair notes visible standing monuments.',
      houses: 'General site survey, no specific buildings',
      source: 'Pre-excavation reconnaissance'
    },
    {
      year: 1883, title: 'Boissière, L\'Algérie romaine',
      person: 'Gaston Boissière',
      type: 'publication',
      desc: 'Early monograph framing Timgad within the broader archaeological project of Roman Algeria. Establishes the site as one of major scholarly interest.',
      houses: 'General references',
      source: 'Boissière 1883 (SRC_001)'
    },
    {
      year: 1885, title: 'Duthoit directs the first major campaign',
      person: 'Edmond Duthoit',
      type: 'campaign',
      desc: 'The architect Edmond Duthoit runs the first large scale fieldwork at Timgad between 1885 and 1887, concentrated on the forum, the theater, and the Arch of Trajan. Duthoit leaves no written excavation report, but a substantial archive of photographs and plans survives at the Médiathèque du patrimoine et de la photographie and at the municipal archives in Amiens.',
      houses: 'Forum, theater, Arch of Trajan',
      source: 'Yelles 2024, p. 86'
    },
    {
      year: 1891, title: 'Cagnat reports to the Académie',
      person: 'René Cagnat',
      type: 'publication',
      desc: 'First formal report on the Timgad excavations to the Académie des Inscriptions. Documents the founding by Trajan and the Third Augustan Legion, the cardo/decumanus grid, and the emerging forum complex.',
      houses: 'General city description',
      source: 'Cagnat 1891, CRAI (SRC_003)'
    },
    {
      year: 1897, title: 'Les ruines de Timgad, the founding monograph',
      person: 'Albert Ballu',
      type: 'publication',
      desc: 'The first major monograph on the excavations. 244 pages with 8 plans, 32 phototype plates, and 41 drawings. Contains the earliest house plans, including the Maison des Jardinières. Published with state subsidy by the Imprimerie Nationale.',
      houses: 'Maison des Jardinières (M70), and many unnumbered domus types',
      source: 'Ballu 1897 (SRC_006)'
    },
    {
      year: 1897, title: 'Guide de Timgad published',
      person: 'Albert Ballu',
      type: 'publication',
      desc: 'Companion tourist and scholarly guide in the "Guides en Algérie et en Tunisie" series. Three domus types described in detail (pp. 90 to 92), including a house with stables and stone mangers.',
      houses: 'Three domus typologies described',
      source: 'Ballu 1897, Guide (SRC_007)'
    },
    {
      year: 1901, title: 'Houses of Sertius and Hermaphrodite excavated',
      person: 'Albert Ballu',
      type: 'discovery',
      desc: 'Two of the most important elite peristyle houses at Timgad are cleared. Maison de Sertius has a triclinium of 16 by 25 ft with triple bays. Maison de l\'Hermaphrodite has a complete peristyle and tripartite triclinium.',
      houses: 'Maison de Sertius, Maison de l\'Hermaphrodite',
      source: 'Ballu 1903 (SRC_010); Gsell 1902 (SRC_008)'
    },
    {
      year: 1901, title: '1901 campaign, four insulae documented',
      person: 'Stéphane Gsell (under Ballu)',
      type: 'campaign',
      desc: 'Annual report for the 1901 season. Decumanus maximus cleared to the eastern gate. Four insulae with domestic features recorded room by room. Small thermae documented near the basilica.',
      houses: '4 insulae with domestic features',
      source: 'Gsell 1902, BCTH (SRC_008)'
    },
    {
      year: 1905, title: 'Timgad, une cité africaine, the great synthesis',
      person: 'Boeswillwald, Cagnat, Ballu',
      type: 'publication',
      desc: 'The most influential early monograph on Timgad, co-authored by the three principal figures of the campaigns. Documents the Maison de la Piscina (67/75) and Maisons 83 and 90. Contains figures (40, 152, 156, 166) reproduced in almost every later scholarly work.',
      houses: 'Maisons 67/75 (Piscina), 83, 90',
      source: 'Boeswillwald, Cagnat & Ballu 1905 (SRC_014)'
    },
    {
      year: 1911, title: 'Sept années de découvertes, 1903 to 1910',
      person: 'Albert Ballu',
      type: 'publication',
      desc: 'The definitive early excavation report. Houses pp. 49 to 89. City-wide plan. Houses described as "manifestly reconstructed on earlier dwellings" with extensive commercial-residential mixing (shops, fulling vats). Rebuffat (1969) treats it as the canonical record for peristyles at Timgad.',
      houses: 'All numbered Maisons 25 to 90, plus many unnumbered',
      source: 'Ballu 1911 (SRC_017)'
    },
    {
      year: 1911, title: 'Gsell, Atlas archéologique de l\'Algérie',
      person: 'Stéphane Gsell',
      type: 'publication',
      desc: 'Regional archaeological atlas placing Timgad within the wider archaeological map of Algeria.',
      houses: 'Regional site plans',
      source: 'Gsell 1911'
    },
    {
      year: 1911, title: 'Pachtère mosaic inventory',
      person: 'F.-G. de Pachtère',
      type: 'publication',
      desc: 'Inventaire des mosaïques de la Gaule et de l\'Afrique, Tome III. Timgad material pp. 67 to 179. The earliest systematic visual corpus of Timgad mosaics with locational data, predating Germain by 58 years.',
      houses: 'All buildings with mosaic floors',
      source: 'Pachtère 1911 (SRC_020)'
    },
    {
      year: 1912, title: 'Sixteen fulling establishments briefly described',
      person: 'Albert Ballu',
      type: 'discovery',
      desc: 'BCTH 1911a and 1912 annual reports first record the northeast industrial quarter. Sixteen fulling installations noted, later consolidated in 1914 and redrawn from Christofle\'s plans by Wilson in 2001.',
      houses: '16 fullonicae in northeast quarter',
      source: 'BCTH 1912 to 1914; Wilson 2001 p. 278'
    },
    {
      year: 1917, title: 'Houses north and south of the boulevards',
      person: 'Albert Ballu',
      type: 'campaign',
      desc: 'Annual reports covering 1916 to 1919. Three zones of houses north and south of the boulevards cleared. Christian chapel documented, with the Maison des Jardinières mosaic (Germain 1) reused within it.',
      houses: 'Three zones of houses, Christian chapel',
      source: 'Ballu 1916 to 1919, BIAA (SRC_021)'
    },
    {
      year: 1922, title: 'Maison des Filadelfes, the largest house at Timgad',
      person: 'Albert Ballu',
      type: 'discovery',
      desc: 'The Maison à l\'ouest des Thermes des Filadelfes is uncovered at roughly 2,469 square meters, the largest documented private residence at Timgad. Two divisions with atrium and peristyle courts, 15+ decorated rooms, six mosaics, a private thermal suite, three shops, and a peristyle well 1.90 m in diameter.',
      houses: 'Maison des Filadelfes (~2,469 m²)',
      source: 'Ballu 1921 to 1922, BIAA (SRC_022)'
    },
    {
      year: 1924, title: 'Theater Quarter House and Maison 102',
      person: 'Albert Ballu with M. Godet',
      type: 'discovery',
      desc: 'Four-section house in the theater quarter with atrium, three columns, mosaic floor, shop component, and a pool 1.20 m square. Maison 102 plan published (courtyard with portico on two sides).',
      houses: 'Theater Quarter House, Maison 102',
      source: 'Ballu 1924, BIAA (SRC_023)'
    },
    {
      year: 1925, title: 'House at the East Rampart',
      person: 'Albert Ballu with M. Godet',
      type: 'discovery',
      desc: 'A six-column portico house with reception hall 6.80 by 11.60 m, atrium 7.35 by 6.10 m, a lead water piping system, and connection to small baths.',
      houses: 'House at the East Rampart',
      source: 'Ballu 1925 to 1926, BIAA (SRC_024)'
    },
    {
      year: 1927, title: 'Christofle succeeds Ballu',
      person: 'Marcel Christofle',
      type: 'campaign',
      desc: 'After Ballu\'s 45-year tenure, Marcel Christofle takes over direction of excavations. The new campaigns run roughly 1927 to 1936 and focus on previously unreported structures, producing new plans rather than reproducing Ballu\'s.',
      houses: 'Transfer of direction',
      source: 'Christofle 1930 (SRC_025, SRC_026)'
    },
    {
      year: 1928, title: 'Entrepôt and Maison du quartier est',
      person: 'Marcel Christofle',
      type: 'discovery',
      desc: 'Large house north of the Capitole (peristyle, 8 sandstone columns) documented. The Entrepôt recorded (Rebuffat No. 9) with double passages, apse chamber, and peristyle mosaics 3.85 by 3.60 m. Maison du quartier est (Rebuffat No. 10) documented.',
      houses: 'House N of Capitole, Entrepôt, Maison du quartier est',
      source: 'Christofle 1930 (SRC_025)'
    },
    {
      year: 1931, title: 'Fullonicae plans published',
      person: 'Marcel Christofle',
      type: 'publication',
      desc: 'First publication of detailed plans for the fulling installations in the northeastern industrial quarter (pp. 69 to 77). Seven plans, later redrawn by Andrew Wilson (2001). These remain the primary source for Timgad\'s textile economy.',
      houses: '7 fullonicae plans + cellar at Trajan\'s Arc',
      source: 'Christofle 1935 (SRC_027)'
    },
    {
      year: 1935, title: 'House south of the theater, 20+ rooms',
      person: 'Marcel Christofle',
      type: 'discovery',
      desc: 'Single intact residence south of the theater with 20+ rooms, a 12-column peristyle, and a central well 9.80 m deep (iron dovetail cramps cast in lead). Initially misidentified as multiple houses. Three further houses north of the Decumanus Maximus documented. Large late house built on the necropolis (30.45 by 28.65 m) with reused Corinthian columns.',
      houses: 'House S of theater, 3 houses N of Decumanus, late house on necropolis',
      source: 'Christofle 1938 (SRC_028)'
    },
    {
      year: 1938, title: 'Byzantine fortress excavations begin',
      person: 'Jean Lassus, Charles Godet, René Godet',
      type: 'campaign',
      desc: 'Excavations of the Byzantine fortress of Aqua Septimiana Felix, roughly 300 m south of the Roman city. Originally initiated by Ballu in 1910, renewed in 1939 at the request of the Byzantine Studies Congress. Roman city materials (including from the Maison des Jardinières) were systematically reused in Byzantine fortress construction.',
      houses: 'Byzantine fortress, suburban 2nd-c. houses',
      source: 'Lassus 1981 (SRC_034); Leschi 1947 (SRC_029)'
    },
    {
      year: 1947, title: 'Leschi, Aqua Septimiana Felix',
      person: 'Louis Leschi',
      type: 'publication',
      desc: 'Study of the Caracalla-era inscription (October to December 213 AD) documenting a monumental complex with viridiarium, painted porticoes, bronze balustrade, and paved plaza. Evidence for the Serapis cult and Dea patria at Timgad.',
      houses: 'Monumental complex at the Byzantine fortress site',
      source: 'Leschi 1947 (SRC_029)'
    },
    {
      year: 1951, title: 'Courtois, Timgad, antique Thamugadi',
      person: 'Christian Courtois',
      type: 'publication',
      desc: 'Popular interpretive synthesis that remains widely cited. Rebuffat (1969, p. 676) flags many of its plans as "fantaisistes" (fanciful) and therefore architecturally imprecise, meaning the volume is better treated as a source for reception history rather than for the plans themselves.',
      houses: 'Schematic plans, read for interpretive framing more than architectural precision',
      source: 'Courtois 1951 (SRC_030)'
    },
    {
      year: 1957, title: 'Tourrenc, the last programmed excavations',
      person: 'Serge Tourrenc',
      type: 'campaign',
      desc: 'Serge Tourrenc directs the last programmed excavations at Timgad between 1957 and 1962. As head of the Constantine South circumscription, which also covered Lambèse and Khenchela, his work at Timgad was confined to a few targeted sectors. In 1959, fieldwork at the Temple du Génie recovered the dedicatory inscription, and parallel work in the Byzantine fortress sector revealed Legio III Augusta legate inscriptions reused in later construction.',
      houses: 'Temple du Génie inscription; Byzantine fort reused inscriptions',
      source: 'Tourrenc 1968; Lassus 1981'
    },
    {
      year: 1962, title: 'Algerian Independence',
      person: '',
      type: 'context',
      desc: "After a war of liberation that took hundreds of thousands of Algerian lives and displaced many more, Algeria won its sovereignty back from France. Timgad, along with the rest of the country's archaeological record, returned to the custodianship of the people whose ancestors had built, inhabited, and outlasted it. The French-era archive endures as the main documentary base for excavation history, a colonial inheritance that Algerian and Maghrebi scholars continue to reread on their own terms.",
      houses: '',
      source: 'Historical context'
    },
    {
      year: 1967, title: 'Post-independence return to the Byzantine fortress',
      person: 'Jean Lassus, Marcel Le Glay, Jean-Claude Golvin',
      type: 'campaign',
      desc: 'Five years after independence, a short return mission documents the Byzantine fortress sector. Lassus and Le Glay work alongside Jean-Claude Golvin. These are among the last fieldwork visits by the colonial-era generation of scholars.',
      houses: 'Byzantine fortress documentation',
      source: 'Lassus 1981'
    },
    {
      year: 1969, title: 'Germain mosaic corpus, 189 mosaics cataloged',
      person: 'Suzanne Germain',
      type: 'publication',
      desc: "Comprehensive mosaic corpus cataloging 189 mosaics across all Timgad buildings. Schematic plans link mosaics to room locations (figs. 3, 6, 7, 10, 12), with museum inventory numbers for 120+ pieces. The standard reference for Timgad's decorative program, though its approach is primarily art historical, extracting pavements from their architectural contexts rather than reading them as part of integrated domestic environments. Essential for mosaic identification, limited for spatial or architectural reconstruction.",
      houses: 'All houses with mosaics',
      source: 'Germain 1969 (SRC_032)'
    },
    {
      year: 1969, title: 'Rebuffat\'s peristyle repertoire',
      person: 'René Rebuffat',
      type: 'publication',
      desc: 'The foundational catalog of North African peristyle houses. Twelve Timgad houses documented with standardized 1:500 plans. Methodological corrections to earlier colonial-era work. Rebuffat\'s numbering system is still in use today, including in this project\'s database.',
      houses: '12 houses: Sertius, Hermaphrodite, Corfidius, Piscina, Jardinières, 83, 90, 102, Entrepôt, Quartier est, Filadelfes, Optat',
      source: 'Rebuffat 1969 (SRC_033)'
    },
    {
      year: 1974, title: 'Rebuffat, Part II',
      person: 'René Rebuffat',
      type: 'publication',
      desc: 'Expanded and corrected catalog with index for cross-site comparison across North African peristyle houses.',
      houses: 'Updated peristyle catalog with index',
      source: 'Rebuffat 1974'
    },
    {
      year: 1981, title: 'Lepelley, Les Cités de l\'Afrique romaine',
      person: 'Claude Lepelley',
      type: 'publication',
      desc: 'Tome II covers the Late Roman civic life of Numidian cities, including Timgad. The standard reference for Late Antique Timgad. Precisely dates the Corfidius Crementius restoration to the 4th century AD via epigraphy.',
      houses: 'Late Antique civic life and epigraphy',
      source: 'Lepelley 1981'
    },
    {
      year: 1981, title: 'Lassus, La forteresse byzantine de Thamugadi',
      person: 'Jean Lassus',
      type: 'publication',
      desc: 'Long-delayed monograph publishing the 1938 to 1956 Byzantine fortress excavations. The definitive account of Aqua Septimiana Felix and of the systematic reuse of Roman city materials.',
      houses: 'Byzantine fortress, suburban houses',
      source: 'Lassus 1981 (SRC_034)'
    },
    {
      year: 2001, title: 'Wilson, Timgad and Textile Production',
      person: 'Andrew Wilson',
      type: 'publication',
      desc: 'Identifies at least 22 fullonicae, twice the number attested at Pompeii, concentrated in the northeast quarter. Seven plans redrawn from Christofle 1935. Directly challenges the "consumer city" model of Roman urbanism. Forum vestiarum inscription recovered.',
      houses: '22+ fullonicae, NE industrial zone, Sertius market',
      source: 'Wilson 2001 (SRC_040)'
    },
    {
      year: 2011, title: 'Amraoui, industrial quarter of Timgad',
      person: 'Touatia Amraoui',
      type: 'publication',
      desc: "A reassessment of the state of the question on Timgad's industrial quarter, pulling scattered references from earlier reports into a coherent study. Part of a renewed engagement with Maghrebi production archaeology by scholars with roots in the region, and the groundwork for Amraoui's fuller treatments in 2018 and 2020.",
      houses: 'Industrial quarter',
      source: 'Amraoui 2011'
    },
    {
      year: 2019, title: 'Dufton, gentrification and property consolidation',
      person: 'Andrew Dufton',
      type: 'publication',
      desc: 'Reads Timgad\'s domestic architecture for gentrification dynamics, specifically elite property consolidation during the Severan boom. Critical engagement with colonial excavation practices, using the archive against itself rather than on its own terms.',
      houses: 'Property consolidation patterns citywide',
      source: 'Dufton 2019 (SRC_046, SRC_047)'
    },
    {
      year: 2020, title: 'Rezkallah, first GIS of Timgad excavations',
      person: 'Younès Rezkallah',
      type: 'publication',
      desc: 'Vectorization of the 1960 master plan and 18 insula survey plans. Identifies the southeast quarter as having no prior surveys of record. Critiques arbitrary restorations. First systematic GIS treatment of the Timgad excavation record.',
      houses: '18 insulae surveyed, SE quarter flagged as undocumented',
      source: 'Rezkallah 2020 (SRC_051)'
    },
    {
      year: 2024, title: 'Yelles, Chronocarto de Timgad',
      person: 'Anissa Yelles',
      type: 'publication',
      desc: 'This paper is part of Yelles\'s <a href="https://timgadpro.hypotheses.org/" target="_blank" rel="noopener">Timgad Archives Project (TIMaP)</a> at AOROC, ENS Paris, developed in collaboration with the École française de Rome and the North African Heritage Archives Network (NAHAN). Using the Chronocarto GIS platform, Yelles reconstructs Ballu\'s excavation documentation from the 1880s onward. The study stands as a foundational digital-humanities contribution to rereading Timgad\'s excavation history with the tools of contemporary spatial analysis.',
      houses: 'Archival reassessment of all Ballu excavations',
      source: 'Yelles 2024 (SRC_053)'
    },
    {
      year: 2024, title: 'Laghmouche et al., Late Roman urban changes',
      person: 'Laghmouche et al.',
      type: 'publication',
      desc: 'Five houses with Late Roman restoration evidence documented. Only the Corfidius Crementius house is precisely dated (4th c. AD, via Lepelley 1981 epigraphy). The paper acknowledges imprecise dating across the corpus as a major limitation, and calls for future work to establish secure dates for when individual houses were built, modified, and abandoned.',
      houses: 'Sertius, House N of Capitol, House near Filadelfes, Insula 61, Corfidius Crementius',
      source: 'Laghmouche 2024 (SRC_052)'
    }
  ];

  // ====================================================================
  // LAYOUT CONSTANTS
  // ====================================================================

  const VB_W = 1180, VB_H = 340;
  const MARGIN_L = 50, MARGIN_R = 50;
  const MIN_YEAR = 1870, MAX_YEAR = 2030;

  const ERA_Y = 70;     // era bands
  const ERA_H = 26;
  const DIRECTORS_Y_START = 115;
  const DIRECTOR_H = 30;
  const DIRECTOR_GAP = 6;
  const EVENT_DOT_RADIUS = 5.5;

  // X mapping
  const PLOT_W = VB_W - MARGIN_L - MARGIN_R;
  function x(year) {
    return MARGIN_L + ((year - MIN_YEAR) / (MAX_YEAR - MIN_YEAR)) * PLOT_W;
  }

  // Type -> color
  const TYPE_COLORS = {
    campaign: '#1B6B6F',
    discovery: '#C77B5A',
    publication: '#4F8AA0',
    context: '#6B7380'
  };

  const TYPE_LABELS = {
    campaign: 'Excavation campaign',
    discovery: 'House discovery',
    publication: 'Publication',
    context: 'Context'
  };

  // ====================================================================
  // RENDER SVG
  // ====================================================================

  const svg = document.getElementById('timeline-svg');
  const NS = 'http://www.w3.org/2000/svg';

  function el(tag, attrs, text) {
    const e = document.createElementNS(NS, tag);
    if (attrs) for (const k in attrs) e.setAttribute(k, attrs[k]);
    if (text !== undefined) e.textContent = text;
    return e;
  }

  // Era bands with left-anchored labels (prevents clipping of narrower eras)
  ERAS.forEach(era => {
    const eraX = x(era.start);
    const eraW = x(era.end) - eraX;
    svg.appendChild(el('rect', {
      x: eraX, y: ERA_Y, width: eraW, height: ERA_H,
      fill: era.color, class: 'tl-era-band', rx: 3
    }));
    svg.appendChild(el('text', {
      x: eraX + 10, y: ERA_Y + ERA_H / 2 + 4,
      'text-anchor': 'start', class: 'tl-era-label'
    }, era.label));
  });

  // Decade grid lines and labels (1880, 1890, ..., 2020)
  for (let yr = 1870; yr <= 2030; yr += 10) {
    const xp = x(yr);
    svg.appendChild(el('line', {
      x1: xp, y1: ERA_Y - 8, x2: xp, y2: VB_H - 40,
      class: 'tl-decade-line'
    }));
    svg.appendChild(el('text', {
      x: xp, y: ERA_Y - 14,
      'text-anchor': 'middle', class: 'tl-year-label'
    }, yr));
  }

  // Director tenure bars. Label goes inside if bar is wide enough, otherwise outside to the right in dark text.
  const DIRECTOR_MIN_INSIDE_W = 140;
  DIRECTORS.forEach(d => {
    const yPos = DIRECTORS_Y_START + d.row * (DIRECTOR_H + DIRECTOR_GAP);
    const dX = x(d.start);
    const dW = x(d.end) - dX;
    svg.appendChild(el('rect', {
      x: dX, y: yPos, width: dW, height: DIRECTOR_H,
      fill: d.color, class: 'tl-director-bar', rx: 4
    }));
    const subText = (d.sub ? d.sub + ' · ' : '') + d.start + ' to ' + d.end;
    if (dW >= DIRECTOR_MIN_INSIDE_W) {
      // Inside the bar, white text
      svg.appendChild(el('text', {
        x: dX + 10, y: yPos + 13,
        class: 'tl-director-label'
      }, d.name));
      svg.appendChild(el('text', {
        x: dX + 10, y: yPos + 24,
        class: 'tl-director-sub'
      }, subText));
    } else {
      // Outside the bar, dark text
      svg.appendChild(el('text', {
        x: dX + dW + 8, y: yPos + 13,
        class: 'tl-director-label-outside'
      }, d.name));
      svg.appendChild(el('text', {
        x: dX + dW + 8, y: yPos + 24,
        class: 'tl-director-sub-outside'
      }, subText));
    }
  });

  // Baseline axis line
  const AXIS_Y = VB_H - 60;
  svg.appendChild(el('line', {
    x1: MARGIN_L, y1: AXIS_Y, x2: VB_W - MARGIN_R, y2: AXIS_Y,
    class: 'tl-axis-line'
  }));

  // Events: lay out ABOVE director bars (for publications, context) and BELOW (campaigns, discoveries)
  // Stack vertically if events collide in x.
  const EVENTS_TOP_BASE = DIRECTORS_Y_START - 18;   // events rising above directors
  const EVENTS_TOP_STEP = 18;
  const EVENTS_BOT_BASE = DIRECTORS_Y_START + 3 * (DIRECTOR_H + DIRECTOR_GAP) + 10;
  const EVENTS_BOT_STEP = 18;

  // Assign lane (row number from the anchor) to avoid label collisions.
  // Events laid above director bars (publications, context) rise upward; below (campaigns, discoveries) go downward.
  const MIN_X_GAP = 18; // minimum px between same-lane dots
  const topLanes = [];
  const botLanes = [];

  function assignLane(eventX, lanes) {
    for (let i = 0; i < lanes.length; i++) {
      if (Math.abs(lanes[i] - eventX) > MIN_X_GAP) {
        lanes[i] = eventX;
        return i;
      }
    }
    lanes.push(eventX);
    return lanes.length - 1;
  }

  EVENTS.forEach((ev, idx) => {
    ev._id = 'ev' + idx;
    ev._x = x(ev.year);
    const goUp = (ev.type === 'publication' || ev.type === 'context');
    if (goUp) {
      ev._lane = assignLane(ev._x, topLanes);
      ev._dotY = EVENTS_TOP_BASE - ev._lane * EVENTS_TOP_STEP;
    } else {
      ev._lane = assignLane(ev._x, botLanes);
      ev._dotY = EVENTS_BOT_BASE + ev._lane * EVENTS_BOT_STEP;
    }
  });

  // Draw guide lines from each event dot to the axis (or director bars)
  EVENTS.forEach(ev => {
    const goUp = (ev.type === 'publication' || ev.type === 'context');
    const targetY = goUp
      ? DIRECTORS_Y_START - 2
      : DIRECTORS_Y_START + 3 * (DIRECTOR_H + DIRECTOR_GAP) + 2;
    svg.appendChild(el('line', {
      x1: ev._x, y1: ev._dotY, x2: ev._x, y2: targetY,
      stroke: TYPE_COLORS[ev.type], class: 'tl-event-line',
      'data-ev-line': ev._id
    }));
  });

  // Draw event dots
  EVENTS.forEach(ev => {
    const dot = el('circle', {
      cx: ev._x, cy: ev._dotY, r: EVENT_DOT_RADIUS,
      fill: TYPE_COLORS[ev.type],
      stroke: '#fff', 'stroke-width': 1.5,
      class: 'tl-event-dot',
      'data-ev-id': ev._id,
      'data-type': ev.type,
      tabindex: 0,
      role: 'button',
      'aria-label': ev.year + ', ' + ev.title
    });
    svg.appendChild(dot);
  });

  // ====================================================================
  // FULL LIST (below the SVG)
  // ====================================================================

  const listRoot = document.getElementById('timeline-list');
  const decades = {};
  EVENTS.forEach(ev => {
    const decade = Math.floor(ev.year / 10) * 10;
    if (!decades[decade]) decades[decade] = [];
    decades[decade].push(ev);
  });
  Object.keys(decades).sort().forEach(decade => {
    const wrap = document.createElement('div');
    wrap.className = 'tl-decade';
    const h = document.createElement('h3');
    h.className = 'tl-decade-heading';
    h.textContent = decade + 's';
    wrap.appendChild(h);
    const eventsWrap = document.createElement('div');
    eventsWrap.className = 'tl-decade-events';
    decades[decade].forEach(ev => {
      const card = document.createElement('article');
      card.className = 'tl-event';
      card.id = ev._id + '-card';
      card.dataset.type = ev.type;
      card.dataset.evId = ev._id;
      card.innerHTML = `
        <div class="tl-e-year">${ev.year}</div>
        <div class="tl-e-body">
          <h4 class="tl-e-title">${ev.title}</h4>
          ${ev.person ? `<p class="tl-e-person">${ev.person}</p>` : ''}
          <p class="tl-e-desc">${ev.desc}</p>
          <div class="tl-e-meta">
            ${ev.houses ? `<span><em>Buildings:</em> ${ev.houses}</span>` : ''}
            ${ev.source ? `<span><em>Source:</em> ${ev.source}</span>` : ''}
          </div>
        </div>
      `;
      eventsWrap.appendChild(card);
    });
    wrap.appendChild(eventsWrap);
    listRoot.appendChild(wrap);
  });

  // ====================================================================
  // INTERACTION: hover, selection, filter
  // ====================================================================

  const hoverEl = document.getElementById('timeline-hover');
  const detailEl = document.getElementById('timeline-detail');
  let selectedEv = null;
  let currentFilter = 'all';

  function renderDetail(ev) {
    if (!ev) {
      detailEl.innerHTML = '<div class="td-empty"><p><strong>Select an event above</strong> to read its description, the houses or buildings it uncovered, and the source citation. Or scroll down for the full chronological list.</p></div>';
      return;
    }
    detailEl.innerHTML = `
      <div class="td-card">
        <div class="td-year">${ev.year}<span class="td-type-badge td-type-${ev.type}">${TYPE_LABELS[ev.type]}</span></div>
        <h3 class="td-title">${ev.title}</h3>
        ${ev.person ? `<p class="td-person">${ev.person}</p>` : ''}
        <p class="td-desc">${ev.desc}</p>
        ${ev.houses ? `<p class="td-houses"><em>Buildings:</em> ${ev.houses}</p>` : ''}
        ${ev.source ? `<p class="td-source">Source: ${ev.source}</p>` : ''}
      </div>
    `;
  }

  function applyFilter(filter) {
    currentFilter = filter;
    document.querySelectorAll('.tf-chip').forEach(c => {
      c.classList.toggle('is-active', c.dataset.filter === filter);
    });
    document.querySelectorAll('.tl-event-dot').forEach(d => {
      const t = d.dataset.type;
      const show = (filter === 'all' || filter === t);
      d.classList.toggle('is-dim', !show);
    });
    document.querySelectorAll('[data-ev-line]').forEach(l => {
      const evId = l.dataset.evLine;
      const ev = EVENTS.find(e => e._id === evId);
      const show = (filter === 'all' || filter === ev.type);
      l.classList.toggle('is-dim', !show);
    });
    document.querySelectorAll('.tl-event').forEach(c => {
      const t = c.dataset.type;
      const show = (filter === 'all' || filter === t);
      c.classList.toggle('is-dim', !show);
    });
  }

  // Hover tooltip on dots
  const vizWrap = document.querySelector('.timeline-viz-wrap');
  function showHover(ev, pageX, pageY) {
    hoverEl.innerHTML = `<div class="th-year">${ev.year} · ${TYPE_LABELS[ev.type]}</div>${ev.title}`;
    const wrapRect = vizWrap.getBoundingClientRect();
    const tlX = pageX - wrapRect.left - window.scrollX;
    const tlY = pageY - wrapRect.top - window.scrollY;
    hoverEl.style.left = Math.min(Math.max(tlX + 12, 8), wrapRect.width - 260) + 'px';
    hoverEl.style.top = Math.max(tlY - 10, 8) + 'px';
    hoverEl.classList.add('is-visible');
  }
  function hideHover() {
    hoverEl.classList.remove('is-visible');
  }

  svg.addEventListener('mouseover', e => {
    const dot = e.target.closest('.tl-event-dot');
    if (!dot) return;
    const evId = dot.dataset.evId;
    const ev = EVENTS.find(x => x._id === evId);
    if (!ev) return;
    showHover(ev, e.pageX, e.pageY);
  });
  svg.addEventListener('mousemove', e => {
    const dot = e.target.closest('.tl-event-dot');
    if (!dot) { hideHover(); return; }
    const evId = dot.dataset.evId;
    const ev = EVENTS.find(x => x._id === evId);
    if (ev) showHover(ev, e.pageX, e.pageY);
  });
  svg.addEventListener('mouseleave', hideHover);

  // Click -> select event, render detail, highlight card in list
  function selectEvent(ev) {
    selectedEv = ev;
    document.querySelectorAll('.tl-event-dot').forEach(d => d.classList.remove('is-selected'));
    document.querySelectorAll('.tl-event').forEach(c => c.classList.remove('is-highlight'));
    if (!ev) return;
    const dot = svg.querySelector(`[data-ev-id="${ev._id}"]`);
    if (dot) dot.classList.add('is-selected');
    const card = document.getElementById(ev._id + '-card');
    if (card) card.classList.add('is-highlight');
    renderDetail(ev);
    // Smooth-scroll the detail panel into view, gently
    const detailRect = detailEl.getBoundingClientRect();
    if (detailRect.top < 80 || detailRect.top > window.innerHeight - 120) {
      detailEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  svg.addEventListener('click', e => {
    const dot = e.target.closest('.tl-event-dot');
    if (!dot) return;
    const ev = EVENTS.find(x => x._id === dot.dataset.evId);
    if (ev) selectEvent(ev);
  });
  svg.addEventListener('keydown', e => {
    if (e.key !== 'Enter' && e.key !== ' ') return;
    const dot = e.target.closest('.tl-event-dot');
    if (!dot) return;
    e.preventDefault();
    const ev = EVENTS.find(x => x._id === dot.dataset.evId);
    if (ev) selectEvent(ev);
  });

  // Clicking a card also selects
  listRoot.addEventListener('click', e => {
    const card = e.target.closest('.tl-event');
    if (!card) return;
    const ev = EVENTS.find(x => x._id === card.dataset.evId);
    if (ev) selectEvent(ev);
  });

  // Filter chip click
  document.querySelectorAll('.tf-chip').forEach(chip => {
    chip.addEventListener('click', () => applyFilter(chip.dataset.filter));
  });

  // Keyboard nav between dots (left/right arrows)
  document.addEventListener('keydown', e => {
    if (!selectedEv) return;
    if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
    const visible = EVENTS.filter(ev => currentFilter === 'all' || ev.type === currentFilter);
    visible.sort((a, b) => a.year - b.year || a._id.localeCompare(b._id));
    const idx = visible.findIndex(ev => ev._id === selectedEv._id);
    if (idx === -1) return;
    let next;
    if (e.key === 'ArrowLeft') next = visible[Math.max(0, idx - 1)];
    else next = visible[Math.min(visible.length - 1, idx + 1)];
    if (next) selectEvent(next);
  });

})();
</script>

{% include cite-block.html %}
