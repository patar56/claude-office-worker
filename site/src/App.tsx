import { Route, Routes } from "react-router-dom";
import { Layout } from "./components/Layout";
import { Home } from "./pages/Home";
import { Watches } from "./pages/Watches";
import { Watch } from "./pages/Watch";
import { About } from "./pages/About";
import { Contact } from "./pages/Contact";
import { Shipping } from "./pages/Shipping";

export default function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="watches" element={<Watches />} />
        <Route path="watches/x7-ti" element={<Watch />} />
        <Route path="about" element={<About />} />
        <Route path="contact" element={<Contact />} />
        <Route path="shipping" element={<Shipping />} />
      </Route>
    </Routes>
  );
}
