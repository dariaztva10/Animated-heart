import React from "react";
import "../static/style.css";

const Footer = () => {
  const currentYear = new Date().getFullYear();
  
  return (
    <footer className="footer">
      <p>© {currentYear} Hecho con mucho amor💘 - Daria.</p>
      <p><small>(No alcancé a comprar las flores)</small></p>
    </footer>
  );
};

export default Footer;
