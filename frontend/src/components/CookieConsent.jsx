import React from "react";
import { X } from "lucide-react";

const CookieConsent = ({ onAccept }) => {
  return (
    <div className="fixed bottom-4 right-4 max-w-sm bg-white border border-gray-200 rounded-lg shadow-lg p-6 z-50 animate-slide-up">
      <div className="flex items-start justify-between mb-4">
        <h4 className="text-lg font-semibold text-gray-800">
          This website uses cookies.
        </h4>
        <button
          onClick={onAccept}
          className="text-gray-400 hover:text-gray-600 transition-colors duration-200"
        >
          <X size={20} />
        </button>
      </div>
      
      <p className="text-sm text-gray-600 mb-4 leading-relaxed">
        We use cookies to analyze website traffic and optimize your website experience. 
        By accepting our use of cookies, your data will be aggregated with all other user data.
      </p>
      
      <button
        onClick={onAccept}
        className="w-full bg-gray-800 hover:bg-gray-900 text-white py-2 px-4 rounded-md font-medium transition-colors duration-200"
      >
        ACCEPT
      </button>
    </div>
  );
};

export default CookieConsent;