document.addEventListener('DOMContentLoaded', () => {
  // 1. Sticky Header Scroll Effect & Scroll Progress Bar
  const header = document.querySelector('.glass-header');
  const progressBar = document.querySelector('.scroll-progress-bar');
  
  window.addEventListener('scroll', () => {
    // Header background transition
    if (window.scrollY > 20) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
    
    // Progress bar width updates
    const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    if (windowHeight > 0 && progressBar) {
      const scrolledPercentage = (window.scrollY / windowHeight) * 100;
      progressBar.style.width = scrolledPercentage + '%';
    }
  });

  // 2. Mobile Menu Toggle
  const mobileToggle = document.querySelector('.mobile-toggle');
  const navLinks = document.querySelector('.nav-links');
  const mobileToggleIcon = mobileToggle ? mobileToggle.querySelector('i') : null;

  if (mobileToggle && navLinks) {
    mobileToggle.addEventListener('click', () => {
      navLinks.classList.toggle('mobile-open');
      if (mobileToggleIcon) {
        if (navLinks.classList.contains('mobile-open')) {
          mobileToggleIcon.classList.remove('bx-menu');
          mobileToggleIcon.classList.add('bx-x');
        } else {
          mobileToggleIcon.classList.remove('bx-x');
          mobileToggleIcon.classList.add('bx-menu');
        }
      }
    });

    // Close mobile menu on clicking any navigation link
    const links = navLinks.querySelectorAll('a');
    links.forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('mobile-open');
        if (mobileToggleIcon) {
          mobileToggleIcon.classList.remove('bx-x');
          mobileToggleIcon.classList.add('bx-menu');
        }
      });
    });
  }

  // 3. Automated Slideshow Hero (For Home Page)
  const slides = document.querySelectorAll('.hero-slide');
  const prevBtn = document.querySelector('.prev-arrow');
  const nextBtn = document.querySelector('.next-arrow');
  const dotsContainer = document.querySelector('.slide-indicators');
  
  if (slides.length > 0) {
    let currentSlideIndex = 0;
    let slideInterval;
    
    // Create indicator dots dynamically if dotsContainer is present
    if (dotsContainer) {
      dotsContainer.innerHTML = '';
      slides.forEach((_, index) => {
        const dot = document.createElement('button');
        dot.classList.add('indicator-dot');
        if (index === 0) dot.classList.add('active');
        dot.setAttribute('aria-label', `Go to slide ${index + 1}`);
        dot.addEventListener('click', () => {
          setSlide(index);
        });
        dotsContainer.appendChild(dot);
      });
    }

    const dots = document.querySelectorAll('.indicator-dot');

    function updateSlides() {
      slides.forEach((slide, index) => {
        if (index === currentSlideIndex) {
          slide.classList.add('active');
        } else {
          slide.classList.remove('active');
        }
      });

      if (dots.length > 0) {
        dots.forEach((dot, index) => {
          if (index === currentSlideIndex) {
            dot.classList.add('active');
          } else {
            dot.classList.remove('active');
          }
        });
      }
    }

    function nextSlide() {
      currentSlideIndex = (currentSlideIndex + 1) % slides.length;
      updateSlides();
    }

    function prevSlide() {
      currentSlideIndex = (currentSlideIndex - 1 + slides.length) % slides.length;
      updateSlides();
    }

    function setSlide(index) {
      currentSlideIndex = index;
      updateSlides();
      stopSlideshow();
      startSlideshow();
    }

    function startSlideshow() {
      slideInterval = setInterval(nextSlide, 3500);
    }

    function stopSlideshow() {
      if (slideInterval) {
        clearInterval(slideInterval);
      }
    }

    // Attach event listeners
    if (prevBtn) prevBtn.addEventListener('click', prevSlide);
    if (nextBtn) nextBtn.addEventListener('click', nextSlide);

    // Initialize slideshow
    startSlideshow();
    updateSlides();
  }

  // 4. Smooth Anchor Scrolling with Offsets (For Service Detail Tabs)
  const sidebarLinks = document.querySelectorAll('.sidebar-link');
  sidebarLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = link.getAttribute('href') || link.getAttribute('data-target');
      if (targetId) {
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
          const offsetPosition = targetElement.offsetTop - 110; // Scroll margin offset
          window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
          });
        }
      }
    });
  });

  // 5. Intersection Observer for Scroll Reveal Animations
  const revealElements = document.querySelectorAll('.reveal-on-scroll');
  
  if ('IntersectionObserver' in window) {
    const observerOptions = {
      root: null,
      rootMargin: '0px 0px -80px 0px',
      threshold: 0.08
    };
    
    const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);
    
    revealElements.forEach(el => observer.observe(el));
  } else {
    revealElements.forEach(el => el.classList.add('revealed'));
  }

  // 6. Mobile Dropdown Toggle for accordion menu
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

  // 7. Dynamic Shared Footer Component
  const footerElement = document.querySelector('.navy-footer');
  if (footerElement) {
    const isSubpage = window.location.pathname.includes('/services/');
    const pathPrefix = isSubpage ? '../' : '';
    
    // Core Links
    const homeLink = `${pathPrefix}index.html`;
    const aboutLink = `${pathPrefix}about.html`;
    const servicesLink = `${pathPrefix}services.html`;
    const contactLink = `${pathPrefix}contact.html`;
    const logoSrc = `${pathPrefix}assets/logo.jpg`;
    
    // Service Links
    const motorLink = isSubpage ? 'motor-property.html' : 'services/motor-property.html';
    const accidentLink = isSubpage ? 'accident-reconstruction.html' : 'services/accident-reconstruction.html';
    const documentLink = isSubpage ? 'document-examination.html' : 'services/document-examination.html';
    const fingerprintLink = isSubpage ? 'fingerprint-analysis.html' : 'services/fingerprint-analysis.html';
    
    footerElement.innerHTML = `
    <div class="tracevia-container grid grid-cols-1 md:grid-cols-2 lg:grid-cols-[1.5fr_1fr_1fr_1.2fr] gap-12 border-b border-white/5 pb-12">

      <!-- Column 1: About -->
      <div class="footer-col footer-about flex flex-col gap-6">
        <div class="footer-logo">
          <img src="${logoSrc}" alt="Tracevia Forensics Services"
            class="logo-image-footer h-12 rounded border border-white/10 object-contain">
        </div>
        <p class="footer-desc text-sm leading-relaxed text-text-white-muted">
          Delivering truth through science, precision, and integrity. Trusted forensic experts providing independent
          investigations and evidence-based solutions across India.
        </p>
        <div class="social-links flex gap-4 text-xl">
          <a href="#"
            class="w-10 h-10 rounded-full bg-white/5 border border-white/8 hover:bg-accent-cyan hover:text-navy-deep flex items-center justify-center text-white transition-all"
            aria-label="LinkedIn"><i class='bx bxl-linkedin'></i></a>
          <a href="#"
            class="w-10 h-10 rounded-full bg-white/5 border border-white/8 hover:bg-accent-cyan hover:text-navy-deep flex items-center justify-center text-white transition-all"
            aria-label="Twitter"><i class='bx bxl-twitter'></i></a>
          <a href="#"
            class="w-10 h-10 rounded-full bg-white/5 border border-white/8 hover:bg-accent-cyan hover:text-navy-deep flex items-center justify-center text-white transition-all"
            aria-label="Facebook"><i class='bx bxl-facebook'></i></a>
        </div>
      </div>

      <!-- Column 2: Quick Links -->
      <div class="footer-col">
        <h4 class="footer-title font-outfit text-white text-lg font-bold mb-6 relative">Quick Navigation</h4>
        <ul class="footer-links flex flex-col gap-3.5 text-sm">
          <li><a href="${homeLink}" class="hover:text-accent-cyan flex items-center gap-1 transition-all"><i
                class='bx bx-chevron-right'></i> Home Page</a></li>
          <li><a href="${aboutLink}" class="hover:text-accent-cyan flex items-center gap-1 transition-all"><i
                class='bx bx-chevron-right'></i> About Us</a></li>
          <li><a href="${servicesLink}" class="hover:text-accent-cyan flex items-center gap-1 transition-all"><i
                class='bx bx-chevron-right'></i> Our Services</a></li>
          <li><a href="${contactLink}" class="hover:text-accent-cyan flex items-center gap-1 transition-all"><i
                class='bx bx-chevron-right'></i> Contact & Inquiries</a></li>
        </ul>
      </div>

      <!-- Column 3: Core Services -->
      <div class="footer-col">
        <h4 class="footer-title font-outfit text-white text-lg font-bold mb-6 relative">Our Services</h4>
        <ul class="footer-links flex flex-col gap-3.5 text-sm">
          <li><a href="${motorLink}"
              class="hover:text-accent-cyan flex items-center gap-1 transition-all"><i class='bx bx-chevron-right'></i>
              Claim Investigation</a></li>
          <li><a href="${accidentLink}"
              class="hover:text-accent-cyan flex items-center gap-1 transition-all"><i class='bx bx-chevron-right'></i>
              Accident Reconstruction</a></li>
          <li><a href="${documentLink}"
              class="hover:text-accent-cyan flex items-center gap-1 transition-all"><i class='bx bx-chevron-right'></i>
              Document Examination</a></li>
          <li><a href="${fingerprintLink}"
              class="hover:text-accent-cyan flex items-center gap-1 transition-all"><i class='bx bx-chevron-right'></i>
              Fingerprint Disputes</a></li>
        </ul>
      </div>

      <!-- Column 4: Contact info -->
      <div class="footer-col">
        <h4 class="footer-title font-outfit text-white text-lg font-bold mb-6 relative">Get in Touch</h4>
        <ul class="contact-details flex flex-col gap-4 text-sm">
          <li class="flex gap-3">
            <i class='bx bx-phone text-accent-cyan text-2xl mt-1'></i>
            <div>
              <span class="detail-label block text-xs text-text-white-muted">Phone Support</span>
              <a href="tel:+91-9999903390"
                class="detail-value block text-white font-semibold hover:text-accent-cyan">+91-9999903390</a>
              <a href="tel:+91-8958598829"
                class="detail-value block text-white font-semibold hover:text-accent-cyan">+91-8958598829</a>
            </div>
          </li>
          <li class="flex gap-3">
            <i class='bx bx-envelope text-accent-cyan text-2xl mt-1'></i>
            <div>
              <span class="detail-label block text-xs text-text-white-muted">Email Us</span>
              <a href="mailto:traceviaforensics@gmail.com"
                class="detail-value text-white font-semibold hover:text-accent-cyan">traceviaforensics@gmail.com</a>
            </div>
          </li>
          <li class="flex gap-3">
            <i class='bx bx-map text-accent-cyan text-2xl mt-1'></i>
            <div>
              <span class="detail-label block text-xs text-text-white-muted">Head Office & Lab</span>
              <span class="detail-value text-white font-semibold">I-1504, Samridhi Luxuria Avenue, Sector-150, Noida,
                Uttar Pradesh, 201310</span>
            </div>
          </li>
        </ul>
      </div>

    </div>

    <!-- Bottom footer -->
    <div
      class="tracevia-container pt-8 flex flex-col sm:flex-row justify-between items-center gap-4 text-xs text-text-white-muted">
      <p>&copy; 2026 Tracevia Forensics Services Private Limited. All rights reserved. Under strict scientific
        guidelines.</p>

      <div class="footer-policy-links flex gap-6">
        <a href="#" class="hover:text-accent-cyan transition-all">Privacy Policy</a>
        <a href="#" class="hover:text-accent-cyan transition-all">Terms of Service</a>
      </div>
    </div>
    `;
  }

});