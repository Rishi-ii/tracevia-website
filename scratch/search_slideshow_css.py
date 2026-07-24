import os

css_path = r"c:\Users\LENOVO\Downloads\New folder\tracevia-static\css\styles.css"
if os.path.exists(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        if "slideshow-hero" in line or "hero-slide" in line or "slide-info" in line or "slide-buttons" in line:
            print(f"Line {i+1}: {line.strip()}")
else:
    print("styles.css not found.")
