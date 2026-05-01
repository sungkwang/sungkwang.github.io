# Sungkwang Mun's Academic Website

This website is built with Jekyll and hosted on GitHub Pages. It uses collections to manage publications, software, and research themes dynamically.

## 🛠️ How to Update Content

### 1. Adding a New Publication
To add a paper, poster, or presentation:
1. Create a new `.md` file in `_publications/`. (Pattern: `YYYY-BibID.md`)
2. Fill in the YAML frontmatter:
   ```yaml
   ---
   layout: publication
   bibtex_id: Mun2024         # Unique ID for the BibTeX toggle
   category: "Journal Articles" # or "Conference Papers", "Software Manuals", etc.
   year: 2024
   doi: "10.1088/..."         # Optional
   pdf: "pub/YourFile.pdf"    # Optional: Path to file in /pub folder
   theme: "MEAM"              # Linking keyword for the Research page
   bibtex: |                  # BibTeX entry (indented)
     @article{...}
   ---
   ```
3. Add the formatted HTML citation in the `<div class="pub-entry">` block.

### 2. Updating Research Themes
The **Research** page automatically pulls the latest 3 publications for each theme.
*   To change which papers appear, update the `theme` field in the publication's frontmatter.
*   **Current Themes** (case-sensitive):
    *   `compressed sensing`
    *   `MEAM`
    *   `ballistics`
    *   `ML in combustion`
    *   `Advanced Manufacturing`
    *   `Advanced Maintenance`

### 3. Adding Software Tools
1. Create a new `.md` file in `_software/`.
2. Fill in the YAML frontmatter:
   ```yaml
   ---
   name: "ToolName"
   description: "Short tagline."
   github: "https://github.com/..." # or use 'website' for project pages
   priority: 1                     # Lower numbers appear first
   ---
   Full description and features go here.
   ```

### 4. Student Mentoring
Update the list directly in `research.html` under the `<ul class="group-list">` section. Use the `.student-header` class to maintain the dense layout.

## 📁 Directory Structure
*   `_publications/`: Source files for all papers.
*   `_software/`: Source files for software tools.
*   `pub/`: Storage for PDFs, posters, and presentation slides.
*   `img/`: Storage for images and figures.

## 🚀 Deployment
Any changes pushed to the `master` branch will automatically trigger a build and deploy on GitHub Pages.
