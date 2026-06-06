---
layout: page
title: Journal
subtitle: Field notes from my own workflow, written as the project happens, not after.
permalink: /notes/
last_updated: 2026-06-04
published: true
---

<p class="page-intro">A quick word on what this is, since "journal" can mean a few things. This is not an academic journal, peer reviewed and final. It is not quite a personal diary either. Think of it as a set of field notes, but of my own making: honest write-ups of how this project actually comes together, written while it is happening rather than tidied up years later. Some posts walk through a workflow or a tool I am learning. Some work through a question about Roman houses. All of them are written in real time, with the false starts left in, because the process is part of the story.</p>

<ul class="post-list">
  {% for post in site.posts %}
  <li>
    <p class="post-meta">
      {{ post.date | date: "%B %-d, %Y" }}
      {% if post.reading_time %} · <span class="post-readtime">{{ post.reading_time }} min read</span>{% endif %}
      {% if post.categories %} · {{ post.categories | join: ', ' }}{% endif %}
    </p>
    <h3 class="post-title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    {% if post.excerpt %}<p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 40 }}</p>{% endif %}
  </li>
  {% endfor %}
</ul>
