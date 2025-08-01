import React from "react";
import { Leaf, Heart, Award } from "lucide-react";

const AboutSection = () => {
  const features = [
    {
      icon: <Leaf className="w-12 h-12 text-emerald-600" />,
      title: "100% Organic",
      description: "All our products are certified organic, grown without harmful pesticides or chemicals."
    },
    {
      icon: <Heart className="w-12 h-12 text-emerald-600" />,
      title: "Health Focused",
      description: "We prioritize your health with nutritious, natural ingredients that nourish your body."
    },
    {
      icon: <Award className="w-12 h-12 text-emerald-600" />,
      title: "Premium Quality",
      description: "Our commitment to excellence ensures only the finest quality products reach your table."
    }
  ];

  return (
    <section id="about" className="py-20 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-5xl font-serif font-light text-gray-800 mb-6">
            About Mati Food
          </h2>
          <p className="text-lg md:text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
            At Mati Food, we believe in the power of nature to nourish and heal. 
            Our journey began with a simple mission: to bring you the finest organic 
            and natural food products that honor both your health and the environment.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16">
          {features.map((feature, index) => (
            <div
              key={index}
              className="text-center p-8 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300"
            >
              <div className="flex justify-center mb-6">
                {feature.icon}
              </div>
              <h3 className="text-xl font-semibold text-gray-800 mb-4">
                {feature.title}
              </h3>
              <p className="text-gray-600 leading-relaxed">
                {feature.description}
              </p>
            </div>
          ))}
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div>
            <h3 className="text-2xl md:text-3xl font-serif font-light text-gray-800 mb-6">
              Our Story
            </h3>
            <p className="text-gray-600 mb-6 leading-relaxed">
              Founded on the principles of sustainability and wellness, Mati Food has been 
              dedicated to sourcing the highest quality organic ingredients from trusted 
              farmers and producers around the world.
            </p>
            <p className="text-gray-600 leading-relaxed">
              From our premium stimulants and plant growth regulators to our rich 
              micro nutrients and organic fertilizers, every product is carefully 
              selected to support both your health and the environment.
            </p>
          </div>
          <div className="relative">
            <img
              src="https://images.unsplash.com/photo-1590794056675-8354831935b2?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3MjQyMTd8MHwxfHNlYXJjaHwyfHxvcmdhbmljJTIwc291cCUyMGJvd2xzfGVufDB8fHx8MTc1NDA2MjQ3NHww&ixlib=rb-4.1.0&q=85"
              alt="Natural organic food"
              className="rounded-lg shadow-lg w-full h-80 object-cover"
            />
          </div>
        </div>
      </div>
    </section>
  );
};

export default AboutSection;