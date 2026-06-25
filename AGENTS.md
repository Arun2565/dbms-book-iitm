# DBMS Notes Workflow

Repeat this process for each remaining week (7–12). Based on patterns from Week 6.

---

## Prerequisites

- Python packages: `youtube_transcript_api`, `PyMuPDF` (fitz)
- Quarto CLI installed
- PDFs for the week in `../DBMS PPTs/Week N/`
- YouTube video IDs for the week's lectures

---

## Step 1: Create branch and directory

```bash
git checkout week-NN   # or git checkout -b week-NN
mkdir -p weekNN/images weekNN/transcripts
```

---

## Step 2: Download transcripts

Use `youtube_transcript_api` for each lecture video.

Video IDs are found in the course playlist. For each lecture, download the transcript:

```python
from youtube_transcript_api import YouTubeTranscriptApi
text = YouTubeTranscriptApi.get_transcript(VIDEO_ID)
# write formatted text to weekNN/transcripts/L{num}.txt
```

---

## Step 3: Extract slide images from PDFs

Use PyMuPDF (fitz) to render each lecture PDF to PNG at 144 DPI.

```python
import fitz
doc = fitz.open("path/to/Lecture N.pdf")
for pg in range(len(doc)):
    page = doc[pg]
    pix = page.get_pixmap(matrix=fitz.Matrix(144/72, 144/72))
    pix.save(f"weekNN/images/L{N}.p{pg+1}.png")
```

Files: `weekNN/images/L{N}.p{pg}.png`

---

## Step 4: Write module files

Create `weekNN/N-{module}.qmd` for each lecture.

**Rules:**
- Read the transcript to understand the lecture flow
- Reference slide images by `images/L{N}.p{pg}.png`
- DO NOT use Mermaid diagrams — use slide images instead
- Keep ordered lists on separate lines (each item on its own line)
- Use plain-writing style: concise, direct, no commentary or filler
- Match the tone and structure of existing week 6 files

**Image naming convention:**
- PDF page renders: `L{N}.p{pg}.png` (e.g. `L7.1_p12.png`)
- Images are referenced as: `images/L7.1_p12.png`

**Module template:**
```yaml
---
title: "N.N Topic title"
---

Content written here with `images/L{N}.p{pg}.png` references embedded.

```

---

## Step 5: Update sidebar

Edit `_quarto.yml` to add the week to the sidebar:

```yaml
      - section: "Week N: Topic Name"
        contents:
          - text: "N.1 Topic"
            href: weekNN/N-1.qmd
          - text: "N.2 Topic"
            href: weekNN/N-2.qmd
          ...
```

---

## Step 6: Verify

Check all image references point to existing files:

```bash
for f in weekNN/N-*.qmd; do
  grep -o 'images/L[^)]*' "$f" | while read -r img; do
    [ -f "weekNN/$img" ] || echo "MISSING: $img"
  done
done
```

---

## Step 7: Commit and deploy

```bash
git add _quarto.yml weekNN/
git commit -m "Add week N: Topic name"
git push origin week-NN
```

Create a PR on GitHub, merge to `main`. The GitHub Actions workflow auto-deploys to `gh-pages`.

---

## Reference: Week 6 structure

| Module | Topic | Lectures |
|--------|-------|----------|
| 6-1    | Normal Forms (1NF, 2NF, 3NF) | L31 |
| 6-2    | Decomposition Algorithms | L32 |
| 6-3    | LIS Case Study | L33 |
| 6-4    | MVD & 4NF | L34 |
| 6-5    | Design Process & Temporal Data | L35 |

**Font stack:** `Spectral` (body), `Cormorant Garamond` (headings, italic 700), `DM Mono` (code).

**Available PPTs:** Weeks 1–12 in `../DBMS PPTs/`.
