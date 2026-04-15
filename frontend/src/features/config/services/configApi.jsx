import { coreApiRequest } from "../../../shared/api/coreApiClient";

export function listPeriods(token) {
  return coreApiRequest("/config/periods/", { token });
}

export function createPeriod(token, payload) {
  return coreApiRequest("/config/periods/", {
    method: "POST",
    token,
    body: payload,
  });
}

export function updatePeriod(token, id, payload) {
  return coreApiRequest(`/config/periods/${id}/`, {
    method: "PATCH",
    token,
    body: payload,
  });
}

export function deletePeriod(token, id) {
  return coreApiRequest(`/config/periods/${id}/`, {
    method: "DELETE",
    token,
  });
}

export function listWorkingDays(token) {
  return coreApiRequest("/config/working-days/", { token });
}

export function createWorkingDay(token, payload) {
  return coreApiRequest("/config/working-days/", {
    method: "POST",
    token,
    body: payload,
  });
}

export function updateWorkingDay(token, id, payload) {
  return coreApiRequest(`/config/working-days/${id}/`, {
    method: "PATCH",
    token,
    body: payload,
  });
}

export function deleteWorkingDay(token, id) {
  return coreApiRequest(`/config/working-days/${id}/`, {
    method: "DELETE",
    token,
  });
}

export function listTimeSlots(token) {
  return coreApiRequest("/config/time-slots/", { token });
}

export function createTimeSlot(token, payload) {
  return coreApiRequest("/config/time-slots/", {
    method: "POST",
    token,
    body: payload,
  });
}

export function updateTimeSlot(token, id, payload) {
  return coreApiRequest(`/config/time-slots/${id}/`, {
    method: "PATCH",
    token,
    body: payload,
  });
}

export function deleteTimeSlot(token, id) {
  return coreApiRequest(`/config/time-slots/${id}/`, {
    method: "DELETE",
    token,
  });
}

export function listSpaceTypes(token) {
  return coreApiRequest("/config/space-types/", { token });
}

export function createSpaceType(token, payload) {
  return coreApiRequest("/config/space-types/", {
    method: "POST",
    token,
    body: payload,
  });
}

export function updateSpaceType(token, id, payload) {
  return coreApiRequest(`/config/space-types/${id}/`, {
    method: "PATCH",
    token,
    body: payload,
  });
}

export function deleteSpaceType(token, id) {
  return coreApiRequest(`/config/space-types/${id}/`, {
    method: "DELETE",
    token,
  });
}
