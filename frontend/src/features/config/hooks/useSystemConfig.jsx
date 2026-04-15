import { useEffect, useState } from "react";

import {
  createPeriod,
  createSpaceType,
  createTimeSlot,
  createWorkingDay,
  deletePeriod,
  deleteSpaceType,
  deleteTimeSlot,
  deleteWorkingDay,
  listPeriods,
  listSpaceTypes,
  listTimeSlots,
  listWorkingDays,
  updatePeriod,
  updateSpaceType,
  updateTimeSlot,
  updateWorkingDay,
} from "../services/configApi";

const RESOURCE_CONFIG = {
  periods: {
    list: listPeriods,
    create: createPeriod,
    update: updatePeriod,
    remove: deletePeriod,
    defaultForm: {
      code: "",
      name: "",
      start_date: "",
      end_date: "",
      is_active: true,
    },
    fieldOrder: ["code", "name", "start_date", "end_date", "is_active"],
  },
  workingDays: {
    list: listWorkingDays,
    create: createWorkingDay,
    update: updateWorkingDay,
    remove: deleteWorkingDay,
    defaultForm: {
      day_of_week: "",
      name: "",
      is_active: true,
    },
    fieldOrder: ["day_of_week", "name", "is_active"],
  },
  timeSlots: {
    list: listTimeSlots,
    create: createTimeSlot,
    update: updateTimeSlot,
    remove: deleteTimeSlot,
    defaultForm: {
      name: "",
      start_time: "",
      end_time: "",
      is_active: true,
    },
    fieldOrder: ["name", "start_time", "end_time", "is_active"],
  },
  spaceTypes: {
    list: listSpaceTypes,
    create: createSpaceType,
    update: updateSpaceType,
    remove: deleteSpaceType,
    defaultForm: {
      name: "",
      description: "",
      is_active: true,
    },
    fieldOrder: ["name", "description", "is_active"],
  },
};

function buildInitialState() {
  return {
    periods: {
      items: [],
      form: { ...RESOURCE_CONFIG.periods.defaultForm },
      editId: null,
      loading: false,
      submitting: false,
      error: "",
    },
    workingDays: {
      items: [],
      form: { ...RESOURCE_CONFIG.workingDays.defaultForm },
      editId: null,
      loading: false,
      submitting: false,
      error: "",
    },
    timeSlots: {
      items: [],
      form: { ...RESOURCE_CONFIG.timeSlots.defaultForm },
      editId: null,
      loading: false,
      submitting: false,
      error: "",
    },
    spaceTypes: {
      items: [],
      form: { ...RESOURCE_CONFIG.spaceTypes.defaultForm },
      editId: null,
      loading: false,
      submitting: false,
      error: "",
    },
  };
}

function normalizePayload(resourceKey, form) {
  if (resourceKey === "workingDays") {
    return {
      ...form,
      day_of_week: Number(form.day_of_week),
    };
  }

  return form;
}

function mapItemToForm(resourceKey, item) {
  const fields = RESOURCE_CONFIG[resourceKey].fieldOrder;
  const form = {};

  fields.forEach((fieldName) => {
    form[fieldName] = item[fieldName];
  });

  if (resourceKey === "workingDays") {
    form.day_of_week = String(item.day_of_week);
  }

  return form;
}

export function useSystemConfig({ authToken, enabled }) {
  const [state, setState] = useState(buildInitialState());

  const setResourceState = (resourceKey, updater) => {
    setState((previous) => ({
      ...previous,
      [resourceKey]: updater(previous[resourceKey]),
    }));
  };

  const resetResourceForm = (resourceKey) => {
    setResourceState(resourceKey, (resourceState) => ({
      ...resourceState,
      editId: null,
      form: { ...RESOURCE_CONFIG[resourceKey].defaultForm },
      submitting: false,
      error: "",
    }));
  };

  const loadResource = async (resourceKey) => {
    if (!authToken) {
      return;
    }

    const resourceApi = RESOURCE_CONFIG[resourceKey];

    setResourceState(resourceKey, (resourceState) => ({
      ...resourceState,
      loading: true,
      error: "",
    }));

    try {
      const items = await resourceApi.list(authToken);
      setResourceState(resourceKey, (resourceState) => ({
        ...resourceState,
        items,
        loading: false,
      }));
    } catch (error) {
      setResourceState(resourceKey, (resourceState) => ({
        ...resourceState,
        loading: false,
        error: error.message || "No fue posible cargar la configuracion.",
      }));
    }
  };

  const refreshAll = async () => {
    await Promise.all(Object.keys(RESOURCE_CONFIG).map((key) => loadResource(key)));
  };

  useEffect(() => {
    if (!enabled) {
      return;
    }

    refreshAll();
  }, [authToken, enabled]);

  const handleFieldChange = (resourceKey, field, value) => {
    setResourceState(resourceKey, (resourceState) => ({
      ...resourceState,
      form: {
        ...resourceState.form,
        [field]: value,
      },
    }));
  };

  const handleSelectEdit = (resourceKey, item) => {
    setResourceState(resourceKey, (resourceState) => ({
      ...resourceState,
      editId: item.id,
      form: mapItemToForm(resourceKey, item),
      error: "",
    }));
  };

  const handleDelete = async (resourceKey, itemId) => {
    if (!authToken) {
      return;
    }

    const approved = window.confirm("Deseas eliminar este registro?");
    if (!approved) {
      return;
    }

    const resourceApi = RESOURCE_CONFIG[resourceKey];

    try {
      await resourceApi.remove(authToken, itemId);
      await loadResource(resourceKey);

      setResourceState(resourceKey, (resourceState) => {
        if (resourceState.editId !== itemId) {
          return resourceState;
        }

        return {
          ...resourceState,
          editId: null,
          form: { ...resourceApi.defaultForm },
        };
      });
    } catch (error) {
      setResourceState(resourceKey, (resourceState) => ({
        ...resourceState,
        error: error.message || "No fue posible eliminar el registro.",
      }));
    }
  };

  const handleSubmit = async (resourceKey, event) => {
    event.preventDefault();
    if (!authToken) {
      return;
    }

    const resourceApi = RESOURCE_CONFIG[resourceKey];
    const resourceStateSnapshot = state[resourceKey];

    setResourceState(resourceKey, (resourceState) => ({
      ...resourceState,
      submitting: true,
      error: "",
    }));

    const payload = normalizePayload(resourceKey, resourceStateSnapshot.form);

    try {
      if (resourceStateSnapshot.editId) {
        await resourceApi.update(authToken, resourceStateSnapshot.editId, payload);
      } else {
        await resourceApi.create(authToken, payload);
      }

      await loadResource(resourceKey);
      resetResourceForm(resourceKey);
    } catch (error) {
      setResourceState(resourceKey, (resourceState) => ({
        ...resourceState,
        submitting: false,
        error: error.message || "No fue posible guardar el registro.",
      }));
      return;
    }

    setResourceState(resourceKey, (resourceState) => ({
      ...resourceState,
      submitting: false,
    }));
  };

  return {
    configState: state,
    refreshAll,
    handleFieldChange,
    handleSelectEdit,
    handleDelete,
    handleSubmit,
    resetResourceForm,
  };
}
