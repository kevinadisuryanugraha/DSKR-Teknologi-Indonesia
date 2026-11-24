#!/usr/bin/env python
"""Bangun PDF dari index.html: cetak A4 (Chrome headless), tambah footer
nomor halaman + bookmark, simpan ke DSKR-Dokumen-Internal-2026.pdf.

Butuh: Chrome, Python + PyMuPDF (pip install pymupdf).
Jalankan dari root repo:  python tools/pdf.py
"""
import io
import re
import subprocess
import sys
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
CHROME = Path(r'C:/Program Files/Google/Chrome/Application/chrome.exe')
HTML = ROOT / 'index.html'
TMP = ROOT / '_print.pdf'
OUT = ROOT / 'DSKR-Dokumen-Internal-2026.pdf'
FONT = ROOT / 'assets/fonts/plus-jakarta-sans-400.woff'
TTF = ROOT / '_pjs-400.ttf'
PAGE_TEXT = 'DSKR Teknologi Indonesia  \u00b7  Dokumen Internal 2026 v3.0  \u00b7  Konfidensial'


def render():
    if not CHROME.exists():
        sys.exit('Chrome tidak ditemukan: %s' % CHROME)
    subprocess.run([
        str(CHROME), '--headless=new', '--disable-gpu', '--no-sandbox',
        '--no-pdf-header-footer', '--virtual-time-budget=10000',
        '--run-all-compositor-stages-before-draw',
        '--print-to-pdf=%s' % TMP, HTML.as_uri(),
    ], check=True)


def ttf():
    from fontTools.ttLib import TTFont
    f = TTFont(str(FONT))
    f.flavor = None
    f.save(str(TTF))
    return TTF


def clean(t):
    t = re.sub(r'<[^>]+>', '', t)
    t = t.replace('&amp;', '&').replace('&nbsp;', ' ')
    return ' '.join(t.split())


def main():
    render()
    doc = pymupdf.open(TMP)
    n = doc.page_count
    w, h = doc[0].rect.width, doc[0].rect.height
    ml = 14 / 25.4 * 72
    gray = (0.392, 0.408, 0.427)
    fontpath = ttf()
    f = pymupdf.Font(fontfile=str(fontpath))

    for i, page in enumerate(doc, 1):
        page.insert_font(fontname='pjs', fontfile=str(fontpath))
        y = h - 24
        page.draw_line(pymupdf.Point(ml, y - 9), pymupdf.Point(w - ml, y - 9),
                       color=(0.91, 0.918, 0.929), width=0.4)
        page.insert_text((ml, y + 1), PAGE_TEXT, fontname='pjs', fontsize=7, color=gray)
        label = 'hal. %d / %d' % (i, n)
        tw = f.text_length(label, fontsize=7)
        page.insert_text((w - ml - tw, y + 1), label, fontname='pjs', fontsize=7, color=gray)

    html = io.open(HTML, encoding='utf-8').read()
    raw = [(10 ** 9, 1, 'Peta Halaman')]
    for m in re.finditer(r'<div class="part-head[^"]*"[^>]*>(.*?)</div>\s*\n', html, re.S):
        seg = html[m.start():m.start() + 1200]
        h2 = re.search(r'<h2[^>]*>(.*?)</h2>', seg, re.S)
        if h2:
            raw.append((m.start(), 1, clean(h2.group(1))))
    for m in re.finditer(r'<section[^>]*id="([^"]+)"[^>]*>(.*?)</section>', html, re.S):
        sid, body = m.group(1), m.group(2)
        if sid in ('status', 'peta'):
            continue
        h2 = re.search(r'<h2[^>]*>(.*?)</h2>', body, re.S)
        if h2:
            raw.append((m.start(), 2, clean(h2.group(1))))
    raw.sort()

    cursor = 3
    toc = [[1, 'Sampul & Status', 1]]
    for _off, lvl, title in raw:
        if title == 'Peta Halaman':
            toc.append([1, title, 2])
            continue
        key = re.split(r'[\u2014\u2013]', title)[0].strip()[:34]
        found = None
        for p in range(cursor, n + 1):
            if doc[p - 1].search_for(key):
                found = p
                break
        if not found:
            print('! judul tidak ditemukan:', title)
            continue
        cursor = found
        toc.append([lvl, title, found])

    doc.set_toc(toc)
    doc.save(OUT, garbage=4, deflate=True)
    TMP.unlink(missing_ok=True)
    TTF.unlink(missing_ok=True)
    print('OK -> %s (%d halaman, %d bookmark)' % (OUT.name, n, len(toc)))


if __name__ == '__main__':
    main()
