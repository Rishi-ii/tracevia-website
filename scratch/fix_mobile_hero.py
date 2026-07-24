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

index_path = os.path.join(workspace_dir, "index.html")

if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. Replace section height
    old_section = 'section class="slideshow-hero relative w-full h-[650px] overflow-hidden bg-navy-deep p-0 mt-20"'
    new_section = 'section class="slideshow-hero relative w-full h-[540px] sm:h-[580px] md:h-[650px] overflow-hidden bg-navy-deep p-0 mt-20"'
    content = content.replace(old_section, new_section)
    
    # 2. Update slides headings and buttons
    # Slide 1
    old_slide1_header = """            <h1 class="slide-title font-outfit text-5xl md:text-7xl font-black text-white leading-[1.1] mb-8 drop-shadow-lg tracking-tight">
              Scientific Forensic Solutions You Can Trust
            </h1>
            <div class="slide-buttons flex gap-4">
              <a href="contact.html" class="btn btn-accent btn-lg font-semibold px-7 py-3.5 bg-accent-cyan hover:bg-[#00878e] rounded-full text-white flex items-center gap-2 shadow-md transition-all">
                <i class='bx bx-file-find'></i> Request an Investigation
              </a>
              <a href="services.html" class="btn btn-light btn-lg font-semibold px-7 py-3.5 bg-white text-navy-deep hover:bg-accent-cyan hover:text-white rounded-full flex items-center gap-2 shadow-sm transition-all">
                <i class='bx bx-list-check'></i> Our Services
              </a>
            </div>"""
            
    new_slide1_header = """            <h1 class="slide-title font-outfit text-3xl sm:text-4xl md:text-6xl lg:text-7xl font-black text-white leading-[1.1] mb-8 drop-shadow-lg tracking-tight">
              Scientific Forensic Solutions You Can Trust
            </h1>
            <div class="slide-buttons flex flex-col sm:flex-row gap-4 w-full sm:w-auto">
              <a href="contact.html" class="btn btn-accent btn-lg font-semibold px-7 py-3.5 bg-accent-cyan hover:bg-[#00878e] rounded-full text-white flex items-center justify-center gap-2 shadow-md transition-all w-full sm:w-auto">
                <i class='bx bx-file-find'></i> Request an Investigation
              </a>
              <a href="services.html" class="btn btn-light btn-lg font-semibold px-7 py-3.5 bg-white text-navy-deep hover:bg-accent-cyan hover:text-white rounded-full flex items-center justify-center gap-2 shadow-sm transition-all w-full sm:w-auto">
                <i class='bx bx-list-check'></i> Our Services
              </a>
            </div>"""
            
    content = content.replace(old_slide1_header, new_slide1_header)
    
    # Slide 2
    old_slide2_header = """            <h1 class="slide-title font-outfit text-5xl md:text-7xl font-black text-white leading-[1.1] mb-8 drop-shadow-lg tracking-tight">
              From Trace to Truth
            </h1>
            <div class="slide-buttons flex gap-4">
              <a href="contact.html" class="btn btn-accent btn-lg font-semibold px-7 py-3.5 bg-accent-cyan hover:bg-[#00878e] rounded-full text-white flex items-center gap-2 shadow-md transition-all">
                <i class='bx bx-file-find'></i> Request an Investigation
              </a>
              <a href="services.html" class="btn btn-light btn-lg font-semibold px-7 py-3.5 bg-white text-navy-deep hover:bg-accent-cyan hover:text-white rounded-full flex items-center gap-2 shadow-sm transition-all">
                <i class='bx bx-list-check'></i> Our Services
              </a>
            </div>"""
            
    new_slide2_header = """            <h1 class="slide-title font-outfit text-3xl sm:text-4xl md:text-6xl lg:text-7xl font-black text-white leading-[1.1] mb-8 drop-shadow-lg tracking-tight">
              From Trace to Truth
            </h1>
            <div class="slide-buttons flex flex-col sm:flex-row gap-4 w-full sm:w-auto">
              <a href="contact.html" class="btn btn-accent btn-lg font-semibold px-7 py-3.5 bg-accent-cyan hover:bg-[#00878e] rounded-full text-white flex items-center justify-center gap-2 shadow-md transition-all w-full sm:w-auto">
                <i class='bx bx-file-find'></i> Request an Investigation
              </a>
              <a href="services.html" class="btn btn-light btn-lg font-semibold px-7 py-3.5 bg-white text-navy-deep hover:bg-accent-cyan hover:text-white rounded-full flex items-center justify-center gap-2 shadow-sm transition-all w-full sm:w-auto">
                <i class='bx bx-list-check'></i> Our Services
              </a>
            </div>"""
            
    content = content.replace(old_slide2_header, new_slide2_header)
    
    # Slide 3
    old_slide3_header = """            <h1 class="slide-title font-outfit text-5xl md:text-7xl font-black text-white leading-[1.1] mb-8 drop-shadow-lg tracking-tight">
              Where Every Trace Tells a Story
            </h1>
            <div class="slide-buttons flex gap-4">
              <a href="contact.html" class="btn btn-accent btn-lg font-semibold px-7 py-3.5 bg-accent-cyan hover:bg-[#00878e] rounded-full text-white flex items-center gap-2 shadow-md transition-all">
                <i class='bx bx-file-find'></i> Request an Investigation
              </a>
              <a href="services.html" class="btn btn-light btn-lg font-semibold px-7 py-3.5 bg-white text-navy-deep hover:bg-accent-cyan hover:text-white rounded-full flex items-center gap-2 shadow-sm transition-all">
                <i class='bx bx-list-check'></i> Our Services
              </a>
            </div>"""
            
    new_slide3_header = """            <h1 class="slide-title font-outfit text-3xl sm:text-4xl md:text-6xl lg:text-7xl font-black text-white leading-[1.1] mb-8 drop-shadow-lg tracking-tight">
              Where Every Trace Tells a Story
            </h1>
            <div class="slide-buttons flex flex-col sm:flex-row gap-4 w-full sm:w-auto">
              <a href="contact.html" class="btn btn-accent btn-lg font-semibold px-7 py-3.5 bg-accent-cyan hover:bg-[#00878e] rounded-full text-white flex items-center justify-center gap-2 shadow-md transition-all w-full sm:w-auto">
                <i class='bx bx-file-find'></i> Request an Investigation
              </a>
              <a href="services.html" class="btn btn-light btn-lg font-semibold px-7 py-3.5 bg-white text-navy-deep hover:bg-accent-cyan hover:text-white rounded-full flex items-center justify-center gap-2 shadow-sm transition-all w-full sm:w-auto">
                <i class='bx bx-list-check'></i> Our Services
              </a>
            </div>"""
            
    content = content.replace(old_slide3_header, new_slide3_header)
    
    # 3. Adjust tagline margin-bottom for mobile
    content = content.replace("rounded-full mb-6 tracking-widest shadow-sm", "rounded-full mb-4 sm:mb-6 tracking-widest shadow-sm")
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated index.html hero slideshow elements.")


# Part 2: Update HTML cache busters to ?v=1.1.1
print("Updating stylesheet cache buster tags to ?v=1.1.1 in HTML files...")
for filepath in html_files:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = content.replace("styles.css?v=1.1.0", "styles.css?v=1.1.1")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated: {os.path.basename(filepath)}")

print("Mobile hero slideshow adjustments complete!")
