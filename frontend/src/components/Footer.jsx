import React from "react";

const Footer = () => {
  return (
    <footer className="bg-black text-white py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          <p className="text-sm text-gray-400">
            Copyright © 2025 Mati Food - All Rights Reserved.
          </p>
          <div className="mt-4">
            <p className="text-xs text-gray-500">
              Powered by{" "}
              <a
                href="https://emergent.sh"
                target="_blank"
                rel="noopener noreferrer"
                className="text-emerald-400 hover:underline"
              >
                Emergent
              </a>
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;