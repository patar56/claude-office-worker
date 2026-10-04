import { useEffect } from "react";
import { Link } from "react-router-dom";

export function About() {
  useEffect(() => {
    document.title = "About — Kinematic Watch Co.";
  }, []);

  return (
    <article className="page interior about">
      <header className="page-head">
        <p className="eyebrow">About</p>
        <h1>
          Advanced manufacture. <em>Traditional soul.</em>
        </h1>
      </header>

      <div className="about-lead">
        <img
          src="/images/about-wide.jpg"
          alt="Editorial portrait published on the Kinematic about page"
        />
        <p className="reveal">
          Kinematic is redefining modern American watchmaking by merging the most advanced manufacturing
          technologies with the precision and soul of traditional craftsmanship. Every timepiece begins as a
          meticulously engineered titanium form, created through state-of-the-art 3D printing processes that
          allow for geometries and performance characteristics impossible to achieve through conventional
          methods alone.
        </p>
      </div>

      <div className="about-split">
        <img
          src="/images/about.jpg"
          alt="Portrait published on the Kinematic about page"
        />
        <div>
          <p className="reveal">
            From there, each component is refined, fitted, and finished by hand using classic watchmaking
            tools and techniques, bridging digital precision and human artistry. This fusion is core to the
            mission: keep the spirit of American horology alive while pushing what a modern mechanical watch
            can be.
          </p>
          <p className="reveal">
            In a landscape where countless watch brands recycle the same familiar designs, or price their
            most interesting pieces far beyond reach, there is room for something genuinely new. Too often,
            originality is sacrificed for market trends, and true innovation becomes a luxury reserved only
            for the highest tiers of collectors.
          </p>
          <p className="reveal">
            At Kinematic, we’re challenging that norm by creating a watch that doesn’t imitate, but
            originates. By leveraging advanced manufacturing and designing from first principles, we can
            craft a timepiece that is visually striking, mechanically compelling, and unlike anything else
            on the market, while still maintaining a price that makes authentic innovation accessible.
          </p>
          <Link className="text-link" to="/watches/x7-ti">
            See the X7-Ti <span aria-hidden="true">→</span>
          </Link>
        </div>
      </div>

      <figure className="about-still">
        <img
          src="/images/movement.jpg"
          alt="Open-worked mechanical movement used in the Kinematic approach"
        />
        <figcaption>Movements selected from Japan, Switzerland, and the USA. Dials made in America.</figcaption>
      </figure>
    </article>
  );
}
