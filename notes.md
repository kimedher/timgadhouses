---
layout: page
title: Notes & Essays
subtitle: Short pieces on method, scholarship, teaching, and what is changing in how we read provincial Roman houses.
permalink: /notes/
last_updated: 2026-04-18
---

<ul class="post-list">
  {% for post in site.posts %}
  <li>
    <p class="post-meta">
      {{ post.date | date: "%B %-d, %Y" }}
      {% if post.reading_time %} · {{ post.reading_time }} min read{% endif %}
      {% if post.categories %} · {{ post.categories | join: ', ' }}{% endif %}
    </p>
    <h3 class="post-title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    {% if post.excerpt %}<p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 40 }}</p>{% endif %}
  </li>
  {% endfor %}
</ul>
