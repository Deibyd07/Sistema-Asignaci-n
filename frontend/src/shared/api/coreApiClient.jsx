import { extractApiError } from "../utils/extractApiError";

const apiBase = import.meta.env.VITE_API_URL ?? "http://127.0.0.1:8000";
export const coreApiBase = `${apiBase.replace(/\/$/, "")}/api/core`;

export async function coreApiRequest(path, options = {}) {
  const { method = "GET", token, body } = options;

  const response = await fetch(`${coreApiBase}${path}`, {
    method,
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: body ? JSON.stringify(body) : undefined,
  });

  if (response.status === 204) {
    return null;
  }

  const payload = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(extractApiError(payload));
  }

  return payload;
}
