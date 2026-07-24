import os

workspace_dir = r"c:\Users\LENOVO\Downloads\New folder\tracevia-static"

# List of all files to modify
html_files = [
    os.path.join(workspace_dir, "index.html"),
    os.path.join(workspace_dir, "about.html"),
    os.path.join(workspace_dir, "services.html"),
    os.path.join(workspace_dir, "contact.html")
]

services_dir = os.path.join(workspace_dir, "services")
if os.path.exists(services_dir):
    for f in os.listdir(services_dir):
        if f.endswith(".html"):
            html_files.append(os.path.join(services_dir, f))

# Part 1: Update styles.css with mobile accordion rules
css_path = os.path.join(workspace_dir, "css", "styles.css")
target_css = """  .nav-dropdown-menu {
    position: static !important;
    transform: none !important;
    opacity: 1 !important;
    visibility: visible !important;
    pointer-events: auto !important;
    box-shadow: none !important;
    border: none !important;
    background: transparent !important;
    width: 100% !important;
    padding: 0 !important;
    margin-top: 8px !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 4px !important;
  }

  .nav-dropdown-menu a {
    justify-content: center !important;
    padding: 10px 16px !important;
  }

  .dropdown-trigger i {
    transform: rotate(0deg) !important;
  }"""

replacement_css = """  .nav-dropdown-menu {
    display: none !important; /* Hidden on mobile by default */
    position: static !important;
    transform: none !important;
    opacity: 1 !important;
    visibility: visible !important;
    pointer-events: auto !important;
    box-shadow: none !important;
    border: none !important;
    background: transparent !important;
    width: 100% !important;
    padding: 0 !important;
    margin-top: 8px !important;
  }
  
  .nav-item-dropdown.mobile-dropdown-active .nav-dropdown-menu {
    display: flex !important;
    flex-direction: column !important;
    gap: 4px !important;
  }

  .nav-dropdown-menu a {
    justify-content: center !important;
    padding: 10px 16px !important;
  }

  .dropdown-trigger i {
    transition: transform 0.3s ease !important;
  }"""

if os.path.exists(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    if target_css in css_content:
        css_content = css_content.replace(target_css, replacement_css)
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(css_content)
        print("Updated styles.css with mobile accordion classes.")
    else:
        # Fallback if whitespace differs
        print("Target CSS block not matched exactly. Performing fuzzy replacement...")
        css_content = css_content.replace(".nav-dropdown-menu {", ".nav-dropdown-menu-old {", 1) # temp
        # Let's write the stylesheet change programmatically
        # Actually, let's just do a string replacement of the specific block
        start_idx = css_content.find("  .nav-dropdown-menu {")
        end_idx = css_content.find("  .glass-header.scrolled nav.nav-links a:not(.btn)")
        if start_idx != -1 and end_idx != -1:
            css_content = css_content[:start_idx] + replacement_css + "\n\n" + css_content[end_idx:]
            with open(css_path, 'w', encoding='utf-8') as f:
                f.write(css_content)
            print("Completed fuzzy CSS replacement.")
        else:
            print("CSS block not found.")


# Part 2: Update main.js with mobile dropdown logic
js_path = os.path.join(workspace_dir, "js", "main.js")
target_js = """  } else {
    revealElements.forEach(el => el.classList.add('revealed'));
  }
});"""

replacement_js = """  } else {
    revealElements.forEach(el => el.classList.add('revealed'));
  }

  // 6. Mobile Dropdown Toggle for accordion menu
  const dropdownTrigger = document.querySelector('.dropdown-trigger');
  const navDropdown = document.querySelector('.nav-item-dropdown');
  const chevronIcon = dropdownTrigger ? dropdownTrigger.querySelector('.bx-chevron-down') : null;
  
  if (dropdownTrigger && navDropdown) {
    dropdownTrigger.addEventListener('click', (e) => {
      // Toggle dropdown on mobile viewports
      if (window.innerWidth < 768) {
        e.preventDefault();
        e.stopPropagation();
        
        navDropdown.classList.toggle('mobile-dropdown-active');
        
        // Rotate chevron icon
        if (chevronIcon) {
          if (navDropdown.classList.contains('mobile-dropdown-active')) {
            chevronIcon.style.transform = 'rotate(180deg)';
          } else {
            chevronIcon.style.transform = 'rotate(0deg)';
          }
        }
      }
    });
  }
});"""

if os.path.exists(js_path):
    with open(js_path, 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    if target_js in js_content:
        js_content = js_content.replace(target_js, replacement_js)
        with open(js_path, 'w', encoding='utf-8') as f:
            f.write(js_content)
        print("Updated main.js with dropdown trigger event listener.")
    else:
        # Fuzzy replacement if needed
        last_brace = js_content.rfind("});")
        if last_brace != -1:
            # We can insert before the last brace
            js_content = js_content[:last_brace] + """
  // 6. Mobile Dropdown Toggle for accordion menu
  const dropdownTrigger = document.querySelector('.dropdown-trigger');
  const navDropdown = document.querySelector('.nav-item-dropdown');
  const chevronIcon = dropdownTrigger ? dropdownTrigger.querySelector('.bx-chevron-down') : null;
  
  if (dropdownTrigger && navDropdown) {
    dropdownTrigger.addEventListener('click', (e) => {
      // Toggle dropdown on mobile viewports
      if (window.innerWidth < 768) {
        e.preventDefault();
        e.stopPropagation();
        
        navDropdown.classList.toggle('mobile-dropdown-active');
        
        // Rotate chevron icon
        if (chevronIcon) {
          if (navDropdown.classList.contains('mobile-dropdown-active')) {
            chevronIcon.style.transform = 'rotate(180deg)';
          } else {
            chevronIcon.style.transform = 'rotate(0deg)';
          }
        }
      }
    });
  }
""" + js_content[last_brace:]
            with open(js_path, 'w', encoding='utf-8') as f:
                f.write(js_content)
            print("Completed fuzzy JS replacement.")
        else:
            print("JS block not found.")


# Part 3: Update HTML files with cache buster v=1.0.8
print("Setting cache buster to ?v=1.0.8 across HTML files...")
for filepath in html_files:
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = content.replace("styles.css?v=1.0.7", "styles.css?v=1.0.8")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated cache buster on page: {os.path.basename(filepath)}")

print("Navbar mobile accordion adjustments complete!")
