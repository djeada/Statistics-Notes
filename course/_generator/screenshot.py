#!/usr/bin/env python3
"""Screenshot one provisioned dashboard:  python screenshot.py stats-03-percentiles out.png [http://localhost:3055]
(needs playwright + chromium; see the course README)"""
import sys
from playwright.sync_api import sync_playwright

uid, out = sys.argv[1], sys.argv[2]
base = sys.argv[3] if len(sys.argv) > 3 else "http://localhost:3055"
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1500, "height": 1100})
    pg.goto(f"{base}/d/{uid}/x?orgId=1&kiosk", wait_until="networkidle")
    pg.wait_for_timeout(4000)
    pg.screenshot(path=out, full_page=True)
    b.close()
