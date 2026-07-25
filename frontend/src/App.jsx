import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Dashboard from "./pages/Dashboard";
import StudentDetails from "./pages/StudentPage";

function App() {
  return (
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route
          path="/student/:admission_no"
          element={<StudentDetails />}
        />
      </Routes>
  );
}

export default App;