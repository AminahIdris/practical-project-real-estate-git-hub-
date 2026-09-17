import { Routes, Route, Link } from "react-router-dom";

/**
 * Placeholder application shell.
 * Future screens (per TECHNICAL_SPEC):
 * - Customer enquiry / chat
 * - Sales login
 * - Lead list
 * - Lead detail
 * - Conversation view
 * - Qualification display
 * - Follow-ups
 */
function App() {
  return (
    <div style={{ fontFamily: "system-ui, sans-serif", padding: "2rem", maxWidth: 800, margin: "0 auto" }}>
      <header style={{ marginBottom: "2rem" }}>
        <h1>Real Estate Lead Management</h1>
        <p style={{ color: "#555" }}>MVP scaffold – frontend structure ready</p>
        <nav style={{ display: "flex", gap: "1rem", marginTop: "1rem" }}>
          <Link to="/">Home</Link>
          <Link to="/enquiry">Customer Enquiry</Link>
          <Link to="/sales">Sales Dashboard</Link>
        </nav>
      </header>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/enquiry" element={<Placeholder title="Customer Enquiry / Chat" />} />
        <Route path="/sales" element={<Placeholder title="Sales Dashboard (Login → Leads)" />} />
      </Routes>
    </div>
  );
}

function Home() {
  return (
    <section>
      <h2>Welcome</h2>
      <p>
        This is the React frontend scaffold for the Real Estate Lead Management &amp; AI
        Qualification System.
      </p>
      <ul>
        <li>Customer can submit enquiries</li>
        <li>Sales team can view, qualify and follow up on leads</li>
        <li>Backend: FastAPI + PostgreSQL + n8n</li>
      </ul>
    </section>
  );
}

function Placeholder({ title }: { title: string }) {
  return (
    <section>
      <h2>{title}</h2>
      <p style={{ color: "#888" }}>Component to be implemented in a later phase.</p>
    </section>
  );
}

export default App;
