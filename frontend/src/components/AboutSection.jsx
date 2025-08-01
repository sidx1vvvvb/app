import React, { useEffect, useState } from "react";
import { Leaf, Heart, Award, Users, Globe, Crown } from "lucide-react";

const AboutSection = () => {
  const [isVisible, setIsVisible] = useState(false);
  const [activeFeature, setActiveFeature] = useState(0);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true);
        }
      },
      { threshold: 0.3 }
    );

    const element = document.getElementById('about');
    if (element) observer.observe(element);

    return () => observer.disconnect();
  }, []);

  const features = [
    {
      icon: <Crown className="w-8 h-8 text-amber-600" />,
      title: "Royal Heritage",
      description: "Recipes passed down through generations of master craftsmen, each dish a testament to centuries of culinary excellence.",
      gradient: "from-amber-500 to-yellow-500"
    },
    {
      icon: <Heart className="w-8 h-8 text-rose-600" />,
      title: "Crafted with Soul",
      description: "Every ingredient is hand-selected with love, transforming simple elements into extraordinary experiences that touch your heart.",
      gradient: "from-rose-500 to-pink-500"
    },
    {
      icon: <Award className="w-8 h-8 text-emerald-600" />,
      title: "Award-Winning Excellence",
      description: "Recognized globally by culinary masters and food critics as the pinnacle of organic cuisine innovation.",
      gradient: "from-emerald-500 to-teal-500"
    }
  ];

  const stats = [
    { number: "50K+", label: "Happy Families", icon: <Users className="w-6 h-6" /> },
    { number: "25+", label: "Countries", icon: <Globe className="w-6 h-6" /> },
    { number: "100%", label: "Organic", icon: <Leaf className="w-6 h-6" /> },
    { number: "3", label: "Michelin Stars", icon: <Award className="w-6 h-6" /> }
  ];

  return (
    <section id="about" className="py-32 bg-gradient-to-br from-gray-50 via-white to-slate-100 relative overflow-hidden">
      {/* Premium Background Elements */}
      <div className="absolute inset-0 opacity-40">
        <div className="absolute top-10 left-1/4 w-64 h-64 bg-gradient-to-br from-amber-200/30 to-transparent rounded-full blur-3xl"></div>
        <div className="absolute bottom-20 right-1/4 w-96 h-96 bg-gradient-to-br from-emerald-200/30 to-transparent rounded-full blur-3xl"></div>
        <div className="absolute top-1/2 left-10 w-32 h-32 bg-gradient-to-br from-rose-200/30 to-transparent rounded-full blur-2xl"></div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
        {/* Emotional Header */}
        <div className={`text-center mb-20 transition-all duration-1000 ${isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'}`}>
          <div className="inline-flex items-center glass-badge mb-8">
            <Heart className="w-4 h-4 text-rose-600 mr-2 animate-pulse" />
            <span className="text-sm font-medium text-gray-700 tracking-wide">OUR PASSIONATE STORY</span>
          </div>
          
          <h2 className="text-5xl md:text-7xl font-thin text-gray-800 mb-8 leading-tight">
            Where <span className="bg-gradient-to-r from-amber-600 via-rose-600 to-emerald-600 bg-clip-text text-transparent">Love</span> Meets
            <br />
            <span className="bg-gradient-to-r from-emerald-600 to-teal-600 bg-clip-text text-transparent">Perfection</span>
          </h2>
          
          <div className="max-w-4xl mx-auto glass-container">
            <p className="text-xl md:text-2xl text-gray-600 leading-relaxed font-light">
              In the heart of pristine valleys, where morning mist kisses organic gardens, 
              <span className="text-amber-700 font-medium"> our story begins</span>. Three generations of 
              passionate artisans have poured their souls into creating 
              <span className="text-emerald-700 font-medium"> liquid poetry</span> that doesn't just nourish your body, 
              but awakens your very essence.
            </p>
          </div>
        </div>

        {/* Premium Feature Cards */}
        <div className={`grid grid-cols-1 md:grid-cols-3 gap-8 mb-20 transition-all duration-1200 delay-300 ${isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'}`}>
          {features.map((feature, index) => (
            <div
              key={index}
              className="group relative"
              onMouseEnter={() => setActiveFeature(index)}
            >
              <div className="product-card h-full cursor-pointer">
                <div className={`w-16 h-16 rounded-2xl bg-gradient-to-br ${feature.gradient} flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300`}>
                  {feature.icon}
                </div>
                
                <h3 className="text-2xl font-light text-gray-800 mb-4 group-hover:text-amber-700 transition-colors duration-300">
                  {feature.title}
                </h3>
                
                <p className="text-gray-600 leading-relaxed font-light">
                  {feature.description}
                </p>

                {/* Premium Glow Effect */}
                <div className={`absolute -inset-1 bg-gradient-to-r ${feature.gradient} rounded-3xl opacity-0 group-hover:opacity-20 blur-xl transition-opacity duration-700`}></div>
              </div>
            </div>
          ))}
        </div>

        {/* Emotional Story Section */}
        <div className={`grid grid-cols-1 lg:grid-cols-2 gap-16 items-center mb-20 transition-all duration-1000 delay-600 ${isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'}`}>
          <div className="space-y-8">
            <h3 className="text-3xl md:text-4xl font-thin text-gray-800 leading-tight">
              Every Bowl Tells a 
              <span className="bg-gradient-to-r from-amber-600 to-emerald-600 bg-clip-text text-transparent"> Sacred Story</span>
            </h3>
            
            <div className="space-y-6 text-gray-600 leading-relaxed font-light text-lg">
              <p>
                From the first rays of dawn illuminating our organic gardens to the careful 
                hands that harvest each ingredient at the perfect moment of ripeness, our 
                journey is one of <span className="text-amber-700 font-medium">absolute devotion</span>.
              </p>
              
              <p>
                Our master chefs don't just cook—they compose symphonies of flavor that 
                dance on your palate and create memories that last forever. Each spoonful 
                carries the essence of <span className="text-emerald-700 font-medium">pure nature</span>, 
                the warmth of tradition, and the promise of wellness.
              </p>
              
              <p>
                This isn't just food. This is a <span className="text-rose-700 font-medium">love letter</span> to 
                your soul, written in the language of taste, crafted with ingredients that 
                have been blessed by sun, rain, and time itself.
              </p>
            </div>

            <div className="flex space-x-4">
              <button className="premium-button-small">
                <span>Our Heritage</span>
              </button>
              <button className="glass-button px-6 py-3 text-gray-700 hover:text-amber-700">
                <span>Meet Our Artisans</span>
              </button>
            </div>
          </div>
          
          <div className="relative">
            <div className="glass-container p-2 rounded-3xl">
              <img
                src="https://images.unsplash.com/photo-1590794056675-8354831935b2?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3MjQyMTd8MHwxfHNlYXJjaHwyfHxvcmdhbmljJTIwc291cCUyMGJvd2xzfGVufDB8fHx8MTc1NDA2MjQ3NHww&ixlib=rb-4.1.0&q=85"
                alt="Artisan crafting organic food"
                className="rounded-2xl w-full h-96 object-cover"
              />
            </div>
            
            {/* Floating Elements */}
            <div className="absolute -top-6 -right-6 glass-card animate-float-slow">
              <Crown className="w-6 h-6 text-amber-600" />
              <span className="text-gray-700 text-sm font-medium ml-2">Master Crafted</span>
            </div>
            
            <div className="absolute -bottom-6 -left-6 glass-card animate-float-medium">
              <Heart className="w-6 h-6 text-rose-600" />
              <span className="text-gray-700 text-sm font-medium ml-2">Made with Love</span>
            </div>
          </div>
        </div>

        {/* Premium Stats */}
        <div className={`glass-container rounded-3xl transition-all duration-1000 delay-900 ${isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'}`}>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
            {stats.map((stat, index) => (
              <div key={index} className="text-center group">
                <div className="flex justify-center mb-4">
                  <div className="w-12 h-12 rounded-full bg-gradient-to-br from-amber-500 to-emerald-500 flex items-center justify-center text-white group-hover:scale-110 transition-transform duration-300">
                    {stat.icon}
                  </div>
                </div>
                <div className="text-3xl md:text-4xl font-light text-gray-800 mb-2 group-hover:text-amber-700 transition-colors duration-300">
                  {stat.number}
                </div>
                <div className="text-gray-600 font-light">
                  {stat.label}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default AboutSection;