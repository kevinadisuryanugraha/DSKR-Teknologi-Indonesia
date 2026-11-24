# DSKR Teknologi Indonesia — Dokumen Internal 2026

Satu halaman, tiga dokumen (v3.0, digabung 2026-11-24). Alasan: satu berkas, satu URL, satu siklus revisi — tidak ada versi yang tertinggal.

```
dskr/
├── index.html                  SATU HALAMAN: Brand Book (01–09) + Business Playbook (10–18) + Sales Kit (19–27)
├── README.md                   berkas ini
├── assets/                     aset bersama
│   ├── brand.css               token warna, tipografi, komponen (termasuk .part-head, .toc-grid, .totop)
│   ├── dskr-logo.png           logo navy, transparan (latar terang)
│   ├── dskr-logo-on-dark.png   logo putih, transparan (latar navy)
│   ├── dskr-logo-source.png    sumber asli 1600x524 opaque, jangan dipakai di navy
│   ├── favicon.png             512px monogram
│   ├── apple-touch-icon.png    180px
│   └── og-image.png            1200x630
├── source/                     masukan mentah, jangan diedit
│   ├── proposal_bisnis_it.pdf  proposal bisnis 2026, sumber semua angka
│   ├── proposal.txt            ekstraksi teks PDF
│   └── brandkit.txt            ekstraksi teks brand kit v1.0
└── archive/                    dokumen lama, hanya referensi
    ├── v2-terpisah/            versi 3-halaman sebelum digabung
    │   ├── brand-book.html
    │   ├── business-playbook.html
    │   └── sales-kit.html
    ├── DSKR Teknologi Indonesia — Brand Kit 2026.html   v1.0, satu berkas 1,9 MB
    ├── backup-brand-kit-v1-sebelum-fix-gelap.html       v1.0 sebelum perbaikan tema
    └── screenshots/
        ├── verify-merged-top.png
        ├── verify-merged-part2.png
        ├── screenshot-tema-gelap-masalah.png
        ├── screenshot-tema-terang-setelah-fix.png
        ├── verify-brand-book.png
        ├── verify-business-playbook.png
        └── verify-sales-kit.png
```

## Struktur halaman

| Rentang | Bagian | Audiens |
|---|---|---|
| — | Hero + Status/Blocker + Peta 27 bagian | internal |
| 01–09 | Brand Book: fondasi, logo, warna, tipografi, grafis, voice, aksesibilitas, kolateral, tata kelola | desainer, vendor, tim |
| 10–18 | Business Playbook: prinsip, layanan, skema bayar, provider, tim, risiko, legal, KPI, roadmap | internal |
| 19–27 | Sales Kit: data resmi, persona, paket, skema, objection, template, one-pager, cadence, bahasa | sales (+ sebagian ke klien) |

Nomor bagian berurutan 01–27. Setiap bagian punya `id` yang bisa ditautkan langsung (`index.html#layanan`, `#provider`, `#paket`, dst.).

## Aturan

1. Token warna dan ukuran hanya diubah di `assets/brand.css` — bukan di `index.html`.
2. Satu berkas: konten baru masuk sebagai `<section>` baru di `index.html` dengan nomor lanjut, bukan berkas baru. Konten yang dihapus pindah ke `archive/`.
3. Teks minimum 12px. Merah `#CC1927` dilarang sebagai teks di atas navy — pakai `#FF5A65`.
4. `.tbd` / `[isi ...]` wajib dipakai untuk data yang belum ada. Angka fiktif dilarang.
5. Nomor versi dan tanggal di footer diperbarui setiap rilis.
6. Halaman ini `noindex` dan berlabel internal. Jangan di-deploy publik apa adanya — bagian 10–18 memuat margin, formula harga, dan risk register.

## Responsif

Enam titik henti di `assets/brand.css`, semuanya di bawah satu set token.

| Lebar | Ubah |
|---|---|
| ≤1024 | `--pad-x: 1.25rem` |
| ≤900 | hero & `.split` satu kolom, `g3/g4` dua kolom, footer dua kolom, `--section-y: 3rem` |
| ≤760 | `g2`, `.dodont` satu kolom |
| ≤640 | `--topbar-h: 56px`, `--section-y: 2.75rem`, `--table-min: 520px`, semua grid satu kolom, tabel geser horizontal dengan kolom pertama menempel |
| ≤480 | `--section-y: 2.25rem`, `--pad-x: 1rem`, hero h1 1.55rem |
| ≤380 | hero h1 1.45rem, jarak nav dirapatkan |

Token di `:root`: `--pad-x`, `--section-y`, `--topbar-h`, `--table-min`. `scroll-padding-top` dan `scroll-margin-top` dihitung dari `--topbar-h`, jadi jangkar tidak pernah tertutup topbar saat tingginya berubah.

`@media (pointer: coarse)` menaikkan semua sasaran sentuh ke ≥44px di tablet maupun ponsel. `@media (hover: none)` mematikan keadaan hover.

Diverifikasi otomatis (Chrome headless, 320/360/480/640/768/900/1024/1440): tidak ada overflow halaman, tidak ada kotak yang melampaui viewport, tidak ada elemen bertumpuk, tidak ada teks <12px. Tabel lebar hanya menggeser di dalam `.table-wrap`, bukan halaman.

## Blocker belum selesai

- [ ] Kontak resmi: telepon, WhatsApp, email, alamat, handle sosial
- [ ] Harga paket dan tenor cicilan
- [ ] NIB / NPWP / rekening bisnis
- [ ] Master logo SVG/AI (sekarang hanya PNG raster)
- [ ] Verifikasi kemitraan: Tokease, RNA.id, Perwira Cloud AS211407, PT Ref Group Indonesia
- [ ] Template SPK, invoice, SLA, berita acara serah terima (berkas terpisah)
- [ ] Portofolio project pertama