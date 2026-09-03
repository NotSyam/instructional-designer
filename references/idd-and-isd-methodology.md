# Instructional Design Document (IDD) & ISD Methodology Reference

> **Version**: 3.2.0 | **Domain**: Curriculum Architecture, L&D Enterprise Documentation, & Project Governance

---

## 1. The L&D Documentation Hierarchy

An **Instructional Design Document (IDD)** serves as the master architectural contract between the Instructional Designer, Stakeholders, SMEs, and Developers before media production or storyboarding begins.

```
+----------------------------------------------------------------------------------------+
|                        HIERARKI DOKUMENTASI INSTRUCTIONAL DESIGN                       |
+----------------------------------------------------------------------------------------+
| 1. Needs Analysis Report   -> Diagnosis: kesenjangan performa, akar masalah, audiens   |
| 2. INSTRUCTIONAL DESIGN    -> ARSITEKTUR MAKRO: Kontrak strategi, scoring framework,   |
|    DOCUMENT (IDD)             LMS, WCAG, kriteria evaluasi, DoD, dan RACI sign-off     |
| 3. ISD Project Plan (WBS)  -> MANAJEMEN PROYEK: Timeline kontekstual & review SLA      |
| 4. Course Blueprint        -> MATRIKS KURIKULUM: Modul, objektif, aktivitas, asesmen   |
| 5. Storyboard / Script     -> DETAIL MIKRO: Teks per layar, instruksi visual, tombol   |
| 6. Facilitator/Learner Doc -> MATERI DELIVERABLE: Panduan fasilitator, buku peserta     |
| 7. Evaluation Report       -> EVALUASI DAMPAK: Analisis data Kirkpatrick L1 - L4       |
+----------------------------------------------------------------------------------------+
```

---

## 2. Weighted Scoring Engine & Framework Selection

Real-world training initiatives rarely fit into neat, mutually exclusive boxes. Proyek compliance sering membutuhkan perubahan perilaku nyata di lapangan, sementara proyek kepemimpinan sering butuh tata kelola korporat yang formal.

### 2.1 Lima Dimensi Penilaian Proyek (Skala 1–5)

Setiap proyek instructional design dievaluasi pada 5 dimensi berikut:

| Dimensi | Skor 1 (Rendah) | Skor 3 (Sedang) | Skor 5 (Tinggi) |
|---|---|---|---|
| **D1 — Stakes / Risiko Kegagalan** | Konsekuensi minor jika learner gagal (orientasi, awareness) | Berdampak ke kinerja tim/departemen (sales, CS) | Zero-tolerance (keselamatan fisik, hukum, klinis, audit finansial) |
| **D2 — Kompleksitas Skill** | Recall fakta, terminologi, atau prosedur sederhana | Prosedur multi-langkah dengan pertimbangan situasional | Cognitive skill kompleks, heuristik, variabel saling terkait |
| **D3 — Tekanan Waktu / Delivery** | Timeline longgar (>12 minggu), iterasi bebas | Standar korporat (6–12 minggu) | Sangat cepat (<6 minggu) atau butuh rilis prototipe bertahap |
| **D4 — Orientasi Hasil** | Transfer pemahaman konseptual jangka panjang | Penyelesaian tugas kerja prosedural spesifik | Perubahan perilaku terukur langsung di lapangan |
| **D5 — Konteks Governance** | Tim mandiri, startup, approval minimal | Korporat menengah, review berkala dengan SME | Regulasi ketat, audit eksternal, multi-stakeholder formal sign-off |

### 2.2 Profil Kecocokan Framework per Dimensi

Setiap framework memiliki profil afinitas terhadap skor di tiap dimensi:

| Framework | D1 Stakes | D2 Kompleksitas | D3 Waktu / Delivery | D4 Orientasi Hasil | D5 Governance |
|---|---|---|---|---|---|
| **ADDIE Classic** | Cocok stakes sedang–tinggi | Cocok semua level | Cocok timeline longgar | Cocok transfer & tugas | Cocok governance ketat |
| **SAM (Allen)** | Cocok stakes rendah–sedang | Cocok sedang | **Sangat cocok** timeline cepat/iteratif | Cocok tugas kerja | Kurang cocok governance sangat ketat |
| **Dick & Carey** | **Sangat cocok** stakes tinggi | Cocok kompleksitas tinggi (prosedural) | Cocok timeline longgar | Cocok tugas presisi | **Sangat cocok** governance ketat/regulasi |
| **Action Mapping (Moore)**| Cocok stakes sedang | Cocok sedang | Cocok cepat–sedang | **Sangat cocok** perubahan perilaku | Kurang cocok governance sangat ketat |
| **Backward Design (UbD)** | Cocok stakes rendah–sedang | Cocok kompleksitas konseptual | Cocok timeline longgar | **Sangat cocok** transfer konseptual | Cocok akademik/edukasi formal |
| **4C/ID** | Cocok stakes sedang–tinggi | **Sangat cocok** kompleksitas tinggi | Cocok timeline longgar | Cocok tugas kompleks | Cocok governance sedang–ketat |

### 2.3 Logika Engine & Aturan Ambang Batas 20 Poin

1. **Penilaian Awal**: Agent menilai proyek pada kelima dimensi (D1–D5) berdasarkan input user. Jika informasi belum lengkap, gunakan estimasi default yang masuk akal dan tandai secara transparan.
2. **Kalkulasi Skor Kecocokan**: Hitung skor kecocokan masing-masing framework (skala 0–100).
3. **Urutkan Peringkat**: Urutkan framework dari skor tertinggi (#1, #2, dst.).
4. **Aturan Single Framework (Selisih > 20 Poin)**:
   - Jika selisih skor antara peringkat #1 dan peringkat #2 **lebih dari 20 poin**, gunakan framework peringkat #1 secara tunggal.
   - Status kepercayaan: **Confidence: High**.
5. **Aturan Hybrid Mandatori (Selisih ≤ 20 Poin)**:
   - Jika selisih skor antara peringkat #1 dan #2 **20 poin atau kurang**, ini merupakan indikator kuat bahwa proyek bersifat lintas domain (mis. kepatuhan berisiko tinggi namun berorientasi perubahan perilaku).
   - Agent **wajib** merekomendasikan salah satu arsitektur hybrid resmi (lihat Bagian 3), bukan memaksakan satu model.
   - Status kepercayaan: **Confidence: Medium**.
6. **User Override**:
   - Jika user secara eksplisit meminta framework tertentu (mis. *"gunakan SAM"*), pilihan user selalu diutamakan. Agent mencatat skor diagnostik dan memberikan catatan trade-off singkat (mis. *"Kamu memilih SAM, namun karena D1=5 (safety-critical), kami merekomendasikan penambahan quality gate ala Dick & Carey pada tahap validasi prototipe"*).
7. **Standar Output Diagnostik Transparan**:
   Setiap rekomendasi model wajib menampilkan tabel diagnostik:
   ```
   Framework Terpilih: [Framework Tunggal atau Hybrid Pola X]
   Confidence: [High / Medium / Low]

   | Dimensi | Skor (1-5) | Justifikasi Kontekstual |
   |---|:---:|---|
   | D1 Stakes / Risiko | [X]/5 | [Alasan ringkas] |
   | D2 Kompleksitas | [X]/5 | [Alasan ringkas] |
   | D3 Waktu / Delivery | [X]/5 | [Alasan ringkas] |
   | D4 Orientasi Hasil | [X]/5 | [Alasan ringkas] |
   | D5 Governance | [X]/5 | [Alasan ringkas] |

   Rasional Pemilihan: [Penjelasan kenapa kombinasi/framework ini paling efektif]
   User Override: [Catatan bahwa user dapat mengubah atau memilih model murni kapan saja]
   ```

---

## 3. Arsitektur Hybrid Resmi

Pola kombinasi harus terstruktur dan teruji, bukan pencampuran ad-hoc tanpa dasar:

| Pola | Kombinasi | Kapan Dipakai | Pembagian Peran Kerja |
|---|---|---|---|
| **Pola A — Behavioral Agile** | Action Mapping + SAM | Training perilaku dengan timeline ketat (<6 minggu) | **Action Mapping** menentukan *apa* yang harus dilatih (analisis gap perilaku, skenario keputusan) -> **SAM** mengatur *bagaimana* proses build-nya (Savvy Start, sprint Alpha/Beta/Gold bersama SME). |
| **Pola B — Technical Rigor & Transfer** | Dick & Carey + Action Mapping | Compliance / teknis yang butuh perubahan perilaku nyata (bukan sekadar hafalan aturan) | **Dick & Carey** untuk analisis hierarki tugas, pemetaan subordinate skills, dan tes berbasis kriteria -> **Action Mapping** untuk desain skenario latihan bercabang dengan konsekuensi nyata di lapangan. |
| **Pola C — Academic Enterprise** | UbD + ADDIE | Program pendidikan formal skala besar (universitas korporat, akademi kepemimpinan) | **UbD** untuk desain pemahaman mendalam (Stage 1 Desired Results, Stage 2 GRASPS authentic assessment, Stage 3 WHERETO) -> **ADDIE** untuk tata kelola budgeting makro, manajemen logistik, dan evaluasi operasional lintas angkatan. |
| **Pola D — Complex Systems** | 4C/ID + SAM | Skill kompleks (software architecture, cyber incident, technical troubleshooting) dengan rilis bertahap | **4C/ID** untuk struktur Whole Learning Tasks, Supportive Information, dan Procedural Job Aids -> **SAM** untuk rilis prototipe fungsional bertahap per modul. |

> **Prinsip Penting**: Hybrid **bukan default otomatis**. Jika proyek murni satu karakteristik (mis. kursus online pendek non-kritis dengan selisih skor > 20 poin), gunakan framework murni. Jangan memaksakan hybrid demi terlihat rumit.

---

## 4. Standar "Industry-Ready" Deliverables

Setiap output yang dihasilkan oleh skill ini harus berstandar operasional industri nyata:

### 4.1 Larangan Keras "Placeholder Jargon"
Output tidak boleh berhenti pada label teoritis atau instruksi abstrak.
- ❌ **Dilarang:** *"Gunakan Gagné's Nine Events untuk sesi ini."* atau *"Lakukan icebreaking selama 10 menit."*
- ✅ **Wajib:** *"Menit 00–05: Buka slide dengan studi kasus insiden downtime Q2 yang menelan biaya Rp 240 juta (Gain Attention) -> Menit 05–08: Bacakan sasaran pembelajaran: 'Peserta mampu mengisolasi kebocoran memori dalam 15 menit menggunakan profiler X' (State Objective) -> ..."* — lengkap dengan alokasi waktu menit-demi-menit, skrip fasilitator yang siap dibacakan langsung, dan instruksi transisi.

### 4.2 Angka dan Detail Harus Kontekstual (Bukan Template Generik)
- Timeline dan WBS harus menyesuaikan skala program yang diminta user. Dilarang memaksakan jadwal "16-Week WBS" jika training yang diminta hanya berupa workshop 90 menit atau microlearning 5 menit.
- Jika user tidak memberikan rincian tertentu (misalnya anggaran, platform LMS, atau rasio fasilitator), tandai secara eksplisit: `[ASUMSI: LMS belum ditentukan; dirancang kompatibel SCORM 1.2 / Moodle]`. Jangan mengarang data operasional seolah-olah itu fakta yang disetujui stakeholder.

### 4.3 Setiap Deliverable Wajib Memiliki "Definition of Done" (DoD)
Setiap dokumen harus menutup dengan kriteria spesifik kapan deliverable tersebut dianggap siap pakai:
```markdown
### Project Definition of Done (DoD)
- [ ] Sasaran pembelajaran disetujui tertulis oleh Business Sponsor & Head of L&D.
- [ ] Skenario keputusan dan konsekuensi divalidasi keakuratannya oleh SME Compliance.
- [ ] Seluruh skrip fasilitator telah lolos simulasi dry-run tanpa kebingungan instruksional.
- [ ] Aset visual dan handout memenuhi uji aksesibilitas kontras WCAG 2.2 AA.
```

### 4.4 Larangan Generalisasi Tanpa Rujukan
Dilarang mencantumkan statistik efektivitas tanpa nama peneliti dan tahun publikasi resmi (mis. dilarang menulis *"Penelitian membuktikan microlearning meningkatkan retensi 20%"* tanpa dasar ilmiah). Jika tidak ada rujukan empiris spesifik, gunakan prinsip kognitif kualitatif (mis. *"Mengurangi beban kognitif ekstraneus dengan teknik chunking"*).

### 4.5 Uji "Bisa Dipakai Besok Pagi" (Ready-to-Deploy Test)
Sebelum dokumen diserahkan, lakukan verifikasi:
*"Jika dokumen ini dicetak dan diserahkan ke fasilitator atau developer besok pagi pukul 08.00, apakah mereka bisa langsung mengeksekusi tanpa perlu bertanya klarifikasi lagi?"* Jika masih terdapat tanda kurung siku kosong `[isi di sini]` atau instruksi menggantung, deliverable belum selesai.
