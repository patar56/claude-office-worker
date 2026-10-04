import { useEffect } from "react";
import { Link } from "react-router-dom";
import { serials } from "../data";

export function Watches() {
  useEffect(() => {
    document.title = "Watches — Kinematic Watch Co.";
  }, []);

  return (
    <article className="page interior">
      <header className="page-head">
        <p className="eyebrow">Watch collection</p>
        <h1>
          One piece. <em>Ten serials.</em>
        </h1>
        <p className="lede">
          Shop the latest release and the pre-order exclusives of Kinematic Watch Co. The X7-Ti is the
          current titanium timepiece: printed, machined, and assembled in the USA.
        </p>
      </header>

      <Link className="catalogue" to="/watches/x7-ti">
        <figure>
          <img src="/images/x7-1.jpg" alt="Kinematic X7-Ti" />
        </figure>
        <div>
          <p className="eyebrow">Prototype series</p>
          <h2>Kinematic X7-Ti</h2>
          <p>
            Aerospace-grade 3D-printed titanium, a Japanese automatic skeleton movement, and a dial made in
            the USA. Hand-finished, piece by piece.
          </p>
          <dl>
            <div>
              <dt>Price</dt>
              <dd>$2,980.64</dd>
            </div>
            <div>
              <dt>Serials offered</dt>
              <dd>{serials.join(" · ")}</dd>
            </div>
          </dl>
          <span className="text-link">
            Select a serial <span aria-hidden="true">→</span>
          </span>
        </div>
      </Link>

      <section className="strip">
        <img src="/images/x7-5.jpg" alt="Kinematic X7-Ti worn on the wrist" />
        <img src="/images/x7-3.jpg" alt="Close view of the printed titanium case" />
        <img src="/images/x7-4.jpg" alt="Skeleton dial of the Kinematic X7-Ti" />
      </section>
    </article>
  );
}
