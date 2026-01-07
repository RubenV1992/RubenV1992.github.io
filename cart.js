// Cart State Management with localStorage
class Cart {
  constructor() {
    this.items = this.loadCart();
    this.init();
  }

  // Load cart from localStorage
  loadCart() {
    try {
      const saved = localStorage.getItem('valhalla-cart');
      return saved ? JSON.parse(saved) : [];
    } catch (e) {
      console.error('Error loading cart:', e);
      return [];
    }
  }

  // Save cart to localStorage
  saveCart() {
    try {
      localStorage.setItem('valhalla-cart', JSON.stringify(this.items));
    } catch (e) {
      console.error('Error saving cart:', e);
    }
  }

  // Initialize cart UI and event listeners
  init() {
    this.renderProducts();
    this.setupCartUI();
    this.updateCartBadge();
    this.renderCart();
    
    // Set current year in footer
    const yearEl = document.getElementById('year');
    if (yearEl) {
      yearEl.textContent = new Date().getFullYear();
    }
  }

  // Product data - In production, this would come from an API
  getProducts() {
    return [
      {
        id: 1,
        name: "Baldur's Gin",
        description: 'Premium craft gin with botanical notes. Smooth and refined, perfect for cocktails or sipping neat. 40% ABV.',
        price: 34.99,
        image: "images/Valhalla Brewery images/Baldur's gin 4.png",
        slogan: null // No slogan image available
      },
      {
        id: 2,
        name: "Fenrir's Wrath",
        description: 'Bold and powerful beer with intense flavors. A fierce brew that commands respect. 7.5% ABV.',
        price: 12.99,
        image: "images/Valhalla Brewery images/Fenrir´s wrath.png",
        slogan: "images/Valhalla Brewery images/Fenrir's Wrath Slogan.png"
      },
      {
        id: 3,
        name: "Freya's Might",
        description: 'Elegant wine with complex flavors. A tribute to strength and beauty. Perfect for special occasions.',
        price: 28.99,
        image: "images/Valhalla Brewery images/Freyas Might bottle.png",
        slogan: "images/Valhalla Brewery images/Freya's wine slogan 1.png"
      },
      {
        id: 4,
        name: "Hela's Wine",
        description: 'Mysterious and deep wine with rich undertones. A journey into the depths of flavor. Premium quality.',
        price: 32.99,
        image: "images/Valhalla Brewery images/Hela Wine 3.png",
        slogan: "images/Valhalla Brewery images/Hela's wine slogan 2.png"
      },
      {
        id: 5,
        name: "Mjolnir Thunder Energy Drink",
        description: 'Powerful energy drink inspired by the legendary hammer. Boost your strength and vitality.',
        price: 4.99,
        image: "images/Valhalla Brewery images/Mjolnir thunder energy drink.png",
        slogan: "images/Valhalla Brewery images/MJOLNIR SLOGAN.png"
      },
      {
        id: 6,
        name: "Odin's Might",
        description: 'Supreme craft beer worthy of the All-Father. Rich, complex, and commanding. 8.0% ABV.',
        price: 15.99,
        image: "images/Valhalla Brewery images/Odin's Might bottle 2.png",
        slogan: null // No slogan image available
      }
    ];
  }

  // Render product cards
  renderProducts() {
    const grid = document.getElementById('products-grid');
    if (!grid) return;

    const products = this.getProducts();
    grid.innerHTML = products.map(product => `
      <article class="product-card" data-product-id="${product.id}">
        <div class="product-image-container">
          <img src="${product.image}" alt="${product.name}" class="product-image" />
          ${product.slogan ? `<div class="product-slogan-container">
            <img src="${product.slogan}" alt="${product.name} slogan" class="product-slogan" />
          </div>` : ''}
        </div>
        <div class="product-info">
          <h3 class="product-name">${this.escapeHtml(product.name)}</h3>
          <p class="product-description">${this.escapeHtml(product.description)}</p>
          <div class="product-price">$${product.price.toFixed(2)}</div>
          <button class="add-to-cart-btn" data-product-id="${product.id}">
            Add to Cart
          </button>
        </div>
      </article>
    `).join('');

    // Add event listeners to Add to Cart buttons
    document.querySelectorAll('.add-to-cart-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const productId = parseInt(btn.dataset.productId);
        this.addToCart(productId);
      });
    });
  }

  // Add product to cart
  addToCart(productId) {
    const products = this.getProducts();
    const product = products.find(p => p.id === productId);
    
    if (!product) return;

    const existingItem = this.items.find(item => item.id === productId);
    
    if (existingItem) {
      existingItem.quantity += 1;
    } else {
      this.items.push({
        id: product.id,
        name: product.name,
        price: product.price,
        quantity: 1
      });
    }

    this.saveCart();
    this.updateCartBadge();
    this.renderCart();
    
    // Visual feedback on button
    const btn = document.querySelector(`[data-product-id="${productId}"]`);
    if (btn) {
      btn.style.transform = 'scale(0.95)';
      setTimeout(() => {
        btn.style.transform = '';
      }, 150);
    }
  }

  // Remove product from cart
  removeFromCart(productId) {
    this.items = this.items.filter(item => item.id !== productId);
    this.saveCart();
    this.updateCartBadge();
    this.renderCart();
  }

  // Update quantity
  updateQuantity(productId, change) {
    const item = this.items.find(item => item.id === productId);
    if (!item) return;

    item.quantity += change;
    
    if (item.quantity <= 0) {
      this.removeFromCart(productId);
    } else {
      this.saveCart();
      this.updateCartBadge();
      this.renderCart();
    }
  }

  // Update cart badge count
  updateCartBadge() {
    const badge = document.getElementById('cart-badge');
    if (!badge) return;

    const totalItems = this.items.reduce((sum, item) => sum + item.quantity, 0);
    badge.textContent = totalItems;
    badge.style.display = totalItems > 0 ? 'flex' : 'none';
  }

  // Render cart items
  renderCart() {
    const cartItems = document.getElementById('cart-items');
    const cartEmpty = document.getElementById('cart-empty');
    const cartFooter = document.getElementById('cart-footer');
    const checkoutBtn = document.getElementById('checkout-btn');

    if (!cartItems || !cartEmpty || !cartFooter) return;

    if (this.items.length === 0) {
      cartItems.innerHTML = '';
      cartEmpty.style.display = 'block';
      checkoutBtn.disabled = true;
    } else {
      cartEmpty.style.display = 'none';
      checkoutBtn.disabled = false;
      
      cartItems.innerHTML = this.items.map(item => `
        <div class="cart-item">
          <div class="cart-item-info">
            <div class="cart-item-name">${this.escapeHtml(item.name)}</div>
            <div class="cart-item-price">$${item.price.toFixed(2)} each</div>
            <div class="cart-item-controls">
              <button class="quantity-btn" data-action="decrease" data-product-id="${item.id}">−</button>
              <span class="quantity-display">${item.quantity}</span>
              <button class="quantity-btn" data-action="increase" data-product-id="${item.id}">+</button>
              <button class="remove-item-btn" data-product-id="${item.id}">Remove</button>
            </div>
          </div>
        </div>
      `).join('');

      // Add event listeners
      cartItems.querySelectorAll('[data-action]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          const productId = parseInt(btn.dataset.productId);
          const action = btn.dataset.action;
          
          if (action === 'increase') {
            this.updateQuantity(productId, 1);
          } else if (action === 'decrease') {
            this.updateQuantity(productId, -1);
          }
        });
      });

      cartItems.querySelectorAll('.remove-item-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          const productId = parseInt(btn.dataset.productId);
          this.removeFromCart(productId);
        });
      });
    }

    // Update total
    const total = this.items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    const totalEl = document.getElementById('cart-total');
    if (totalEl) {
      totalEl.textContent = `$${total.toFixed(2)}`;
    }
  }

  // Setup cart UI (open/close)
  setupCartUI() {
    const cartToggle = document.getElementById('cart-toggle');
    const cartClose = document.getElementById('cart-close');
    const cartOverlay = document.getElementById('cart-overlay');
    const cartSidebar = document.getElementById('cart-sidebar');

    const openCart = () => {
      cartOverlay?.classList.add('active');
      cartSidebar?.classList.add('active');
      document.body.style.overflow = 'hidden';
    };

    const closeCart = () => {
      cartOverlay?.classList.remove('active');
      cartSidebar?.classList.remove('active');
      document.body.style.overflow = '';
    };

    cartToggle?.addEventListener('click', openCart);
    cartClose?.addEventListener('click', closeCart);
    cartOverlay?.addEventListener('click', closeCart);

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && cartSidebar?.classList.contains('active')) {
        closeCart();
      }
    });

    // Checkout button (placeholder)
    const checkoutBtn = document.getElementById('checkout-btn');
    checkoutBtn?.addEventListener('click', () => {
      if (this.items.length > 0) {
        alert('Checkout functionality would be implemented here. Items in cart: ' + 
              this.items.reduce((sum, item) => sum + item.quantity, 0));
      }
    });
  }

  // Escape HTML to prevent XSS
  escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }
}

// Initialize cart when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  new Cart();
});
