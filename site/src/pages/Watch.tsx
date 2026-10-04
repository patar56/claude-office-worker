import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { Inquiry } from "../components/Inquiry";
import { productImages, serials, specs } from "../data";

export function Watch() {
  const [active, setActive] = useState(0);
  const [serial, setSerial] = useState(serials[0]);

  useEffect(() => {
    document.title = "Kinematic X7-Ti — Kinematic Watch Co.";
  }, []);

  const image = productImages[active];

  return (
    <article className="page interior watch">
      <p className="crumb">
        <Link to="/">Home</Link>
        <span aria-hidden="true">/</span>
        <Link to="/watches">Watch collection</Link>
        <span aria-hidden="true">/</span>
        X7-Ti
      </p>

      <div className="watch-layout">
        <div className="gallery">
          <figure>
            <img key={image.src} src={image.src} alt={image.alt} />
          </figure>
          <div className="thumbs" role="tablist" aria-label="X7-Ti views">
            {productImages.map((item, index) => (
              <button
                key={item.src}
                type="button"
                role="tab"
                aria-selected={index === active}
                onClick={() => setActive(index)}
              >
                <img src={item.src} alt="" />
              </button>
            ))}
          </div>
        </div>

        <div className="watch-copy">
          <p className="eyebrow">Ultra light titanium</p>
          <h1>
            Kinematic <em>X7-Ti</em>
          </h1>
          <p className="price">$2,980.64</p>
          <p>
            Engineered in ultra light titanium. Finished by hand. This is a watch built the way modern
            things should be made — designed, precision-machined, hand-finished, and assembled in the USA.
          </p>
          <p>
            The case is 3D-printed in aerospace-grade titanium, then meticulously hand-finished. Inside, a
            premium Japanese automatic skeleton movement, the Miyota 8N24, puts the mechanics on display.
          </p>

          <fieldset>
            <legend>Serial number</legend>
            <div className="serials">
              {serials.map((item) => (
                <button
                  key={item}
                  type="button"
                  aria-pressed={item === serial}
                  onClick={() => setSerial(item)}
                >
                  {item}
                </button>
              ))}
            </div>
          </fieldset>

          <p className="fine">
            These are prototype pieces. Because each case is hand-finished, expect subtle variation from
            piece to piece in the texture and brushwork: the mark of a watch made by people, not a
            production line.
          </p>
        </div>
      </div>

      <section className="spec-table">
        <header>
          <p className="eyebrow">Specifications</p>
          <h2>What the piece is.</h2>
        </header>
        <dl>
          {specs.map(([label, value]) => (
            <div key={label}>
              <dt>{label}</dt>
              <dd>{value}</dd>
            </div>
          ))}
        </dl>
        <p className="fine">
          Water resistance is pressure-tested to 185 ft and rated for 60 ft of actual use. Weight 2 lbs.
          Dimensions 6 × 12 × 6 in, packed.
        </p>
      </section>

      <section className="ask">
        <div>
          <p className="eyebrow">Request this serial</p>
          <h2>
            {serial}, held for a conversation.
          </h2>
          <p>
            Free shipping and no sales tax for U.S. customers. International orders ship as well; duties and
            customs sit with the recipient. Write Phil and name the serial.
          </p>
        </div>
        <Inquiry subject={`Kinematic X7-Ti — ${serial}`} detail={`Kinematic X7-Ti, ${serial}`} />
      </section>
    </article>
  );
}
