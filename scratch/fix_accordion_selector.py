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

# Part 1: Update styles.css with the correct wrapper class selector
css_path = os.path.join(workspace_dir, "css", "styles.css")
if os.path.exists(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # Replace nav-item-dropdown with nav-dropdown-wrapper
    css_content = css_content.replace(
        ".nav-item-dropdown.mobile-dropdown-active .nav-dropdown-menu",
        ".nav-dropdown-wrapper.mobile-dropdown-active .nav-dropdown-menu"
    )
    
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("Updated styles.css active selector.")

# Part 2: Update HTML cache busters to ?v=1.1.0
print("Updating stylesheet cache buster tags to ?v=1.1.0 in HTML files...")
for filepath in html_files:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = content.replace("styles.css?v=1.0.9", "styles.css?v=1.1.0")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated: {os.path.basename(filepath)}")

print("Selector correction complete!")
