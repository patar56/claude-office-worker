import { useEffect } from "react";
import { NavLink, Outlet, useLocation } from "react-router-dom";
import { brand, nav } from "../data";

export function Layout() {
  const { pathname } = useLocation();

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [pathname]);

  useEffect(() => {
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const nodes = Array.from(document.querySelectorAll<HTMLElement>(".reveal"));
    if (reduce) {
      nodes.forEach((node) => node.classList.add("in"));
      return;
    }
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("in");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.18, rootMargin: "0px 0px -8% 0px" },
    );
    nodes.forEach((node) => observer.observe(node));
    return () => observer.disconnect();
  }, [pathname]);

  useEffect(() => {
    const bar = document.querySelector<HTMLElement>(".progress");
    if (!bar) return;
    const onScroll = () => {
      const height = document.documentElement.scrollHeight - window.innerHeight;
      const progress = height > 0 ? window.scrollY / height : 0;
      bar.style.transform = `scaleX(${progress})`;
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, [pathname]);

  return (
    <div className="shell">
      <a className="skip" href="#content">
        Skip to content
      </a>
      <div className="progress" aria-hidden="true" />
      <aside className="rail">
        <NavLink to="/" className="mark" end>
          <img src="/images/mark.png" alt="" width="36" height="42" />
          <span>
            Kinematic
            <small>Watch Co.</small>
          </span>
        </NavLink>
        <nav aria-label="Primary">
          {nav.map((item) => (
            <NavLink key={item.to} to={item.to} end={item.to === "/"}>
              {item.label}
            </NavLink>
          ))}
        </nav>
        <p className="rail-foot">
          Los Angeles
          <span>U.S. shipping, no sales tax</span>
        </p>
      </aside>
      <div className="stage" id="content">
        <Outlet />
        <footer className="colophon">
          <div>
            <p className="eyebrow">Kinematic Watch Co.</p>
            <p className="colophon-line">{brand.place}</p>
          </div>
          <div>
            <a href={`mailto:${brand.email}`}>{brand.email}</a>
            <p>Instagram DM</p>
          </div>
          <p>{brand.note}</p>
        </footer>
      </div>
    </div>
  );
}
