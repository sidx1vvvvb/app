import React from "react";
import { mockProducts } from "../data/mockData";

const ProductsSection = () => {
  return (
    <section id="products" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-5xl font-serif font-light text-gray-800 mb-6">
            Our Natural Products
          </h2>
          <p className="text-lg md:text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
            Discover our carefully curated selection of organic and natural food products, 
            each crafted to bring you the finest flavors and nutrients nature has to offer.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {mockProducts.map((product, index) => (
            <div
              key={index}
              className="group bg-white rounded-lg shadow-md hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2 overflow-hidden"
            >
              <div className="relative overflow-hidden">
                <img
                  src={product.image}
                  alt={product.name}
                  className="w-full h-64 object-cover group-hover:scale-110 transition-transform duration-300"
                />
                <div className="absolute inset-0 bg-emerald-600/0 group-hover:bg-emerald-600/20 transition-all duration-300"></div>
              </div>
              
              <div className="p-6">
                <div className="flex items-center justify-between mb-2">
                  <span className="inline-block bg-emerald-100 text-emerald-800 text-xs px-2 py-1 rounded-full font-medium">
                    {product.category}
                  </span>
                  <span className="text-emerald-600 font-bold text-lg">
                    ${product.price}
                  </span>
                </div>
                
                <h3 className="text-xl font-semibold text-gray-800 mb-3 group-hover:text-emerald-600 transition-colors duration-200">
                  {product.name}
                </h3>
                
                <p className="text-gray-600 text-sm mb-4 line-clamp-3">
                  {product.description}
                </p>
                
                <button className="w-full bg-emerald-600 hover:bg-emerald-700 text-white py-2 px-4 rounded-md font-medium transition-colors duration-200 transform active:scale-95">
                  Learn More
                </button>
              </div>
            </div>
          ))}
        </div>

        <div className="text-center mt-12">
          <button className="bg-gray-800 hover:bg-gray-900 text-white px-8 py-4 rounded-full font-medium transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl">
            View All Products
          </button>
        </div>
      </div>
    </section>
  );
};

export default ProductsSection;