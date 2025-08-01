import React, { useState, useEffect } from "react";
import { Mail, Phone, MapPin, Send, Heart, Star } from "lucide-react";
import { useToast } from "../hooks/use-toast";

const ContactSection = () => {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    message: "",
    newsletter: false
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });
  const { toast } = useToast();

  useEffect(() => {
    const handleMouseMove = (e) => {
      setMousePosition({ x: e.clientX, y: e.clientY });
    };
    window.addEventListener('mousemove', handleMouseMove);
    return () => window.removeEventListener('mousemove', handleMouseMove);
  }, []);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    console.log("Premium form submitted:", formData);
    toast({
      title: "✨ Message Sent with Love!",
      description: "Our artisan team will craft a personalized response just for you.",
    });
    
    setFormData({
      name: "",
      email: "",
      message: "",
      newsletter: false
    });
    setIsSubmitting(false);
  };

  const contactInfo = [
    {
      icon: <Phone className="w-6 h-6" />,
      title: "Call Our Artisans",
      detail: "+1 (555) 123-4567",
      subtitle: "Available 24/7 for your culinary journey",
      gradient: "from-emerald-500 to-teal-500"
    },
    {
      icon: <Mail className="w-6 h-6" />,
      title: "Email Our Hearts",
      detail: "hello@matifood.com",
      subtitle: "We respond with the same care we put in our food",
      gradient: "from-amber-500 to-yellow-500"
    },
    {
      icon: <MapPin className="w-6 h-6" />,
      title: "Visit Our Sanctuary",
      detail: "123 Organic Farm Road, Natural Valley, CA 90210",
      subtitle: "Where magic happens daily",
      gradient: "from-rose-500 to-pink-500"
    }
  ];

  return (
    <section id="contact" className="py-32 bg-gradient-to-br from-slate-900 via-gray-900 to-black relative overflow-hidden">
      {/* Ambient Lighting Effects */}
      <div className="absolute inset-0 opacity-30">
        <div className="absolute top-20 left-1/4 w-96 h-96 bg-gradient-to-br from-amber-500/20 to-transparent rounded-full blur-3xl"></div>
        <div className="absolute bottom-20 right-1/4 w-64 h-64 bg-gradient-to-br from-emerald-500/20 to-transparent rounded-full blur-3xl"></div>
      </div>

      {/* Floating Particles */}
      <div className="absolute inset-0">
        {[...Array(15)].map((_, i) => (
          <div
            key={i}
            className="absolute w-2 h-2 bg-amber-400/30 rounded-full animate-pulse"
            style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
              animationDelay: `${Math.random() * 3}s`,
              animationDuration: `${2 + Math.random() * 2}s`,
            }}
          />
        ))}
      </div>

      {/* Mouse Following Light */}
      <div 
        className="absolute w-96 h-96 rounded-full opacity-10 pointer-events-none mix-blend-screen transition-all duration-1000 ease-out"
        style={{
          background: `radial-gradient(circle, rgba(245, 158, 11, 0.4) 0%, transparent 70%)`,
          left: mousePosition.x - 192,
          top: mousePosition.y - 192,
        }}
      />

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
        {/* Emotional Header */}
        <div className="text-center mb-20">
          <div className="inline-flex items-center glass-badge mb-8">
            <Heart className="w-4 h-4 text-rose-400 mr-2 animate-pulse" />
            <span className="text-sm font-medium text-white/80 tracking-wide">LET'S CREATE MAGIC TOGETHER</span>
          </div>
          
          <h2 className="text-5xl md:text-7xl font-thin text-white mb-8 leading-tight">
            Share Your 
            <span className="bg-gradient-to-r from-amber-400 via-yellow-300 to-amber-400 bg-clip-text text-transparent"> Dreams</span>
          </h2>
          
          <div className="max-w-3xl mx-auto glass-container">
            <p className="text-xl text-white/90 leading-relaxed font-light">
              Every message you send becomes part of our story. Let's craft something 
              <span className="text-amber-300 font-medium"> extraordinary</span> together, 
              one conversation at a time.
            </p>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-12">
          {/* Contact Information */}
          <div className="lg:col-span-1 space-y-8">
            <div className="glass-container">
              <h3 className="text-2xl font-light text-white mb-8">Connect With Our Souls</h3>
              
              <div className="space-y-6">
                {contactInfo.map((info, index) => (
                  <div key={index} className="group cursor-pointer">
                    <div className="flex items-start space-x-4 p-4 rounded-2xl hover:bg-white/5 transition-all duration-300">
                      <div className={`w-12 h-12 rounded-xl bg-gradient-to-br ${info.gradient} flex items-center justify-center text-white group-hover:scale-110 transition-transform duration-300`}>
                        {info.icon}
                      </div>
                      <div className="flex-1">
                        <h4 className="font-medium text-white mb-1 group-hover:text-amber-300 transition-colors duration-300">
                          {info.title}
                        </h4>
                        <p className="text-white/90 mb-1">{info.detail}</p>
                        <p className="text-white/60 text-sm">{info.subtitle}</p>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Premium Testimonial */}
            <div className="glass-container">
              <div className="flex items-center mb-4">
                {[...Array(5)].map((_, i) => (
                  <Star key={i} className="w-5 h-5 text-amber-400 fill-current" />
                ))}
              </div>
              <p className="text-white/90 italic mb-4 leading-relaxed">
                "Mati Food doesn't just deliver products—they deliver pure happiness. 
                Every interaction feels like a warm embrace from family."
              </p>
              <div className="flex items-center">
                <img
                  src="https://images.unsplash.com/photo-1494790108755-2616b612b762?w=50&h=50&fit=crop&crop=face"
                  alt="Customer"
                  className="w-10 h-10 rounded-full mr-3"
                />
                <div>
                  <div className="text-white font-medium">Sarah Johnson</div>
                  <div className="text-white/60 text-sm">Food Enthusiast</div>
                </div>
              </div>
            </div>
          </div>

          {/* Premium Contact Form */}
          <div className="lg:col-span-2">
            <div className="glass-container">
              <form onSubmit={handleSubmit} className="space-y-8">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div className="space-y-2">
                    <label htmlFor="name" className="block text-sm font-medium text-white/80">
                      Your Beautiful Name
                    </label>
                    <input
                      type="text"
                      id="name"
                      name="name"
                      value={formData.name}
                      onChange={handleChange}
                      required
                      className="w-full px-6 py-4 bg-white/10 border border-white/20 rounded-2xl focus:outline-none focus:ring-2 focus:ring-amber-500/50 focus:border-amber-500/50 transition-all duration-300 text-white placeholder-white/50 backdrop-blur-sm"
                      placeholder="What should we call you?"
                    />
                  </div>

                  <div className="space-y-2">
                    <label htmlFor="email" className="block text-sm font-medium text-white/80">
                      Your Sacred Email
                    </label>
                    <input
                      type="email"
                      id="email"
                      name="email"
                      value={formData.email}
                      onChange={handleChange}
                      required
                      className="w-full px-6 py-4 bg-white/10 border border-white/20 rounded-2xl focus:outline-none focus:ring-2 focus:ring-amber-500/50 focus:border-amber-500/50 transition-all duration-300 text-white placeholder-white/50 backdrop-blur-sm"
                      placeholder="your.email@example.com"
                    />
                  </div>
                </div>

                <div className="space-y-2">
                  <label htmlFor="message" className="block text-sm font-medium text-white/80">
                    Share Your Heart
                  </label>
                  <textarea
                    id="message"
                    name="message"
                    value={formData.message}
                    onChange={handleChange}
                    rows={6}
                    className="w-full px-6 py-4 bg-white/10 border border-white/20 rounded-2xl focus:outline-none focus:ring-2 focus:ring-amber-500/50 focus:border-amber-500/50 transition-all duration-300 text-white placeholder-white/50 backdrop-blur-sm resize-none"
                    placeholder="Tell us about your dreams, your story, your culinary desires... We're listening with our hearts."
                  />
                </div>

                <div className="flex items-center space-x-3">
                  <input
                    type="checkbox"
                    id="newsletter"
                    name="newsletter"
                    checked={formData.newsletter}
                    onChange={handleChange}
                    className="w-5 h-5 text-amber-500 bg-white/10 border-white/20 rounded focus:ring-amber-500/50 focus:ring-2"
                  />
                  <label htmlFor="newsletter" className="text-white/80 leading-relaxed">
                    Yes, I want to receive love letters filled with recipes, stories, and exclusive previews of new creations.
                  </label>
                </div>

                <button
                  type="submit"
                  disabled={isSubmitting}
                  className="w-full premium-button group relative overflow-hidden"
                >
                  <span className="relative z-10 flex items-center justify-center">
                    {isSubmitting ? (
                      <>
                        <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin mr-3"></div>
                        Crafting Your Message...
                      </>
                    ) : (
                      <>
                        <Send className="w-5 h-5 mr-3 group-hover:translate-x-1 transition-transform duration-300" />
                        Send With Love
                      </>
                    )}
                  </span>
                </button>
              </form>

              <p className="text-xs text-white/50 mt-6 text-center leading-relaxed">
                This sacred space is protected by reCAPTCHA and the Google{" "}
                <a href="#" className="text-amber-400 hover:underline transition-colors duration-300">Privacy Policy</a>{" "}
                and{" "}
                <a href="#" className="text-amber-400 hover:underline transition-colors duration-300">Terms of Service</a>{" "}
                apply. Your trust is our most precious ingredient.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ContactSection;