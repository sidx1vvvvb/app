import React, { useState } from "react";
import { mockProducts } from "../data/mockData";
import { Star, Heart, ShoppingBag, Sparkles } from "lucide-react";

const ProductsSection = () => {
  const [hoveredProduct, setHoveredProduct] = useState(null);

  return (
    <section id="products" className="py-32 bg-gradient-to-br from-slate-50 via-white to-slate-100 relative overflow-hidden">
      {/* Background Artistry */}
      <div className="absolute inset-0 opacity-30">
        <div className="absolute top-20 left-10 w-72 h-72 bg-gradient-to-br from-amber-200/20 to-emerald-200/20 rounded-full blur-3xl"></div>
        <div className="absolute bottom-20 right-10 w-96 h-96 bg-gradient-to-br from-rose-200/20 to-amber-200/20 rounded-full blur-3xl"></div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
        {/* Premium Section Header */}
        <div className="text-center mb-20">
          <div className="inline-flex items-center glass-badge mb-8">
            <Sparkles className="w-4 h-4 text-amber-600 mr-2" />
            <span className="text-sm font-medium text-gray-700 tracking-wide">CURATED COLLECTION</span>
          </div>
          
          <h2 className="text-5xl md:text-7xl font-thin text-gray-800 mb-8 leading-tight">
            Our <span className="bg-gradient-to-r from-amber-600 to-emerald-600 bg-clip-text text-transparent">Artisanal</span> Products
          </h2>
          
          <div className="max-w-4xl mx-auto glass-container">
            <p className="text-xl md:text-2xl text-gray-600 leading-relaxed font-light">
              Each creation is a masterpiece, crafted by <span className="text-amber-700 font-medium">master artisans</span> 
              who transform nature's finest ingredients into <span className="text-emerald-700 font-medium">liquid gold</span> 
              that awakens your senses and nourishes your soul.
            </p>
          </div>
        </div>

        {/* Premium Products Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-16">
          {mockProducts.map((product, index) => (
            <div
              key={index}
              className="product-card group relative"
              onMouseEnter={() => setHoveredProduct(index)}
              onMouseLeave={() => setHoveredProduct(null)}
            >
              {/* Product Image Container */}
              <div className="relative overflow-hidden rounded-2xl mb-6 aspect-square">
                <img
                  src={product.image}
                  alt={product.name}
                  className="w-full h-full object-cover transition-all duration-700 group-hover:scale-110"
                />
                
                {/* Premium Overlay */}
                <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                
                {/* Floating Action Buttons */}
                <div className={`absolute top-4 right-4 flex flex-col gap-3 transition-all duration-500 ${
                  hoveredProduct === index ? 'opacity-100 translate-x-0' : 'opacity-0 translate-x-4'
                }`}>
                  <button className="glass-button w-12 h-12 flex items-center justify-center group/btn">
                    <Heart className="w-5 h-5 text-white group-hover/btn:text-rose-300 transition-colors duration-300" />
                  </button>
                  <button className="glass-button w-12 h-12 flex items-center justify-center group/btn">
                    <ShoppingBag className="w-5 h-5 text-white group-hover/btn:text-emerald-300 transition-colors duration-300" />
                  </button>
                </div>

                {/* Premium Badge */}
                <div className="absolute top-4 left-4">
                  <div className="glass-badge">
                    <span className="text-xs font-medium text-white/90">{product.category}</span>
                  </div>
                </div>

                {/* Rating Stars */}
                <div className="absolute bottom-4 left-4 flex items-center space-x-1">
                  {[...Array(5)].map((_, i) => (
                    <Star
                      key={i}
                      className="w-4 h-4 text-amber-300 fill-current"
                    />
                  ))}
                </div>
              </div>
              
              {/* Product Details */}
              <div className="space-y-4">
                <div className="flex items-center justify-between">
                  <h3 className="text-xl font-light text-gray-800 group-hover:text-emerald-700 transition-colors duration-300">
                    {product.name}
                  </h3>
                  <div className="text-right">
                    <div className="text-2xl font-light text-gray-800">${product.price}</div>
                    <div className="text-xs text-gray-500 line-through">$29.99</div>
                  </div>
                </div>
                
                <p className="text-gray-600 text-sm leading-relaxed font-light">
                  {product.description}
                </p>
                
                {/* Premium CTA */}
                <button className="w-full premium-button-small group/cta">
                  <span className="flex items-center justify-center">
                    <ShoppingBag className="w-4 h-4 mr-2 group-hover/cta:scale-110 transition-transform duration-300" />
                    Add to Collection
                  </span>
                </button>
              </div>

              {/* Premium Glow Effect */}
              <div className={`absolute -inset-1 bg-gradient-to-r from-amber-600 via-emerald-600 to-amber-600 rounded-3xl opacity-0 group-hover:opacity-20 blur-xl transition-opacity duration-700`}></div>
            </div>
          ))}
        </div>

        {/* Premium Collection CTA */}
        <div className="text-center">
          <div className="inline-block glass-container p-8 rounded-3xl">
            <h3 className="text-2xl font-light text-gray-800 mb-4">
              Experience the Complete Collection
            </h3>
            <p className="text-gray-600 mb-6 font-light">
              Join thousands who have discovered the art of premium organic cuisine
            </p>
            <button className="premium-button">
              <span className="flex items-center">
                <Sparkles className="w-5 h-5 mr-2" />
                Explore Full Collection
              </span>
            </button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ProductsSection;