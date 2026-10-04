import { useEffect } from "react";
import { Inquiry } from "../components/Inquiry";
import { brand } from "../data";

export function Contact() {
  useEffect(() => {
    document.title = "Contact — Kinematic Watch Co.";
  }, []);

  return (
    <article className="page interior contact">
      <header className="page-head">
        <p className="eyebrow">Contact us</p>
        <h1>
          Los Angeles. <em>Write directly.</em>
        </h1>
        <p className="lede">
          Kinematic Watch Co. reads its own mail. For a serial, a question about manufacture, or a return
          inside thirty days, start here.
        </p>
      </header>

      <div className="contact-grid">
        <ul className="facts">
          <li>
            <span>Email</span>
            <a href={`mailto:${brand.email}`}>{brand.email}</a>
          </li>
          <li>
            <span>Instagram</span>
            <strong>DM</strong>
          </li>
          <li>
            <span>Studio</span>
            <strong>Los Angeles, California</strong>
          </li>
          <li>
            <span>U.S. orders</span>
            <strong>Free shipping, no sales tax</strong>
          </li>
        </ul>
        <Inquiry subject="Hello from the Kinematic site" />
      </div>

      <figure className="contact-still">
        <img src="/images/x7-5.jpg" alt="Kinematic X7-Ti on the wrist" />
      </figure>
    </article>
  );
}
