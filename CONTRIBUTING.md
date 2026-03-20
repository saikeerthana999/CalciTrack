# Contributing to CalciTrack

Thank you for your interest in contributing to CalciTrack. This project aims to bring precision cardiovascular risk detection to South Asian communities, and we welcome contributions from clinicians, data scientists, and developers.

---

## Ways to Contribute

### Clinical Contributions
- **Algorithm review** — Validate or suggest improvements to the South Asian risk adjustment model
- **Evidence updates** — Propose new evidence-based guidelines for integration
- **Clinical testing** — Share de-identified case feedback to improve risk accuracy

### Technical Contributions
- **Bug reports** — Open a GitHub Issue with a clear description and steps to reproduce
- **Feature requests** — Open an Issue tagged `enhancement`
- **Code contributions** — Fork → Branch → Pull Request (see below)

### Language Contributions
- **New language support** — Add a new language dictionary to `translations.py`
- **Translation corrections** — Improve Hindi, Telugu, or Tamil translations for medical accuracy

---

## Development Setup

```bash
# Clone the repository
git clone https://github.com/saikeerthana999/CalciTrack.git
cd CalciTrack

# Install dependencies
pip install streamlit pandas fpdf

# Run the application
streamlit run app.py --server.port 5000
```

---

## Pull Request Guidelines

1. Fork the repository and create a branch: `git checkout -b feature/your-feature-name`
2. Make your changes with clear, descriptive commits
3. Ensure the app runs without errors: `streamlit run app.py`
4. Submit a Pull Request with:
   - A clear description of what changed and why
   - Any relevant clinical references if modifying the risk engine
   - Screenshots if changing the UI

---

## Code Style

- Follow PEP 8 for Python code
- Keep clinical logic in clearly named functions with docstrings
- Add a comment citing the guideline/study when changing any risk scoring logic

---

## Reporting Clinical Concerns

If you identify a potential clinical accuracy issue, please open a GitHub Issue tagged `clinical-review` and describe the concern clearly. Do not open a generic bug report for clinical logic questions.

---

## Contact

**Sai Keerthana Cherukuri**
MS4 Clinical Innovation Project
GitHub: [@saikeerthana999](https://github.com/saikeerthana999)
