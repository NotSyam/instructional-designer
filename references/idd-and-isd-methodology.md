# Instructional Design Document (IDD) & ISD Methodology Reference

> **Version**: 3.2.0 | **Domain**: Curriculum Architecture, L&D Enterprise Documentation, & Project Governance  
> **Theoretical Foundation**: Grounded in *Survey of Instructional Design Models (6th Edition)* by Tonia A. Dousay & Robert Maribe Branch (Brill / AECT, 2022).

---

## 1. The L&D Documentation Hierarchy

An **Instructional Design Document (IDD)** serves as the master architectural contract between the Instructional Designer, Stakeholders, SMEs, and Developers before media production or storyboarding begins.

```
+----------------------------------------------------------------------------------------+
|                        HIERARKI DOKUMENTASI INSTRUCTIONAL DESIGN                       |
+----------------------------------------------------------------------------------------+
| 1. Needs Analysis Report   -> Diagnosis: kesenjangan performa, akar masalah, audiens   |
| 2. INSTRUCTIONAL DESIGN    -> ARSITEKTUR MAKRO: Kontrak strategi, scoring M-IDA,       |
|    DOCUMENT (IDD)             LMS, WCAG, kriteria evaluasi, DoD, dan RACI sign-off     |
| 3. ISD Project Plan (WBS)  -> MANAJEMEN PROYEK: Timeline kontekstual & review SLA      |
| 4. Course Blueprint        -> MATRIKS KURIKULUM: Modul, objektif, aktivitas, asesmen   |
| 5. Storyboard / Script     -> DETAIL MIKRO: Teks per layar, audio VO, interaksi        |
| 6. Facilitator/Learner Doc -> MATERI DELIVERABLE: Panduan fasilitator, buku peserta     |
| 7. Evaluation Report       -> EVALUASI DAMPAK: Analisis data Kirkpatrick L1 - L4       |
+----------------------------------------------------------------------------------------+
```

---

## 2. Open Modular ID Architecture (M-IDA)

Alih-alih membatasi diri pada 4 pola hybrid kaku, perancangan instruksional profesional menggunakan arsitektur modular berlapis (*4-Layer Modular Stack*) berbasis taksonomi Branch & Dousay (2022):

```
┌─────────────────────────────────────────────────────────────────────────┐
│              OPEN MODULAR INSTRUCTIONAL DESIGN ARCHITECTURE (M-IDA)     │
├─────────────────────────────────────────────────────────────────────────┤
│ LAYER 1: MACRO GOVERNANCE & LIFECYCLE (The Container)                   │
│ Pilihan: ADDIE | Agile ID (Scrum) | Gentry IPDM | Seels & Glasgow ISD 2 │
├─────────────────────────────────────────────────────────────────────────┤
│ LAYER 2: TASK & KNOWLEDGE ARCHITECTURE (The Structural Engine)          │
│ Pilihan: Dick & Carey | Merrill Pebble in Pond | 4C/ID | Action Mapping │
├─────────────────────────────────────────────────────────────────────────┤
│ LAYER 3: PEDAGOGICAL & CULTURAL STRATEGY (The Delivery Experience)      │
│ Pilihan: Gagné 9 Events | UbD (Transfer) | Young CBM (Culture) | UDL   │
├─────────────────────────────────────────────────────────────────────────┤
│ LAYER 4: CONSTRAINT SCALING & EVOLUTION (The Resource Adapter)          │
│ Pilihan: Tessmer & Wedman Layers-of-Necessity (Layer 1 MVP -> Layer n)  │
└─────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Katalog 15 Model Kanonikal (Dousay & Branch, 2022)

#### Kategori A: Classroom-Oriented Models (Fokus Pengajar, Media, & Fleksibilitas)
1. **The Kemp, Morrison & Ross Model (2019)**:
   * *Karakteristik*: Desain sirkular-oval non-linier. Memungkinkan perancang masuk dari titik mana pun (topik, karakteristik siswa, atau asesmen) tanpa urutan sekuensial kaku.
   * *Cocok Untuk*: Pendidikan tinggi, kurikulum sekolah, dan kursus pelatihan internal yang dinamis.
2. **The Gerlach and Ely Model (1980)**:
   * *Karakteristik*: Menentukan konten dan objektif secara simultan (*concurrent*), disusul alokasi waktu, ruang, dan pemilihan sumber daya.
   * *Cocok Untuk*: Pengajar K-12 dan instruktur teknis yang terbiasa berpikir berbasis materi (*content-first*).
3. **Understanding by Design (UbD - Wiggins & McTighe, 2005)**:
   * *Karakteristik*: Perencanaan mundur (*backward design*): Stage 1 Desired Results -> Stage 2 Assessment Evidence (GRASPS) -> Stage 3 Learning Plan (WHERETO).
   * *Cocok Untuk*: Pembelajaran berorientasi transfer pemahaman mendalam dan berpikir kritis.

#### Kategori B: Product-Oriented Models (Fokus Paket Siap Pakai & Iterasi)
4. **The Pebble in the Pond Model (Merrill, 2020)**:
   * *Karakteristik*: Pendekatan *problem-centered* melalui efek riak air: *Problem Definition → Problem Progression → Instructional Strategy → Prototype → Evaluate*.
   * *Cocok Untuk*: Pelatihan teknis dan pemecahan masalah nyata tanpa harus terjebak penulisan objektif teoritis di awal.
5. **The Four-Component Instructional Design (4C/ID - van Merriënboer, 2017)**:
   * *Karakteristik*: Mengintegrasikan 4 komponen: Whole Learning Tasks, Supportive Information, Procedural Information, dan Part-Task Practice.
   * *Cocok Untuk*: Keterampilan kognitif kompleks, software architecture, troubleshooting mesin rumit.
6. **The Layers-of-Necessity Model (Tessmer & Wedman, 1990)**:
   * *Karakteristik*: Model evolusioner berbasis waktu dan sumber daya. Dimulai dari Layer 1 (MVP instruksional sederhana), lalu menambah Layer 2..n seiring ketersediaan waktu.
   * *Cocok Untuk*: Proyek dengan kendala sumber daya ketat, startup, dan situasi darurat.
7. **Agile Development Model (Beck et al., 2001; Dousay & Branch, 2022)**:
   * *Karakteristik*: Iteratif, participatory, daily stand-up, working product over documentation, sprint deliverable.
   * *Cocok Untuk*: Tim produk digital, e-learning cepat, dan lingkungan kerja software.
8. **Michael Allen's SAM (Successive Approximation Model)**:
   * *Karakteristik*: Savvy Start kickoff -> Iterative Prototyping (Alpha, Beta, Gold) dengan feedback berkala dari SME.
9. **Cathy Moore Action Mapping (2017)**:
   * *Karakteristik*: Analisis gap kinerja bisnis murni -> target perilaku nyata -> skenario keputusan bercabang -> informasi minimal esensial.

#### Kategori C: System-Oriented Models (Fokus Skala Enterprise & Regulasi Ketat)
10. **The Dick, Carey and Carey Model (2015)**:
    * *Karakteristik*: Pendekatan sistem preskriptif dengan analisis hierarki tugas subordinat dan instrumen tes berbasis kriteria.
    * *Cocok Untuk*: Pelatihan keselamatan kerja, sistem penerbangan, klinis, dan kepatuhan hukum berisiko tinggi.
11. **The ISD Model 2: for Practitioners (Seels & Glasgow, 1997)**:
    * *Karakteristik*: Menempatkan manajemen proyek dan difusi inovasi (*diffusion of adoption*) sepanjang fase desain hingga rilis.
    * *Cocok Untuk*: Transformasi L&D korporat besar di mana tantangan terbesarnya adalah adopsi pengguna.
12. **The Instructional Project Development and Management (IPDM) Model (Gentry, 1994)**:
    * *Karakteristik*: 8 komponen pengembangan + 5 proses pendukung terpisah (*Management, Information Handling, Resource Allocation, Personnel, Facilities*).
    * *Cocok Untuk*: Proyek multi-departemen berskala besar yang membutuhkan pengadaan fasilitas dan vendor luar.
13. **The Interservices Procedures for ISD (IPISD - Branson et al., 1975)**:
    * *Karakteristik*: Standar militer 5 fase (Analyze, Design, Develop, Implement, Control) terbagi dalam 20 langkah dengan kontrol mutu lapangan ketat.
14. **ADDIE Generic Paradigm (Branch, 2017)**:
    * *Karakteristik*: Kerangka kerja konseptual makro standar industri.

#### Kategori D: Culturally Responsive & Inclusive Models (Konteks Modern)
15. **The Culture Based Model (CBM - Patricia Young, 2008)**:
    * *Karakteristik*: 8 area budaya materi (*Inquiry, Development, Team, Assessments, Brainstorming, Learners, Elements, Training*) untuk memastikan materi bebas dari bias budaya dominan dan relevan bagi audiens global.

---

## 3. Weighted Scoring Engine 5 Dimensi

Setiap proyek dinilai pada 5 dimensi (skala 1–5):
* **D1 — Stakes / Risiko Kegagalan** (1: Minor, 3: Operasional tim, 5: Zero-tolerance/Hukum/Klinis)
* **D2 — Kompleksitas Skill** (1: Recall, 3: Prosedural multi-langkah, 5: Kognitif kompleks & heuristik)
* **D3 — Tekanan Waktu / Delivery** (1: Longgar >12 wks, 3: Standar 6-12 wks, 5: Cepat <6 wks)
* **D4 — Orientasi Hasil** (1: Transfer konseptual, 3: Tugas kerja spesifik, 5: Perubahan perilaku terukur)
* **D5 — Konteks Governance** (1: Startup/tim mandiri, 3: Korporat menengah, 5: Regulasi & audit ketat)

### Aturan Keputusan:
* **Selisih Skor > 20 Poin**: Gunakan single model (#1 ranked), **Confidence: High**.
* **Selisih Skor <= 20 Poin**: Rakit kombinasi dinamis melalui 4-layer M-IDA, **Confidence: Medium**.
* **User Override**: Pilihan eksplisit user selalu diutamakan, disertai catatan diagnostik trade-off.

---

## 4. Standar "Industry-Ready" Deliverables

1. **Larangan Keras "Placeholder Jargon"**: Lengkap dengan durasi menit-demi-menit, skrip verbatim fasilitator/audio, dan langkah konkret tanpa instruksi abstrak.
2. **Detail Kontekstual & `[ASUMSI]`**: Skala WBS dan timeline disesuaikan dengan durasi proyek riil; tandai asumsi yang belum dikonfirmasi stakeholder.
3. **Project-Specific Definition of Done (DoD)**: Kriteria konkret kapan dokumen dianggap tuntas dan siap dieksekusi di lapangan.
4. **Uji "Bisa Dipakai Besok Pagi"**: Jika dicetak pukul 08.00 pagi besok, fasilitator atau developer bisa langsung jalan tanpa kebingungan instruksional.
