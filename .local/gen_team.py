import pandas as pd
from datetime import datetime

def parse_date(d):
    if pd.isna(d) or str(d).strip() == "":
        return None
    try:
        return datetime.strptime(str(d).strip(), "%d/%m/%Y")
    except:
        return None


def read_csv_auto(path):
    """Read CSV detecting separator automatically"""
    return pd.read_csv(path, sep=None, engine="python")


permanent = []
postdocs = []
phds = []
alumni = []


# ---------------- Permanent members ----------------

df = read_csv_auto("perm.csv")

df.columns = [c.strip().lower() for c in df.columns]

for _, row in df.iterrows():

    prenom = str(row.get("prenom", "")).strip()
    nom = str(row.get("nom", "")).strip()
    name = f"{prenom} {nom}".strip()

    position = str(row.get("type", "")).strip().lower()

    start = parse_date(row.get("debut"))
    end = parse_date(row.get("fin"))

    if end:
        alumni.append((name, start, end, position))
    else:
        permanent.append((name, position))


# ---------------- Postdocs ----------------

df = read_csv_auto("post-doc.csv")

for _, row in df.iterrows():

    name = f"{row['prenom']} {row['nom']}"

    supervisors = str(row.iloc[0]).replace(";;", "").split(";")
    supervisors = [s.strip() for s in supervisors if s.strip()]

    start = parse_date(row.get("debut"))
    end = parse_date(row.get("fin"))

    if end:
        alumni.append((name, start, end, "postdoc"))
    else:
        postdocs.append((name, supervisors))


# ---------------- PhD students ----------------

df = read_csv_auto("doc.csv")

for _, row in df.iterrows():

    name = f"{row['prenom']} {row['nom']}"

    supervisors = str(row.iloc[0]).replace(";;", "").split(";")
    supervisors = [s.strip() for s in supervisors if s.strip()]

    start = parse_date(row.get("debut"))
    end = parse_date(row.get("fin"))

    if end:
        alumni.append((name, start, end, "phd"))
    else:
        phds.append((name, supervisors, start))


# ---------------- Markdown output ----------------

print("### Permanent Members\n")
for name, position in permanent:
    print(f"- {name} ({position})")

print("\n### Post-doc\n")
for name, supervisors in postdocs:
    sup = ", ".join(supervisors)
    print(f"- {name} ({sup})")

print("\n### PhD students\n")
for name, supervisors, start in phds:
    sup = ", ".join(supervisors)
    start_str = start.strftime("%Y") if start else "?"
    print(f"- {name} (started {start_str}, supervision by {sup})")

print("\n### Alumni\n")
for name, start, end, position in alumni:
    s = start.strftime("%Y") if start else "?"
    e = end.strftime("%Y") if end else "?"
    print(f"- {name} ({s}, {e}, {position})")
