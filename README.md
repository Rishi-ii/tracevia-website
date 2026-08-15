# Tracevia Forensics Company Website 🌐

A premium, database-free static website built for *Tracevia Forensics Services Private Limited*, featuring glassmorphic design and smooth UI animations.

### 🛠️ Tech Stack
*   **Frontend**: HTML5, CSS3, JavaScript, Tailwind CSS (via Play CDN), Boxicons, Google Fonts (Inter, Outfit)
*   **Hosting & Deployment**: Netlify Configuration (`netlify.toml`)

### 📂 Page Structure & Services Offered
*   `index.html`: Home page with an automated slideshow hero and core service previews.
*   `about.html`: Corporate profile and vision of the firm.
*   `services.html`: Grid of clinical/claims service offerings.
*   `contact.html`: Contact inquiries form and details.
*   **Specific Service Detailed Pages (`services/`)**:
    *   Fingerprint Analysis
    *   Questioned Document Verification
    *   Accident Reconstruction
    *   Audio/Video Authentication
    *   Crime Scene Investigation
    *   Forensic Accounting & Fraud Audits
    *   Forensic Education & Corporate Training
    *   Motor & Property Claims Investigation

### ⚙️ Server Configuration (`netlify.toml`)
Includes server-side rules for:
*   Clean URL redirects (e.g., routing `/about` to `/about.html`).
*   HTTP Security Headers: `X-Frame-Options: DENY`, `X-XSS-Protection`, and `X-Content-Type-Options: nosniff`.

### 🚀 Local Running
Open `index.html` directly in any web browser, or serve it locally using python:
```bash
python -m http.server 8000
```
