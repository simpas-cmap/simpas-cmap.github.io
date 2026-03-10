#!/usr/bin/env python3
import requests
import icalendar
from datetime import datetime, date, timedelta, timezone

# === CONFIG ===
ICS_URL = "https://calendar.google.com/calendar/ical/2c521jtulagu5g6hg4kprtsiok%40group.calendar.google.com/public/basic.ics"
OUTPUT_FILE = "_pages/agenda.md"

# Fetch ICS
resp = requests.get(ICS_URL)
resp.raise_for_status()

cal = icalendar.Calendar.from_ical(resp.content)

# Current time (UTC) as naive datetime
now = datetime.utcnow()

# Collect upcoming events
events = []

for component in cal.walk():
    if component.name == "VEVENT":
        start = component.get('dtstart').dt
        dtend = component.get('dtend')
        end = dtend.dt if dtend else start
        summary = component.get('summary')
        location = component.get('location')

        # Convert all-day events (date instead of datetime)
        if isinstance(start, date) and not isinstance(start, datetime):
            start = datetime.combine(start, datetime.min.time())
        if isinstance(end, date) and not isinstance(end, datetime):
            end = datetime.combine(end, datetime.min.time())

        # Make timezone-aware datetimes naive in UTC
        if start.tzinfo:
            start = start.astimezone(timezone.utc).replace(tzinfo=None)
        if end.tzinfo:
            end = end.astimezone(timezone.utc).replace(tzinfo=None)

        # Only keep upcoming events
        if end >= now:
            events.append((start, end, summary, location))

# Sort by start time
events.sort(key=lambda x: x[0])

# Write Markdown
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("---\n")
    f.write("layout: page\n")
    f.write("title: Agenda\n")
    f.write("permalink: /agenda/\n")
    f.write("---\n\n")
    f.write("# Upcoming Agenda\n\n")

    if not events:
        f.write("No upcoming events.\n")

    for start, end, summary, location in events:
        start_str = start.strftime("%Y-%m-%d %H:%M")
        end_str = end.strftime("%H:%M")
        line = f"- **{summary}** ({start_str} - {end_str})"
        if location:
            line += f" at {location}"
        f.write(line + "\n")

print(f"Agenda page updated: {OUTPUT_FILE} ({len(events)} upcoming events)")
