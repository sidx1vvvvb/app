import React, { useEffect, useState } from "react";
import { ChevronDown, Sparkles, Heart } from "lucide-react";

const HeroSection = () => {
  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    setIsLoaded(true);
    const handleMouseMove = (e) => {
      setMousePosition({ x: e.clientX, y: e.clientY });
    };
    window.addEventListener('mousemove', handleMouseMove);
    return () => window.removeEventListener('mousemove', handleMouseMove);
  }, []);

  const scrollToAbout = () => {
    const element = document.getElementById("about");
    if (element) {
      element.scrollIntoView({ behavior: "smooth" });
    }
  };

  return (
    <section
      id="home"
      className="relative min-h-screen flex items-center justify-center overflow-hidden"
    >
      {/* Animated Background Particles */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="floating-particles">
          {[...Array(20)].map((_, i) => (
            <div
              key={i}
              className="particle"
              style={{
                left: `${Math.random() * 100}%`,
                animationDelay: `${Math.random() * 3}s`,
                animationDuration: `${3 + Math.random() * 2}s`,
              }}
            />
          ))}
        </div>
      </div>

      {/* Hero Background with Parallax Effect */}
      <div
        className="absolute inset-0 z-0"
        style={{
          backgroundImage: `url('https://images.unsplash.com/photo-1679949479680-c65ef800b48b?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3MjQyMTd8MHwxfHNlYXJjaHwxfHxvcmdhbmljJTIwc291cCUyMGJvd2xzfGVufDB8fHx8MTc1NDA2MjQ3NHww&ixlib=rb-4.1.0&q=85')`,
          backgroundSize: "cover",
          backgroundPosition: "center",
          backgroundAttachment: "fixed",
          transform: `translate(${mousePosition.x * 0.01}px, ${mousePosition.y * 0.01}px)`,
        }}
      >
        {/* Luxury Gradient Overlay */}
        <div className="absolute inset-0 bg-gradient-to-br from-amber-900/30 via-transparent to-emerald-900/40"></div>
        <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent"></div>
        
        {/* Glassmorphism Layer */}
        <div className="absolute inset-0 backdrop-blur-[0.5px] bg-gradient-to-br from-white/5 to-transparent"></div>
      </div>

      {/* Floating Glass Cards */}
      <div className="absolute top-20 left-10 glass-card animate-float-slow">
        <Sparkles className="w-6 h-6 text-amber-300" />
        <span className="text-white/90 text-sm font-medium ml-2">Premium Organic</span>
      </div>
      
      <div className="absolute top-32 right-16 glass-card animate-float-medium">
        <Heart className="w-6 h-6 text-rose-300" />
        <span className="text-white/90 text-sm font-medium ml-2">Made with Love</span>
      </div>

      {/* Main Content */}
      <div className={`relative z-10 text-center px-4 sm:px-6 lg:px-8 max-w-6xl mx-auto transition-all duration-2000 ${isLoaded ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'}`}>
        
        {/* Premium Badge */}
        <div className="inline-flex items-center glass-badge mb-8 animate-glow">
          <Sparkles className="w-4 h-4 text-amber-300 mr-2" />
          <span className="text-sm font-medium text-white/90 tracking-wide">AWARD-WINNING ORGANIC CUISINE</span>
        </div>

        {/* Main Heading */}
        <h1 className="hero-title mb-8">
          <span className="block text-6xl md:text-8xl lg:text-9xl font-thin text-white leading-tight">
            Taste the
          </span>
          <span className="block text-6xl md:text-8xl lg:text-9xl font-thin bg-gradient-to-r from-amber-200 via-yellow-100 to-amber-300 bg-clip-text text-transparent leading-tight">
            Goodness
          </span>
          <span className="block text-5xl md:text-7xl lg:text-8xl font-thin text-white/90 leading-tight">
            of Nature
          </span>
        </h1>
        
        {/* Emotional Subtitle */}
        <div className="glass-container mb-12 max-w-4xl mx-auto">
          <p className="text-xl md:text-2xl text-white/95 leading-relaxed font-light">
            Every spoonful tells a story of <span className="text-amber-200 font-medium">passionate farmers</span>, 
            <span className="text-emerald-200 font-medium"> pristine ingredients</span>, and 
            <span className="text-rose-200 font-medium"> centuries-old traditions</span> crafted into 
            liquid poetry that nourishes your soul.
          </p>
        </div>

        {/* Premium CTA */}
        <div className="flex flex-col sm:flex-row gap-6 justify-center items-center">
          <button
            onClick={scrollToAbout}
            className="premium-button group"
          >
            <span className="relative z-10 flex items-center">
              Begin Your Journey
              <ChevronDown className="ml-3 w-5 h-5 group-hover:translate-y-1 transition-transform duration-300" />
            </span>
          </button>
          
          <div className="flex items-center glass-card cursor-pointer hover:scale-105 transition-all duration-300">
            <div className="w-3 h-3 bg-emerald-400 rounded-full animate-pulse mr-3"></div>
            <span className="text-white/90 font-medium">Limited Edition Collection</span>
          </div>
        </div>
      </div>

      {/* Scroll Indicator */}
      <div className="absolute bottom-8 left-1/2 transform -translate-x-1/2">
        <div className="scroll-indicator">
          <ChevronDown className="w-6 h-6 text-white/70" />
        </div>
      </div>

      {/* Ambient Light Effect */}
      <div 
        className="absolute w-96 h-96 rounded-full opacity-20 pointer-events-none mix-blend-screen transition-all duration-1000 ease-out"
        style={{
          background: `radial-gradient(circle, rgba(251, 191, 36, 0.3) 0%, transparent 70%)`,
          left: mousePosition.x - 192,
          top: mousePosition.y - 192,
        }}
      />
    </section>
  );
};

export default HeroSection;