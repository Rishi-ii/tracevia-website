import os

workspace_dir = r"c:\Users\LENOVO\Downloads\New folder\tracevia-static"

# List of root pages
root_pages = ["index.html", "about.html", "services.html", "contact.html"]

# List of service subpages
subpages = [
    "motor-property.html",
    "accident-reconstruction.html",
    "document-examination.html",
    "fingerprint-analysis.html",
    "audio-video.html",
    "forensic-accounting.html",
    "crime-scene.html",
    "forensic-education.html"
]

print("Splitting the Services dropdown label and trigger icon across 12 templates...")

# 1. Update CSS styles.css dropdown chevron selector
css_path = os.path.join(workspace_dir, "css", "styles.css")
if os.path.exists(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()
    
    # Replace selector
    css = css.replace(".dropdown-trigger i {", ".dropdown-trigger-icon i {")
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated styles.css chevron CSS transition selector.")

# 2. Update js/main.js mobile dropdown click listener
js_path = os.path.join(workspace_dir, "js", "main.js")
new_js_logic = """  // 6. Mobile Dropdown Toggle for accordion menu
  const dropdownTriggerIcons = document.querySelectorAll('.dropdown-trigger-icon');
  
  dropdownTriggerIcons.forEach(trigger => {
    const parentDropdown = trigger.closest('.nav-dropdown-wrapper');
    const chevronIcon = trigger.querySelector('.bx-chevron-down, .dropdown-arrow');
    
    if (parentDropdown && trigger) {
      trigger.addEventListener('click', (e) => {
        if (window.innerWidth < 768) {
          e.preventDefault();
          e.stopPropagation();
          
          parentDropdown.classList.toggle('mobile-dropdown-active');
          
          // Rotate chevron icon
          if (chevronIcon) {
            if (parentDropdown.classList.contains('mobile-dropdown-active')) {
              chevronIcon.style.transform = 'rotate(180deg)';
            } else {
              chevronIcon.style.transform = 'rotate(0deg)';
            }
          }
        }
      });
    }
  });
});"""

if os.path.exists(js_path):
    with open(js_path, 'r', encoding='utf-8') as f:
        js = f.read()
        
    # Locate the start of "// 6. Mobile Dropdown Toggle"
    start_pos = js.find("  // 6. Mobile Dropdown Toggle")
    if start_pos != -1:
        js = js[:start_pos] + new_js_logic
        with open(js_path, 'w', encoding='utf-8') as f:
            f.write(js)
        print("Updated main.js with trigger-icon click listeners.")
    else:
        print("Could not find mobile dropdown section in main.js. Appending at the end.")
        last_brace = js.rfind("});")
        if last_brace != -1:
            js = js[:last_brace] + new_js_logic + "\n"
            with open(js_path, 'w', encoding='utf-8') as f:
                f.write(js)
            print("Appended dropdown listeners to main.js.")

# 3. Update root pages HTML
for filename in root_pages:
    filepath = os.path.join(workspace_dir, filename)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Perform specific replacement based on whether it is services.html (active) or others (inactive)
    if filename == "services.html":
        # Services active
        old_block = """        <!-- Services Dropdown -->
        <div class="nav-dropdown-wrapper relative">
          <a href="services.html" class="active dropdown-trigger flex items-center gap-1 font-outfit text-base font-semibold text-navy-medium hover:text-navy-deep no-underline transition-all cursor-pointer">
            Services <i class='bx bx-chevron-down dropdown-arrow text-sm transition-all duration-200'></i>
          </a>"""
        new_block = """        <!-- Services Dropdown -->
        <div class="nav-dropdown-wrapper relative flex items-center gap-1 md:flex-row flex-row">
          <a href="services.html" class="active font-outfit text-base font-semibold text-navy-medium hover:text-navy-deep no-underline transition-all cursor-pointer">Services</a>
          <button class="dropdown-trigger-icon bg-transparent border-none cursor-pointer p-0 text-navy-medium hover:text-navy-deep transition-all flex items-center justify-center" aria-label="Toggle Services Menu">
            <i class='bx bx-chevron-down dropdown-arrow text-sm transition-all duration-200'></i>
          </button>"""
    else:
        # Services inactive
        old_block = """        <!-- Services Dropdown -->
        <div class="nav-dropdown-wrapper relative">
          <a href="services.html" class="dropdown-trigger flex items-center gap-1 font-outfit text-base font-semibold text-text-medium hover:text-navy-deep no-underline transition-all cursor-pointer">
            Services <i class='bx bx-chevron-down dropdown-arrow text-sm transition-all duration-200'></i>
          </a>"""
        new_block = """        <!-- Services Dropdown -->
        <div class="nav-dropdown-wrapper relative flex items-center gap-1 md:flex-row flex-row">
          <a href="services.html" class="font-outfit text-base font-semibold text-text-medium hover:text-navy-deep no-underline transition-all cursor-pointer">Services</a>
          <button class="dropdown-trigger-icon bg-transparent border-none cursor-pointer p-0 text-text-medium hover:text-navy-deep transition-all flex items-center justify-center" aria-label="Toggle Services Menu">
            <i class='bx bx-chevron-down dropdown-arrow text-sm transition-all duration-200'></i>
          </button>"""
          
    content = content.replace(old_block, new_block)
    
    # Increment cache buster to ?v=1.0.9
    content = content.replace("styles.css?v=1.0.8", "styles.css?v=1.0.9")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated header in root page: {filename}")

# 4. Update service subpages HTML
services_dir = os.path.join(workspace_dir, "services")
for filename in subpages:
    filepath = os.path.join(services_dir, filename)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Services active with parent relative path "../services.html"
    old_block = """        <!-- Services Dropdown -->
        <div class="nav-dropdown-wrapper relative">
          <a href="../services.html" class="active dropdown-trigger flex items-center gap-1 font-outfit text-base font-semibold text-navy-medium hover:text-navy-deep no-underline transition-all cursor-pointer">
            Services <i class='bx bx-chevron-down dropdown-arrow text-sm transition-all duration-200'></i>
          </a>"""
    new_block = """        <!-- Services Dropdown -->
        <div class="nav-dropdown-wrapper relative flex items-center gap-1 md:flex-row flex-row">
          <a href="../services.html" class="active font-outfit text-base font-semibold text-navy-medium hover:text-navy-deep no-underline transition-all cursor-pointer">Services</a>
          <button class="dropdown-trigger-icon bg-transparent border-none cursor-pointer p-0 text-navy-medium hover:text-navy-deep transition-all flex items-center justify-center" aria-label="Toggle Services Menu">
            <i class='bx bx-chevron-down dropdown-arrow text-sm transition-all duration-200'></i>
          </button>"""
          
    content = content.replace(old_block, new_block)
    
    # Increment cache buster to ?v=1.0.9
    content = content.replace("styles.css?v=1.0.8", "styles.css?v=1.0.9")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated header in subpage: {filename}")

print("Dropdown split modification completed successfully!")
