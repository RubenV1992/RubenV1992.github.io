// Vehicle Data
const VEHICLES = [
  {
    id: 1,
    name: "Ferrari F8 Tributo",
    model: "2024",
    category: "Sports",
    image: "assets/images/car1.jpg",
    specs: {
      maxSpeed: 340,
      speedUnit: "km/h",
      acceleration: 2.9,
      accelerationUnit: "s",
      weight: 1330,
      weightUnit: "kg",
      height: 1206,
      heightUnit: "mm",
      fuelType: "Gasoline",
      maintenanceLevel: "High",
      vehicleType: "Sports"
    }
  },
  {
    id: 2,
    name: "Mercedes-Benz S-Class",
    model: "2024",
    category: "Luxury",
    image: "assets/images/car2.jpg",
    specs: {
      maxSpeed: 250,
      speedUnit: "km/h",
      acceleration: 4.5,
      accelerationUnit: "s",
      weight: 1950,
      weightUnit: "kg",
      height: 1509,
      heightUnit: "mm",
      fuelType: "Hybrid",
      maintenanceLevel: "Medium",
      vehicleType: "Luxury"
    }
  },
  {
    id: 3,
    name: "Tesla Model S Plaid",
    model: "2024",
    category: "Electric",
    image: "assets/images/car3.jpg",
    specs: {
      maxSpeed: 322,
      speedUnit: "km/h",
      acceleration: 2.1,
      accelerationUnit: "s",
      weight: 2162,
      weightUnit: "kg",
      height: 1441,
      heightUnit: "mm",
      fuelType: "Electric",
      maintenanceLevel: "Low",
      vehicleType: "Electric"
    }
  },
  {
    id: 4,
    name: "Range Rover Defender",
    model: "2024",
    category: "Off-road",
    image: "assets/images/car4.jpg",
    specs: {
      maxSpeed: 209,
      speedUnit: "km/h",
      acceleration: 6.1,
      accelerationUnit: "s",
      weight: 2310,
      weightUnit: "kg",
      height: 1969,
      heightUnit: "mm",
      fuelType: "Diesel",
      maintenanceLevel: "Medium",
      vehicleType: "Off-road"
    }
  },
  {
    id: 5,
    name: "Porsche 911 Turbo S",
    model: "2024",
    category: "Sports",
    image: "assets/images/car5.jpg",
    specs: {
      maxSpeed: 330,
      speedUnit: "km/h",
      acceleration: 2.7,
      accelerationUnit: "s",
      weight: 1640,
      weightUnit: "kg",
      height: 1301,
      heightUnit: "mm",
      fuelType: "Gasoline",
      maintenanceLevel: "High",
      vehicleType: "Sports"
    }
  },
  {
    id: 6,
    name: "BMW iX",
    model: "2024",
    category: "Electric",
    image: "assets/images/car6.jpg",
    specs: {
      maxSpeed: 200,
      speedUnit: "km/h",
      acceleration: 4.6,
      accelerationUnit: "s",
      weight: 2583,
      weightUnit: "kg",
      height: 1696,
      heightUnit: "mm",
      fuelType: "Electric",
      maintenanceLevel: "Low",
      vehicleType: "Electric"
    }
  }
];

// Carousel Manager
class Carousel {
  constructor() {
    this.currentIndex = 0;
    this.track = null;
    this.prevBtn = null;
    this.nextBtn = null;
    this.isTransitioning = false;
    this.init();
  }

  init() {
    this.renderVehicles();
    this.setupNavigation();
    this.setCurrentYear();
    this.updateNavigation();
  }

  // Render vehicle cards
  renderVehicles() {
    const track = document.getElementById('carousel-track');
    if (!track) return;

    track.innerHTML = VEHICLES.map(vehicle => `
      <div class="vehicle-card" data-vehicle-id="${vehicle.id}">
        <div class="vehicle-image-container">
          <img src="${vehicle.image}" 
               alt="${vehicle.name} ${vehicle.model}" 
               class="vehicle-image"
               onerror="this.src='data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTAwIiBoZWlnaHQ9IjYwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iOTAwIiBoZWlnaHQ9IjYwMCIgZmlsbD0iIzFhMWExYSIvPjx0ZXh0IHg9IjUwJSIgeT0iNTAlIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iMjQiIGZpbGw9IiNkNGFmMzciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGR5PSIuM2VtIj5WZWhpY2xlIEltYWdlPC90ZXh0Pjwvc3ZnPg=='">
          <div class="specs-panel">
            <div class="specs-header">
              <h2 class="vehicle-name">${this.escapeHtml(vehicle.name)}</h2>
              <span class="vehicle-category ${vehicle.category.toLowerCase().replace(' ', '')}">${this.escapeHtml(vehicle.category)}</span>
            </div>
            <div class="specs-grid">
              <div class="spec-item">
                <span class="spec-label">Max Speed</span>
                <div class="spec-value">
                  ${vehicle.specs.maxSpeed}
                  <span class="spec-unit">${vehicle.specs.speedUnit}</span>
                </div>
              </div>
              <div class="spec-item">
                <span class="spec-label">0-100 Acceleration</span>
                <div class="spec-value">
                  ${vehicle.specs.acceleration}
                  <span class="spec-unit">${vehicle.specs.accelerationUnit}</span>
                </div>
              </div>
              <div class="spec-item">
                <span class="spec-label">Weight</span>
                <div class="spec-value">
                  ${vehicle.specs.weight}
                  <span class="spec-unit">${vehicle.specs.weightUnit}</span>
                </div>
              </div>
              <div class="spec-item">
                <span class="spec-label">Height</span>
                <div class="spec-value">
                  ${vehicle.specs.height}
                  <span class="spec-unit">${vehicle.specs.heightUnit}</span>
                </div>
              </div>
              <div class="spec-item">
                <span class="spec-label">Fuel / Energy Type</span>
                <div class="spec-value">
                  <span class="spec-type">${this.escapeHtml(vehicle.specs.fuelType)}</span>
                </div>
              </div>
              <div class="spec-item">
                <span class="spec-label">Maintenance Level</span>
                <div class="spec-value">
                  <span class="spec-type">${this.escapeHtml(vehicle.specs.maintenanceLevel)}</span>
                </div>
              </div>
              <div class="spec-item">
                <span class="spec-label">Vehicle Type</span>
                <div class="spec-value">
                  <span class="spec-type">${this.escapeHtml(vehicle.specs.vehicleType)}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `).join('');

    this.track = track;
  }

  // Setup navigation
  setupNavigation() {
    this.prevBtn = document.getElementById('carousel-prev');
    this.nextBtn = document.getElementById('carousel-next');

    if (this.prevBtn) {
      this.prevBtn.addEventListener('click', () => this.prev());
    }

    if (this.nextBtn) {
      this.nextBtn.addEventListener('click', () => this.next());
    }

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') {
        this.prev();
      } else if (e.key === 'ArrowRight') {
        this.next();
      }
    });

    // Mouse wheel navigation (optional)
    const container = document.getElementById('carousel-container');
    if (container) {
      let wheelTimeout;
      container.addEventListener('wheel', (e) => {
        e.preventDefault();
        clearTimeout(wheelTimeout);
        wheelTimeout = setTimeout(() => {
          if (e.deltaY > 0) {
            this.next();
          } else if (e.deltaY < 0) {
            this.prev();
          }
        }, 50);
      }, { passive: false });
    }
  }

  // Move to previous vehicle
  prev() {
    if (this.isTransitioning) return;
    
    if (this.currentIndex > 0) {
      this.currentIndex--;
      this.updateCarousel();
      this.updateNavigation();
    }
  }

  // Move to next vehicle
  next() {
    if (this.isTransitioning) return;
    
    if (this.currentIndex < VEHICLES.length - 1) {
      this.currentIndex++;
      this.updateCarousel();
      this.updateNavigation();
    }
  }

  // Update carousel position
  updateCarousel() {
    if (!this.track) return;

    this.isTransitioning = true;
    const offset = -this.currentIndex * 100;
    this.track.style.transform = `translateX(${offset}%)`;

    setTimeout(() => {
      this.isTransitioning = false;
    }, 600);
  }

  // Update navigation button states
  updateNavigation() {
    if (this.prevBtn) {
      this.prevBtn.disabled = this.currentIndex === 0;
    }
    if (this.nextBtn) {
      this.nextBtn.disabled = this.currentIndex === VEHICLES.length - 1;
    }
  }

  // Escape HTML to prevent XSS
  escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Set current year in footer
  setCurrentYear() {
    const yearEl = document.getElementById('year');
    if (yearEl) {
      yearEl.textContent = new Date().getFullYear();
    }
  }
}

// Initialize carousel when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  new Carousel();
});
