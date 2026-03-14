const apiUrl = import.meta.env.VITE_API_URL ?? "http://127.0.0.1:8000";

function App() {
  return (
    <main className="app-shell">
      <section className="hero-card">
        <p className="eyebrow">Arquitectura inicial</p>
        <h1>Sistema de asignacion de salones</h1>
        <p className="lead">
          Frontend en React, backend en Django y Supabase como base de datos
          PostgreSQL administrada.
        </p>

        <div className="stack-grid">
          <article>
            <span>Frontend</span>
            <strong>React + Vite</strong>
          </article>
          <article>
            <span>Backend</span>
            <strong>Django API-first</strong>
          </article>
          <article>
            <span>Base de datos</span>
            <strong>Supabase PostgreSQL</strong>
          </article>
        </div>

        <div className="api-box">
          <span>API base esperada</span>
          <code>{apiUrl}</code>
        </div>
      </section>
    </main>
  );
}

export default App;
