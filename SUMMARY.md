## Goal
Build Week 4 and Week 5 DBMS book content using the newly provided notes, matching with the YouTube playlist, adding code and images where needed.

## Constraints & Preferences
- Use the notes from `Private & Shared` (Week 4) and `Private & Shared 2` (Week 5) as primary resources, then match with the YouTube playlist.
- Add code and images wherever necessary.
- Use the established writing skill and style from prior weeks.
- Follow IITM B.Sc. DBMS course content (BSCS2001).
- Font stack: Spectral (body), Cormorant Garamond (headings italic 700), DM Mono (code).
- Auto-deploy via GitHub Actions on push to `main`.
- Content must match slide content exactly; no uncovered frameworks like Django/SQLAlchemy.
- Remove images that are purely decorative title/outline/recap slides without relevant content.

## Progress
### Done
- Weeks 6–12 fully written (10 module files each), all slide images verified, merged into `main` and deployed.
- Font changed from EB Garamond to Spectral / Cormorant Garamond / DM Mono.
- `.gitignore`, `.github/workflows/deploy.yml`, AGENTS.md managed.
- Stale branches `week-06` through `week-12` deleted locally and on remote.
- Build artifacts cleaned; `_book/` and `cover.png` added to `.gitignore`.
- Week 2 table fix committed `692bad4` to `main`.
- Week 2 LA HTML assignment created (5 files + zip).
- Substack saved articles extracted from Gemini in-browser into `~/Downloads/saved_articles.md`.
- **~31 broken URLs corrected** in `saved_articles.md` across 8 hallucinated publication domains.

### In Progress
- Building Week 4 and Week 5 book content from newly provided notes:
  - **Week 4** (`Private & Shared/WEEK 4...md`, 306 lines): Relational Algebra (selection, projection, union, difference, intersection, division, cartesian product, rename), Relational Calculus (tuple & domain), Predicate Logic, ER Model (entities, attributes, relationships, weak/strong entities, cardinality, ternary relationships).
  - **Week 5** (`Private & Shared 2/Week 5...md`, 496 lines): Good DB Design, Redundancy & Anomaly, Functional Dependencies, Armstrong Axioms, Closure, Canonical Cover, Lossless Decomposition, Dependency Preservation, BCNF, Normal Forms, Super Key/Candidate Key. Plus 29 image files in `Week 5/` subfolder.

### Blocked
- (none)

## Key Decisions
- Shift focus from saved-articles cleanup to building Week 4 & 5 content using the new notes.

## Next Steps
- Expand `week04/4-1.qmd` and `week04/4-2.qmd` with full content from notes (currently sparse stubs).
- Create `week04/4-3.qmd`, `week04/4-4.qmd`, `week04/4-5.qmd` for remaining lectures.
- Create `week05/5-1.qmd` through `week05/5-5.qmd` with full content from Week 5 notes + 29 images.
- Cross-reference with DBMS YouTube playlist for accurate lecture matching.
- Uncomment Week 5 section in `_quarto.yml`.
- Push to `main` for auto-deployment.

## Critical Context
- Workspace root: `/Users/kvsrameshvarma/Downloads/IITM /DBMS/dbms-book-iitm/` (space after `IITM`).
- Image naming: `L{week}.{lecture}_p{page}.png` (e.g., `L8.1_p7.png`).
- GitHub Pages auto-deploys via `.github/workflows/deploy.yml` on push to `main`.
- `.gitignore` covers: `/.quarto/`, `/_site/`, `/_book/`, `.DS_Store`, `week*/transcripts/`, `**/*.quarto_ipynb`, `cover.png`.
- Week 4 has 2 sparse qmd files (4-1.qmd, 4-1.html, 4-2.qmd, 4-2.html) with no images directory.
- Week 5 has zero files, commented out in `_quarto.yml`.
- Notes source: `~/Downloads/Private & Shared/WEEK 4 31e6d28b09a680d1aa57d038bc9a0736.md`
- Notes source: `~/Downloads/Private & Shared 2/Week 5 3256d28b09a68007aa29d4cbe4c4d3af.md` + 29 images in `Week 5/` subfolder.

## Relevant Files
- `_quarto.yml`: sidebar config — all weeks 1–12 active with corrected titles (Week 5 commented out).
- `week02/2-2.qmd`: fixed broken duplicate-rows table (committed `692bad4` to main).
- `week04/`: 2 module qmd files (4-1.qmd, 4-2.qmd), no images directory.
- `week05/`: no files exist, commented out in `_quarto.yml`.
- `week06/` through `week12/`: all module `.qmd` files with detailed content, `images/` subdirectories with slide PNGs.
- `custom.scss` / `custom-dark.scss`: font stack (Spectral, Cormorant Garamond, DM Mono).
- `.github/workflows/deploy.yml`: auto-deploy to `gh-pages` on push to `main`.
- `~/Downloads/saved_articles.md`: Substack saved articles checklist with all verified URL corrections applied.
- `~/Downloads/Private & Shared/WEEK 4...md`: Week 4 source notes (Relational Algebra, Selection/Projection/Union/Set Difference/Cartesian Product/Rename/Join, Relational Calculus, ER Model).
- `~/Downloads/Private & Shared 2/Week 5...md` + `Week 5/*.png`: Week 5 source notes (Good DB Design, Redundancy/Anomaly, Functional Dependencies, Normalization, BCNF, Decomposition).
