import { useEffect } from "react";
import { Link } from "react-router-dom";

export function Shipping() {
  useEffect(() => {
    document.title = "Shipping and Returns — Kinematic Watch Co.";
  }, []);

  return (
    <article className="page interior shipping">
      <header className="page-head">
        <p className="eyebrow">Shipping and returns</p>
        <h1>
          Careful to send. <em>Fair to return.</em>
        </h1>
      </header>

      <div className="policy">
        <section className="reveal">
          <h2>Shipping & returns policy</h2>
          <p>
            At Kinematic we aim to ensure every customer has the best possible experience with our products.
            While all returns and exchanges are handled at our discretion, we are typically very flexible and
            always willing to work with you to find a solution that feels fair. If something isn’t right,
            reach out — we’ll do our best to make it right. Returns are not accepted after 30 days.
          </p>
        </section>
        <section className="reveal">
          <h2>Processing & shipping</h2>
          <p>
            Orders are processed as quickly as possible, and shipping times may vary based on product
            availability and destination. Once your order ships, you’ll receive tracking information so you
            can follow it every step of the way. U.S. customers receive free shipping and pay no sales tax.
          </p>
        </section>
        <section className="reveal">
          <h2>Returns</h2>
          <p>
            If you need to return or exchange an item, please contact us first. We review each request
            individually to determine the best course of action. Our goal is always to ensure you’re
            satisfied with your purchase, and we’ll work with you to resolve any issues.
          </p>
          <Link className="text-link" to="/contact">
            Contact us first <span aria-hidden="true">→</span>
          </Link>
        </section>
        <section className="reveal">
          <h2>International shipping</h2>
          <p>
            We do ship internationally. However, customers outside the United States are responsible for all
            shipping costs, including any customs fees, taxes, or duties charged by their country. Delivery
            times may vary based on international carriers and customs processing. We’re happy to assist with
            guidance, but all additional import-related costs fall to the customer.
          </p>
        </section>
      </div>
    </article>
  );
}
