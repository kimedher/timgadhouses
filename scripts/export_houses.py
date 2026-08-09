#!/usr/bin/env python3
"""Export the Timgad houses database (v13 xlsx, HOUSES sheet) to _data/houses.json.

Raw columns are copied verbatim. Derived fields (marked _derived in name comments):
name_en / name_fr (split on final parenthetical), zone, type_class, area_m2.
verification_status is the v13 "Verification Status" column normalized to
verified / partial / review.
Usage: python3 export_houses.py <xlsx path> <output json path>
"""
import csv, datetime, json, os, re, sys
import openpyxl

XLSX, OUT = sys.argv[1], sys.argv[2]

# Public-notes overlay: prose rewrites of the working notes, keyed by grid_id.
# When a grid_id appears here, its note replaces the xlsx note at export time,
# so the public site carries readable prose while the database keeps its
# working shorthand.
OVERLAY_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public_notes.csv")
PUBLIC_NOTES = {}
if os.path.exists(OVERLAY_CSV):
    with open(OVERLAY_CSV, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            PUBLIC_NOTES[row["grid_id"].strip()] = row["note"].strip()

# Analysis-progress overlay: grid_ids with a status of "drawn" or "case_study";
# every house absent from the csv exports as "pending".
ANALYSIS_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "analysis_status.csv")
ANALYSIS_STATUS = {}
if os.path.exists(ANALYSIS_CSV):
    with open(ANALYSIS_CSV, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            ANALYSIS_STATUS[row["grid_id"].strip()] = row["status"].strip()

# The 12-house dissertation sample publishes full records (notes, references).
# All other houses publish index metadata only until the analysis is defended.
SAMPLE_IDS = {
    "TIMG.E-SW.I1", "TIMG.E-SW.I2", "TIMG.SW.I5", "TIMG.E-SE.I4",
    "TIMG.NW.I6", "TIMG.E-SE.I5", "TIMG.SE.I2", "TIMG.NW.I17",
    "TIMG.SW.I8", "TIMG.E-NW.I18", "TIMG.E-NW.I19", "TIMG.NW.I25",
}

def clean(v):
    if v is None: return ""
    return re.sub(r"\s+", " ", str(v)).strip()

def strip_editorial_tags(s):
    # Public output stays clean: drop "[moved from ...]" editorial markers
    # and database-version tokens like ", v13". The xlsx keeps its markers;
    # this is export-side only.
    s = re.sub(r"\s*\[moved from[^\]]*\]\s*", " ", s, flags=re.IGNORECASE)
    s = re.sub(r",\s*v1\d+\]", "]", s)
    return re.sub(r"\s+", " ", s).strip()

def clean_citation(s):
    # Drop internal workflow tokens from public citation fields; the xlsx
    # keeps them. Applied to first_published_by only.
    s = re.sub(
        r"\s*\((?:printed; verify in text|printed; needs scan receipt|"
        r"probable; needs scan receipt|exact page needs Kim)\)", "", s)
    s = s.replace("BIAA-Af-Alg-24, ", "").replace("(BIAA-Af-Alg-24)", "")
    s = re.sub(r"(:\s*)~(\d)", r"\1\2", s)  # "Ballu 1911: ~78-79" -> ": 78-79"
    return re.sub(r"\s+", " ", s).strip()

def split_name(name):
    # Split off the final balanced parenthetical as the French name; handles
    # nested parentheses like "House 83 (formerly 91) (Maison 83 (ex-91))".
    if name.endswith(")"):
        depth = 0
        for i in range(len(name) - 1, -1, -1):
            if name[i] == ")":
                depth += 1
            elif name[i] == "(":
                depth -= 1
                if depth == 0:
                    return name[:i].strip(), name[i + 1:-1].strip()
    return name, ""

def zone(q):
    if q in ("NW","NE","SW","SE"): return "Intramural " + q
    if q.startswith("E-"): return "Extramural " + q[2:]
    return "Unlocated"

def type_class(bt):
    t = bt.lower()
    if "elite" in t or "flamen" in t: return "Elite house"
    if "collective" in t or "warehouse" in t or "mixed-use" in t: return "Mixed-use / other"
    if "block" in t or "insula" in t: return "Residential block"
    if "isolated" in t: return "Freestanding house"
    if "house" in t or "residential" in t: return "House"
    return "Uncertain"

VSTATUS = {
    "VERIFIED": "verified",
    "PARTIALLY VERIFIED": "partial",
    "NEEDS REVIEW": "review",
}

def verification_status(v):
    key = clean(v).upper()
    if key not in VSTATUS:
        raise ValueError(f"Unexpected Verification Status: {v!r}")
    return VSTATUS[key]

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
        "verification_status": verification_status(row["Verification Status"]),
        "analysis_status": ANALYSIS_STATUS.get(clean(row["Grid ID"]), "pending"),
        "area_raw": ar,
        "area_m2": area_m2(ar),
        "first_published_by": clean_citation(clean(row["First Published By"])),
        "key_references": clean(row["Key References"]),
        "possible_duplicate_of": clean(row["Possible Duplicate Of"]),
        "notes": strip_editorial_tags(clean(row["Notes"])),
    })
    h = houses[-1]
    h["sample"] = h["grid_id"] in SAMPLE_IDS
    if not h["sample"]:
        h["notes"] = ""
        h["key_references"] = ""
    if h["grid_id"] in PUBLIC_NOTES:
        h["notes"] = PUBLIC_NOTES[h["grid_id"]]

houses.sort(key=lambda h: h["grid_id"])
out = {"generated": datetime.date.today().isoformat(), "count": len(houses), "houses": houses}
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("wrote", OUT, "houses:", len(houses))
import collections
print("type_class:", dict(collections.Counter(h["type_class"] for h in houses)))
print("zones:", dict(collections.Counter(h["zone"] for h in houses)))
print("areas parsed:", sum(1 for h in houses if h["area_m2"]))
print("full records (sample):", sum(1 for h in houses if h["sample"])) 
