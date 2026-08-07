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
});