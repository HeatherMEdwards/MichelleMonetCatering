# Fix #7, #26, #18, #20, #21: Padding, copy, and menu text

## Summary
Single PR fulfilling five issues: padding/spacing, Por Qué Elegirnos content, and service-list copy for Entradas, Postres, and Panes artesanales.

---

### #7 — Revisit padding on subsections
- **Section spacing:** `.section` margin `2rem` → `1rem`; `.section-title` margin-bottom `1.5rem` → `1rem`
- **Welcome block:** padding `2rem 1rem` → `1.25rem 1rem`, margin `1rem` → `0.75rem`; section-head margin-bottom reduced
- **Welcome text:** line-height `1.75` → `1.5`, bottom margin reduced
- **CTA:** padding `3rem 1rem` → `1.75rem 1rem`, margin `2rem` → `1rem`
- **Por Qué Elegirnos:** line-height `2` → `1.6`; added `.elegirnos-list li` spacing

---

### #26 — Por Qué Elegirnos
- Replaced long paragraph with 5-item list:
  - Ingredientes de primera calidad
  - Recetas auténticas tradicionales
  - Presentación
  - Puntualidad
  - Atención personalizada
- Removed: “francesas y mexicanas”, “elegante y profesional”, “garantizada”, “para cada evento”, “Servicio en Guadalajara, Zapopan, y alrededores”
- Fixed typo: puntalidad → Puntualidad

---

### #18 — Entradas
- Service list text: **Humus, humus de betabel, dips (en español), tartas saladas, y sopas.**

---

### #20 — Postres
- Service list text: **Pasteles, tartas, galletas, y brownies.**

---

### #21 — Panes artesanales
- Removed baguettes and “especialidades de panadería”
- New text: **Pan recién horneado de masa madre y especialidades saladas y dulces.**

---

## Testing
- [ ] Sections look less cramped; spacing feels balanced
- [ ] Por Qué Elegirnos shows as a clean bullet list
- [ ] Entradas, Postres, and Panes artesanales show updated copy

Closes #7, Closes #26, Closes #18, Closes #20, Closes #21
