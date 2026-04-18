const SECTION_DEFINITIONS = {
  periods: {
    title: "Periodos academicos",
    fields: [
      { name: "code", label: "Codigo", type: "text", required: true },
      { name: "name", label: "Nombre", type: "text", required: true },
      { name: "start_date", label: "Fecha inicio", type: "date", required: true },
      { name: "end_date", label: "Fecha fin", type: "date", required: true },
      { name: "is_active", label: "Activo", type: "checkbox", required: false },
    ],
  },
  workingDays: {
    title: "Dias laborables",
    fields: [
      {
        name: "day_of_week",
        label: "Dia (1-7)",
        type: "number",
        min: 1,
        max: 7,
        required: true,
      },
      { name: "name", label: "Nombre", type: "text", required: true },
      { name: "is_active", label: "Activo", type: "checkbox", required: false },
    ],
  },
  timeSlots: {
    title: "Franjas horarias",
    fields: [
      { name: "name", label: "Nombre", type: "text", required: true },
      { name: "start_time", label: "Hora inicio", type: "time", required: true },
      { name: "end_time", label: "Hora fin", type: "time", required: true },
      { name: "is_active", label: "Activo", type: "checkbox", required: false },
    ],
  },
  spaceTypes: {
    title: "Tipos de espacio",
    fields: [
      { name: "name", label: "Nombre", type: "text", required: true },
      { name: "description", label: "Descripcion", type: "text", required: false },
      { name: "is_active", label: "Activo", type: "checkbox", required: false },
    ],
  },
};

function ConfigSectionCard({
  sectionKey,
  title,
  sectionState,
  fields,
  onFieldChange,
  onSubmit,
  onEdit,
  onDelete,
  onCancel,
}) {
  return (
    <article className="card-block config-card">
      <h2>{title}</h2>

      <form className="form-grid" onSubmit={(event) => onSubmit(sectionKey, event)}>
        {fields.map((field) => {
          if (field.type === "checkbox") {
            return (
              <label key={field.name} className="checkbox-row">
                <input
                  type="checkbox"
                  checked={Boolean(sectionState.form[field.name])}
                  onChange={(event) =>
                    onFieldChange(sectionKey, field.name, event.target.checked)
                  }
                />
                {field.label}
              </label>
            );
          }

          return (
            <label key={field.name}>
              {field.label}
              <input
                type={field.type}
                value={sectionState.form[field.name] ?? ""}
                required={field.required}
                min={field.min}
                max={field.max}
                onChange={(event) =>
                  onFieldChange(sectionKey, field.name, event.target.value)
                }
              />
            </label>
          );
        })}

        {sectionState.error ? <p className="error-text">{sectionState.error}</p> : null}

        <div className="actions-inline">
          <button type="submit" disabled={sectionState.submitting}>
            {sectionState.submitting
              ? "Guardando..."
              : sectionState.editId
                ? "Guardar cambios"
                : "Crear"}
          </button>

          {sectionState.editId ? (
            <button type="button" className="secondary" onClick={() => onCancel(sectionKey)}>
              Cancelar
            </button>
          ) : null}
        </div>
      </form>

      <div className="config-items-list">
        {sectionState.loading ? <p className="hint">Cargando...</p> : null}
        {sectionState.items.map((item) => (
          <div key={item.id} className="config-item-row">
            <div>
              <strong>{item.name || item.code || `Registro ${item.id}`}</strong>
              <p className="hint small">{buildItemSummary(sectionKey, item)}</p>
            </div>
            <div className="actions-inline compact">
              <button className="secondary" type="button" onClick={() => onEdit(sectionKey, item)}>
                Editar
              </button>
              <button className="danger" type="button" onClick={() => onDelete(sectionKey, item.id)}>
                Eliminar
              </button>
            </div>
          </div>
        ))}
      </div>
    </article>
  );
}

function buildItemSummary(sectionKey, item) {
  if (sectionKey === "periods") {
    return `${item.code} | ${item.start_date} a ${item.end_date}`;
  }

  if (sectionKey === "workingDays") {
    return `Dia ${item.day_of_week} | ${item.is_active ? "Activo" : "Inactivo"}`;
  }

  if (sectionKey === "timeSlots") {
    return `${item.start_time} - ${item.end_time}`;
  }

  if (sectionKey === "spaceTypes") {
    return item.description || "Sin descripcion";
  }

  return "";
}

export function SystemConfigPanel({
  configState,
  onRefresh,
  onFieldChange,
  onSubmit,
  onEdit,
  onDelete,
  onCancel,
}) {
  return (
    <section className="card-block system-config-panel">
      <header className="dashboard-header config-header">
        <div>
          <p className="eyebrow"></p>
          <h2>Configuracion general del sistema</h2>
        </div>
        <button className="secondary" onClick={onRefresh}>
          Recargar configuracion
        </button>
      </header>

      <div className="config-grid">
        {Object.entries(SECTION_DEFINITIONS).map(([sectionKey, sectionDefinition]) => (
          <ConfigSectionCard
            key={sectionKey}
            sectionKey={sectionKey}
            title={sectionDefinition.title}
            sectionState={configState[sectionKey]}
            fields={sectionDefinition.fields}
            onFieldChange={onFieldChange}
            onSubmit={onSubmit}
            onEdit={onEdit}
            onDelete={onDelete}
            onCancel={onCancel}
          />
        ))}
      </div>
    </section>
  );
}
