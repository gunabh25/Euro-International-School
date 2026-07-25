import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
});

export const getStudents = (search = "") =>
  api.get(`/students/?search=${search}`);

export const getStudent = (admission) =>
  api.get(`/students/${admission}/`);

export const getSummary = (admission) =>
  api.get(`/students/${admission}/summary/`);

export const correctMarks = (admission, data) =>
  api.post(`/students/${admission}/correct/`, data);

export default api;