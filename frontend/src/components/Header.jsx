import React, { useState, useEffect } from "react";
import { Menu, X, Sparkles } from "lucide-react";

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: "smooth" });
    }
    setIsMenuOpen(false);
  };

  return (
    <header className={`fixed top-0 left-0 w-full z-50 transition-all duration-500 ${
      scrolled 
        ? 'backdrop-blur-md bg-white/10 border-b border-white/20 shadow-2xl' 
        : 'bg-transparent'
    }`}>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center py-6">
          {/* Premium Logo */}
          <div className="flex items-center group cursor-pointer">
            <div className="relative">
              <Sparkles className="w-8 h-8 text-amber-300 mr-3 group-hover:rotate-180 transition-transform duration-700" />
              <div className="absolute inset-0 w-8 h-8 bg-amber-300/20 rounded-full animate-ping"></div>
            </div>
            <h1 className="text-3xl md:text-4xl font-thin text-white tracking-[0.2em] group-hover:text-amber-200 transition-colors duration-300">
              MATI FOOD
            </h1>
          </div>

          {/* Premium Desktop Navigation */}
          <nav className="hidden md:flex space-x-12">
            {['Home', 'About', 'Products', 'Contact'].map((item) => (
              <button
                key={item}
                onClick={() => scrollToSection(item.toLowerCase())}
                className="nav-link group relative"
              >
                <span className="relative z-10">{item}</span>
                <div className="absolute inset-0 glass-effect rounded-full scale-0 group-hover:scale-100 transition-transform duration-300"></div>
              </button>
            ))}
          </nav>

          {/* Mobile Menu Button */}
          <button
            onClick={() => setIsMenuOpen(!isMenuOpen)}
            className="md:hidden glass-button p-3"
          >
            {isMenuOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>

        {/* Premium Mobile Navigation */}
        {isMenuOpen && (
          <div className="md:hidden py-6 border-t border-white/20 backdrop-blur-md">
            <nav className="flex flex-col space-y-6">
              {['Home', 'About', 'Products', 'Contact'].map((item) => (
                <button
                  key={item}
                  onClick={() => scrollToSection(item.toLowerCase())}
                  className="text-left text-white/90 hover:text-amber-200 font-light text-lg transition-colors duration-300"
                >
                  {item}
                </button>
              ))}
            </nav>
          </div>
        )}
      </div>
    </header>
  );
};

export default Header;