import React, { useState } from "react";
import { Mail, Phone, MapPin } from "lucide-react";
import { useToast } from "../hooks/use-toast";

const ContactSection = () => {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    message: "",
    newsletter: false
  });
  const { toast } = useToast();

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Mock form submission
    console.log("Form submitted:", formData);
    toast({
      title: "Message Sent!",
      description: "Thank you for contacting us. We'll get back to you soon!",
    });
    setFormData({
      name: "",
      email: "",
      message: "",
      newsletter: false
    });
  };

  return (
    <section id="contact" className="py-20 bg-gray-900 text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-5xl font-serif font-light mb-6">
            Contact Us
          </h2>
          <p className="text-xl text-gray-300 max-w-2xl mx-auto">
            Drop us a line!
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
          {/* Contact Information */}
          <div className="space-y-8">
            <div>
              <h3 className="text-2xl font-semibold mb-6">Get in Touch</h3>
              <p className="text-gray-300 leading-relaxed mb-8">
                We'd love to hear from you. Whether you have questions about our products, 
                need assistance with your order, or want to learn more about our organic 
                farming practices, we're here to help.
              </p>
            </div>

            <div className="space-y-6">
              <div className="flex items-center space-x-4">
                <div className="bg-emerald-600 p-3 rounded-full">
                  <Phone className="w-6 h-6" />
                </div>
                <div>
                  <h4 className="font-semibold">Phone</h4>
                  <p className="text-gray-300">+1 (555) 123-4567</p>
                </div>
              </div>

              <div className="flex items-center space-x-4">
                <div className="bg-emerald-600 p-3 rounded-full">
                  <Mail className="w-6 h-6" />
                </div>
                <div>
                  <h4 className="font-semibold">Email</h4>
                  <p className="text-gray-300">hello@matifood.com</p>
                </div>
              </div>

              <div className="flex items-center space-x-4">
                <div className="bg-emerald-600 p-3 rounded-full">
                  <MapPin className="w-6 h-6" />
                </div>
                <div>
                  <h4 className="font-semibold">Address</h4>
                  <p className="text-gray-300">
                    123 Organic Farm Road<br />
                    Natural Valley, CA 90210
                  </p>
                </div>
              </div>
            </div>
          </div>

          {/* Contact Form */}
          <div className="bg-gray-800 p-8 rounded-lg">
            <form onSubmit={handleSubmit} className="space-y-6">
              <div>
                <label htmlFor="name" className="block text-sm font-medium mb-2">
                  Name
                </label>
                <input
                  type="text"
                  id="name"
                  name="name"
                  value={formData.name}
                  onChange={handleChange}
                  required
                  className="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors duration-200"
                  placeholder="Your full name"
                />
              </div>

              <div>
                <label htmlFor="email" className="block text-sm font-medium mb-2">
                  Email *
                </label>
                <input
                  type="email"
                  id="email"
                  name="email"
                  value={formData.email}
                  onChange={handleChange}
                  required
                  className="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors duration-200"
                  placeholder="your.email@example.com"
                />
              </div>

              <div>
                <label htmlFor="message" className="block text-sm font-medium mb-2">
                  Message
                </label>
                <textarea
                  id="message"
                  name="message"
                  value={formData.message}
                  onChange={handleChange}
                  rows={5}
                  className="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition-colors duration-200 resize-none"
                  placeholder="Tell us how we can help you..."
                />
              </div>

              <div className="flex items-center space-x-3">
                <input
                  type="checkbox"
                  id="newsletter"
                  name="newsletter"
                  checked={formData.newsletter}
                  onChange={handleChange}
                  className="w-4 h-4 text-emerald-600 bg-gray-700 border-gray-600 rounded focus:ring-emerald-500 focus:ring-2"
                />
                <label htmlFor="newsletter" className="text-sm text-gray-300">
                  Sign up for our email list for updates, promotions, and more.
                </label>
              </div>

              <button
                type="submit"
                className="w-full bg-emerald-600 hover:bg-emerald-700 text-white py-3 px-6 rounded-md font-medium transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl"
              >
                Send Message
              </button>
            </form>

            <p className="text-xs text-gray-400 mt-4">
              This site is protected by reCAPTCHA and the Google{" "}
              <a href="#" className="text-emerald-400 hover:underline">Privacy Policy</a>{" "}
              and{" "}
              <a href="#" className="text-emerald-400 hover:underline">Terms of Service</a>{" "}
              apply.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ContactSection;