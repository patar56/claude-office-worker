import { FormEvent, useState } from "react";
import { brand } from "../data";

type Props = {
  subject: string;
  detail?: string;
};

export function Inquiry({ subject, detail }: Props) {
  const [ready, setReady] = useState<string | null>(null);

  function onSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const name = String(data.get("name") || "").trim();
    const email = String(data.get("email") || "").trim();
    const message = String(data.get("message") || "").trim();
    const body = [`Name: ${name}`, `Email: ${email}`, detail ? `Piece: ${detail}` : "", "", message]
      .filter((line) => line !== "")
      .join("\n");
    const href = `mailto:${brand.email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    setReady(href);
  }

  if (ready) {
    return (
      <div className="inquiry-ready" role="status">
        <p className="eyebrow">Composed</p>
        <h3>Your note is ready for {brand.email}.</h3>
        <p>Nothing is sent until you open the email. We read every message from Los Angeles.</p>
        <a className="text-link" href={ready}>
          Open email <span aria-hidden="true">→</span>
        </a>
      </div>
    );
  }

  return (
    <form className="inquiry" onSubmit={onSubmit}>
      <label>
        Name
        <input name="name" required autoComplete="name" />
      </label>
      <label>
        Email
        <input name="email" type="email" required autoComplete="email" />
      </label>
      <label>
        Message
        <textarea name="message" required rows={5} />
      </label>
      <button className="text-link" type="submit">
        Compose email <span aria-hidden="true">→</span>
      </button>
    </form>
  );
}
