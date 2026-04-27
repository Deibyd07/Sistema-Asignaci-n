import { useEffect, useState } from "react";

import {
  createAcademicProgram,
  createPeriod,
  createSubject,
  createSubjectGroup,
  createSubjectOffering,
  createSpaceType,
  createTimeSlot,
  createWorkingDay,
  deleteAcademicProgram,
  deletePeriod,
  deleteSubject,
  deleteSubjectGroup,
  deleteSubjectOffering,
  deleteSpaceType,
  deleteTimeSlot,
  deleteWorkingDay,
  listAcademicPrograms,
  listPeriods,
  listSubjects,
  listSubjectGroups,
  listSubjectOfferings,
  listSpaceTypes,
  listTimeSlots,
  listWorkingDays,
  updateAcademicProgram,
  updatePeriod,
  updateSubject,
  updateSubjectGroup,
  updateSubjectOffering,
  updateSpaceType,
  updateTimeSlot,
  updateWorkingDay,
} from "../services/configApi";

const RESOURCE_CONFIG = {
  academicPrograms: {
    list: listAcademicPrograms,
    create: createAcademicProgram,
    update: updateAcademicProgram,
    remove: deleteAcademicProgram,
    defaultForm: {
      code: "",
      name: "",
      is_active: true,
    },
    fieldOrder: ["code", "name", "is_active"],
  },
  subjects: {
    list: listSubjects,
    create: createSubject,
    update: updateSubject,
    remove: deleteSubject,
    defaultForm: {
      code: "",
      name: "",
      class_type: "presencial",
      credits: "",
      weekly_hours: "",
      capacity: "",
      is_active: true,
    },
    fieldOrder: [
      "code",
      "name",
      "class_type",
      "credits",
      "weekly_hours",
      "capacity",
      "is_active",
    ],
  },
  subjectGroups: {
    list: listSubjectGroups,
    create: createSubjectGroup,
    update: updateSubjectGroup,
    remove: deleteSubjectGroup,
    defaultForm: {
      subject_id: "",
      identifier: "",
      is_active: true,
    },
    fieldOrder: ["subject_id", "identifier", "is_active"],
  },
  subjectOfferings: {
    list: listSubjectOfferings,
    create: createSubjectOffering,
    update: updateSubjectOffering,
    remove: deleteSubjectOffering,
    defaultForm: {
      subject_id: "",
      subject_group_id: "",
      academic_program_id: "",
      semester: "",
      is_active: true,
    },
    fieldOrder: ["subject_id", "subject_group_id", "academic_program_id", "semester", "is_active"],
  },
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
    academicPrograms: {
      items: [],
      form: { ...RESOURCE_CONFIG.academicPrograms.defaultForm },
      editId: null,
      loading: false,
      submitting: false,
      error: "",
    },
    subjects: {
      items: [],
      form: { ...RESOURCE_CONFIG.subjects.defaultForm },
      editId: null,
      loading: false,
      submitting: false,
      error: "",
    },
    subjectGroups: {
      items: [],
      form: { ...RESOURCE_CONFIG.subjectGroups.defaultForm },
      editId: null,
      loading: false,
      submitting: false,
      error: "",
    },
    subjectOfferings: {
      items: [],
      form: { ...RESOURCE_CONFIG.subjectOfferings.defaultForm },
      editId: null,
      loading: false,
      submitting: false,
      error: "",
    },
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

  if (resourceKey === "subjectOfferings") {
    return {
      ...form,
      subject_id: Number(form.subject_id),
      subject_group_id: Number(form.subject_group_id),
      academic_program_id: Number(form.academic_program_id),
      semester: Number(form.semester),
    };
  }

  if (resourceKey === "subjectGroups") {
    return {
      ...form,
      subject_id: Number(form.subject_id),
    };
  }

  if (resourceKey === "subjects") {
    return {
      ...form,
      credits: Number(form.credits),
      weekly_hours: Number(form.weekly_hours),
      capacity: Number(form.capacity),
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

  if (resourceKey === "subjectOfferings") {
    form.subject_id = String(item.subject?.id ?? item.subject_id ?? "");
    form.subject_group_id = String(item.subject_group?.id ?? item.subject_group_id ?? "");
    form.academic_program_id = String(
      item.academic_program?.id ?? item.academic_program_id ?? "",
    );
    form.semester = String(item.semester);
  }

  if (resourceKey === "subjectGroups") {
    form.subject_id = String(item.subject?.id ?? item.subject_id ?? "");
  }

  if (resourceKey === "subjects") {
    form.credits = String(item.credits);
    form.weekly_hours = String(item.weekly_hours);
    form.capacity = String(item.capacity);
  }

  return form;
}

export function useSystemConfig({ authToken, enabled, role }) {
  const [state, setState] = useState(buildInitialState());

  const getResourceKeysForRole = (role) => {
    if (role === "coordinador") {
      return ["subjectOfferings", "subjects", "subjectGroups", "academicPrograms"];
    }

    return Object.keys(RESOURCE_CONFIG);
  };

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

  const refreshAll = async (activeRole) => {
    const keys = getResourceKeysForRole(activeRole);
    await Promise.all(keys.map((key) => loadResource(key)));
  };

  useEffect(() => {
    if (!enabled) {
      return;
    }

    refreshAll(role);
  }, [authToken, enabled, role]);

  const handleFieldChange = (resourceKey, field, value) => {
    if (resourceKey === "subjectOfferings" && field === "subject_id") {
      setResourceState(resourceKey, (resourceState) => ({
        ...resourceState,
        form: {
          ...resourceState.form,
          subject_id: value,
          subject_group_id: "",
        },
      }));
      return;
    }

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
    refreshAll: () => refreshAll(role),
    handleFieldChange,
    handleSelectEdit,
    handleDelete,
    handleSubmit,
    resetResourceForm,
  };
}
