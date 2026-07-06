#!/usr/bin/env python3
"""Export the Timgad houses database (v12 xlsx, HOUSES sheet) to _data/houses.json.

Raw columns are copied verbatim. Derived fields (marked _derived in name comments):
name_en / name_fr (split on final parenthetical), zone, type_class, area_m2.
Usage: python3 export_houses.py <xlsx path> <output json path>
"""
import json, re, sys
import openpyxl

XLSX, OUT = sys.argv[1], sys.argv[2]

# The 12-house dissertation sample publishes full records (notes, references).
# All other houses publish index metadata only until the analysis is defended.
SAMPLE_IDS = {
    "TIMG.E-SW.I1", "TIMG.E-SW.I2", "TIMG.SW.I5", "TIMG.E-SE.I4",
    "TIMG.NW.I6", "TIMG.E-SE.I5", "TIMG.NE.I1", "TIMG.E-NW.I14",
    "TIMG.SE.I7", "TIMG.E-NW.I18", "TIMG.E-NW.I19", "TIMG.E-NW.I6",
}

def clean(v):
    if v is None: return ""
    return re.sub(r"\s+", " ", str(v)).strip()

def split_name(name):
    m = re.match(r"^(.*?)\s*\(([^()]*)\)\s*$", name)
    if m: return m.group(1).strip(), m.group(2).strip()
    return name, ""

def zone(q):
    if q in ("NW","NE","SW","SE"): return "Intramural " + q
    if q.startswith("E-"): return "Extramural " + q[2:]
    return "Unlocated"

def type_class(bt):
    t = bt.lower()
    if "elite" in t or "flamen" in t: return "Elite house"
    if "collective" in t: return "Possibly collective"
    if "warehouse" in t or "mixed-use" in t: return "Warehouse / mixed-use"
    if "block" in t or "insula" in t: return "Residential block"
    if "house" in t or "residential" in t: return "House"
    return "Uncertain"

def area_m2(raw):
    if not raw: return None
    m = re.search(r"~?\s*([\d][\d\s.,]*)\s*m²", raw)
    if not m: return None
    n = m.group(1).replace(" ", "").replace(",", "")
    try: return round(float(n))
    except ValueError: return None

wb = openpyxl.load_workbook(XLSX, data_only=True)
ws = wb["HOUSES"]
hdr = [c.value for c in ws[1]]
houses = []
for r in ws.iter_rows(min_row=2):
    row = dict(zip(hdr, [c.value for c in r]))
    if not any(v not in (None, "") for v in row.values()): continue
    name = clean(row["House Name"])
    en, fr = split_name(name)
    q = clean(row["Quadrant"])
    ar = clean(row["Approx. Area (l x w)"])
    houses.append({
        "grid_id": clean(row["Grid ID"]),
        "name": name,
        "name_en": en,
        "name_fr": fr,
        "alternate_names": clean(row["Alternate Names"]),
        "quadrant": q,
        "zone": zone(q),
        "building_type": clean(row["Building Type"]),
        "type_class": type_class(clean(row["Building Type"])),
        "confidence": clean(row["Confidence"]).lower(),
        "mapping_confidence": clean(row["Mapping Confidence"]).lower(),
        "area_raw": ar,
        "area_m2": area_m2(ar),
        "first_published_by": clean(row["First Published By"]),
        "key_references": clean(row["Key References"]),
        "possible_duplicate_of": clean(row["Possible Duplicate Of"]),
        "notes": clean(row["Notes"]),
    })
    h = houses[-1]
    h["sample"] = h["grid_id"] in SAMPLE_IDS
    if not h["sample"]:
        h["notes"] = ""
        h["key_references"] = ""

houses.sort(key=lambda h: h["grid_id"])
out = {"version": "v12 FINAL 2026-07-05", "generated_from": "Timgad_Houses_Database_v12_FINAL_2026-07-05.xlsx, HOUSES sheet", "count": len(houses), "houses": houses}
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("wrote", OUT, "houses:", len(houses))
import collections
print("type_class:", dict(collections.Counter(h["type_class"] for h in houses)))
print("zones:", dict(collections.Counter(h["zone"] for h in houses)))
print("areas parsed:", sum(1 for h in houses if h["area_m2"]))
print("full records (sample):", sum(1 for h in houses if h["sample"])) 
