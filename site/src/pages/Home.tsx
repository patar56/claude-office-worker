import { Link } from "react-router-dom";
import { chapters, practice } from "../data";
import { useEffect } from "react";

export function Home() {
  useEffect(() => {
    document.title = "Kinematic Watch Co.";
  }, []);

  return (
    <article className="page">
      <section className="hero">
        <div className="hero-copy">
          <p className="eyebrow">Always original</p>
          <h1>
            Next-gen
            <br />
            3D printed
            <br />
            <em>titanium</em> watches
          </h1>
          <p className="lede">
            All precision machining and assembly are completed in the USA. Japanese sapphire, movements
            from Japan, Switzerland, and the USA, and dials crafted entirely in America.
          </p>
          <div className="hero-actions">
            <Link className="text-link" to="/watches/x7-ti">
              The X7-Ti <span aria-hidden="true">→</span>
            </Link>
            <Link className="text-link quiet" to="/about">
              The manufacture <span aria-hidden="true">→</span>
            </Link>
          </div>
        </div>
        <figure className="hero-media">
          <img
            src="/images/hero.jpg"
            alt="Titanium Kinematic wristwatch worn on the wrist"
          />
          <figcaption>Kinematic Watch Company USA</figcaption>
        </figure>
      </section>

      <section className="manifesto">
        <p className="eyebrow reveal">A first encounter</p>
        <blockquote className="reveal">
          Congratulations on discovering <em>Kinematic Watch Co.</em>
        </blockquote>
        <div className="manifesto-grid">
          <p className="reveal">
            3D printed titanium. Each dial is fully crafted in the USA, with meticulous attention at every
            step of production. Premium sapphire glass from Japan. Movement options chosen for the long run.
          </p>
          <p className="reveal">
            Kinematic is dedicated to reviving the spirit of American watchmaking through modern engineering,
            advanced machining, and precision craftsmanship.
          </p>
        </div>
      </section>

      <section className="chapters">
        {chapters.map((chapter) => (
          <article className="chapter reveal" key={chapter.index}>
            <span>{chapter.index}</span>
            <h2>{chapter.title}</h2>
            <p>{chapter.body}</p>
          </article>
        ))}
      </section>

      <section className="bleed">
        <img
          src="/images/case.jpg"
          alt="3D-printed titanium watch case with an open lattice"
        />
        <div className="bleed-copy reveal">
          <p className="eyebrow">Printed, then finished</p>
          <h2>Geometry a mill cannot cut.</h2>
          <p>
            The case is 3D-printed in aerospace-grade titanium, then meticulously hand-finished. Additive
            manufacturing lets us build form that is sculptural, structural, and lighter on the wrist than
            anything comparable in steel.
          </p>
        </div>
      </section>

      <section className="feature">
        <div className="feature-copy">
          <p className="eyebrow reveal">The collection</p>
          <h2 className="reveal">
            Kinematic <em>X7-Ti</em>
          </h2>
          <p className="reveal">
            Engineered in ultra light titanium. Finished by hand. A prototype series, each case carrying the
            variation of brushwork that only a person leaves behind.
          </p>
          <dl className="spec-row reveal">
            <div>
              <dt>Case</dt>
              <dd>41 mm</dd>
            </div>
            <div>
              <dt>Height</dt>
              <dd>11.3 mm</dd>
            </div>
            <div>
              <dt>Movement</dt>
              <dd>Miyota 8N24</dd>
            </div>
            <div>
              <dt>Price</dt>
              <dd>$2,980.64</dd>
            </div>
          </dl>
          <Link className="text-link reveal" to="/watches/x7-ti">
            Study the piece <span aria-hidden="true">→</span>
          </Link>
        </div>
        <Link className="feature-shot" to="/watches/x7-ti" aria-label="Open the Kinematic X7-Ti">
          <img src="/images/x7-2.jpg" alt="" />
        </Link>
      </section>

      <section className="practice">
        <header className="reveal">
          <p className="eyebrow">How it is made</p>
          <h2>Watchmaking, from the ground up.</h2>
        </header>
        <ol>
          {practice.map((item, index) => (
            <li className="reveal" key={item.title}>
              <span>0{index + 1}</span>
              <div>
                <h3>{item.title}</h3>
                <p>{item.body}</p>
              </div>
            </li>
          ))}
        </ol>
      </section>

      <section className="close">
        <img src="/images/motion.jpg" alt="Titanium Kinematic watch on the wrist, side view" />
        <div className="reveal">
          <p className="eyebrow">Los Angeles</p>
          <h2>For those who care how things are made.</h2>
          <Link className="text-link" to="/contact">
            Write to Phil <span aria-hidden="true">→</span>
          </Link>
        </div>
      </section>
    </article>
  );
}
