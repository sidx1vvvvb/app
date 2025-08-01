import React, { useState } from "react";
import Header from "./Header";
import HeroSection from "./HeroSection";
import ProductsSection from "./ProductsSection";
import AboutSection from "./AboutSection";
import ContactSection from "./ContactSection";
import Footer from "./Footer";
import CookieConsent from "./CookieConsent";

const Home = () => {
  const [showCookieConsent, setShowCookieConsent] = useState(true);

  const handleAcceptCookies = () => {
    setShowCookieConsent(false);
  };

  return (
    <div className="min-h-screen">
      <Header />
      <HeroSection />
      <AboutSection />
      <ProductsSection />
      <ContactSection />
      <Footer />
      {showCookieConsent && (
        <CookieConsent onAccept={handleAcceptCookies} />
      )}
    </div>
  );
};

export default Home;