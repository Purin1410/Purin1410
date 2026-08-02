<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/hero-light.svg">
  <img alt="A handwritten integral expression transformed into its LaTeX token sequence" src="assets/hero-light.svg">
</picture>

# Khoa Nguyen

**Nguyễn Minh Khoa** · published as **Khoa Minh Nguyen**

Handwritten mathematics&nbsp; ·&nbsp; molecular text&nbsp; →&nbsp; language-grounded industrial inspection

B.Eng. Artificial Intelligence and Data Science, FPT University&nbsp; ·&nbsp; Research member, AiTA Lab

[![Papers](https://img.shields.io/badge/Papers-4_accepted-B45309?style=flat-square)](#publications)
[![Google Scholar](https://img.shields.io/badge/Google_Scholar-334155?style=flat-square&logo=googlescholar&logoColor=white)](https://scholar.google.com/citations?user=tCq7yoQAAAAJ)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-334155?style=flat-square)](https://www.linkedin.com/in/ngminhkhoa1410)
[![Email](https://img.shields.io/badge/Email-334155?style=flat-square&logo=gmail&logoColor=white)](mailto:ngminhkhoayj2706@gmail.com)

[Publications](#publications)&nbsp; ·&nbsp; [Research direction](#research-direction)&nbsp; ·&nbsp; [Toolkit](#toolkit)&nbsp; ·&nbsp; [Education](#education-and-recognition)

</div>

> [!NOTE]
> Final-year B.Eng. candidate at FPT University and research member at AiTA Lab, with four
> accepted conference papers on handwritten mathematical expression recognition and
> cross-modal representation learning. I work on problems where structured outputs, visual
> understanding, and language meet — and on the training pipelines that keep those
> experiments reproducible.

---

## Publications

<table>
<thead>
<tr>
<th width="160">Venue</th>
<th>Paper</th>
<th width="130">Role</th>
</tr>
</thead>
<tbody>

<tr>
<td valign="top"><b>APWeb-WAIM 2026</b><br><sub>accepted</sub></td>
<td valign="top"><b>LexiChem</b><br><sub>Text-to-molecule generation, evaluated on the L+M-24 benchmark. Grew out of my undergraduate capstone system.</sub></td>
<td valign="top">First author</td>
</tr>

<tr>
<td valign="top"><b>APWeb-WAIM 2026</b><br><sub>accepted</sub></td>
<td valign="top"><b>CorrTie: Correction-aware Tie-breaking for Active Learning with Vision-Language Models</b><br><sub>Acquisition strategy for active learning with VLMs. Gains of 7.14, 3.74, and 0.66 points at 1%, 2%, and 5% labelling budgets.</sub></td>
<td valign="top">Co-author</td>
</tr>

<tr>
<td valign="top"><b>ICCIES 2026</b><br><sub>CCIS 2943</sub></td>
<td valign="top"><a href="https://doi.org/10.1007/978-3-032-21625-0_16"><b>ChemAligner-T5: A Unified Text-to-Molecule Model via Representation Alignment</b></a><br><sub>Contrastive alignment of textual and molecular representations on BioT5+. 69.77% BLEU and 31.28% Levenshtein distance on L+M-24.</sub></td>
<td valign="top">Co-first author</td>
</tr>

<tr>
<td valign="top"><b>ICDAR 2025</b><br><sub>LNCS 16025</sub></td>
<td valign="top"><a href="https://doi.org/10.1007/978-3-032-04624-6_22"><b>Mask CoMER: Enhancing Handwritten Mathematical Expression Recognition with Masked Language Pretraining and Regularization</b></a><br><sub>Masked-language-model pretraining plus stochastic-depth regularization. ExpRate 64.56%, 63.03%, and 65.22% on CROHME 2014, 2016, and 2019 — up to 5 points over the CoMER baseline.</sub></td>
<td valign="top">Co-first author</td>
</tr>

</tbody>
</table>

---

## Research direction

My demonstrated work is in handwritten mathematical expression recognition and cross-modal
alignment. The direction I am developing toward is **language-grounded industrial visual
inspection**: using vision-language models to locate and explain manufacturing defects from
natural-language descriptions, with an emphasis on zero- and few-shot generalization.

The link is concrete rather than aspirational. The contrastive text-to-image alignment
behind ChemAligner-T5 is the same machinery that WinCLIP and AnomalyCLIP apply to defect
detection — the modality on one side changes, the objective does not.

*A direction in progress, not a claim of deployment or validation on real factory data.*

---

## Toolkit

<table>
<tbody>
<tr><td width="200"><b>Research</b></td><td>contrastive representation learning · self-supervised learning · preference optimization (DPO) · controlled ablation design</td></tr>
<tr><td><b>Models and training</b></td><td>PyTorch · PyTorch Lightning · Transformers · LoRA / PEFT · LLaMA-Factory</td></tr>
<tr><td><b>Engineering and data</b></td><td>Python · FastAPI · PostgreSQL / TimescaleDB · pandas · RDKit</td></tr>
<tr><td><b>Reproducibility</b></td><td>Docker · Weights &amp; Biases · MLflow · Git · Linux · LaTeX</td></tr>
</tbody>
</table>

---

## Education and recognition

**B.Eng. candidate, Artificial Intelligence and Data Science** — FPT University, expected 2026<br>
<sub>Capstone: *LexiChem*, a text-to-molecule system with 2D/3D structure visualization, RDKit property computation, and multi-model inference serving.</sub>

**Research member** — AiTA Lab, FPT University, 2024–present<br>
**Member** — AIO2024, AI Vietnam

Silver Medal, Vietnam National Open Mathematics Olympiad for High School Students (2021) · Merit Scholarship, FPT University · Innovation Project Grant, FPT University

---

## Contact

Open to conversations about HMER, multimodal learning, reproducible ML research, and
language-grounded industrial vision — [ngminhkhoayj2706@gmail.com](mailto:ngminhkhoayj2706@gmail.com).
