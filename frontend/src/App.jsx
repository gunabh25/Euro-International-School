import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import StudentDetails from "./pages/StudentDetails";
import Dashboard from "./pages/Dashboard";

function App() {
    return (
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/student/:admissionNo" element={<StudentDetails />} />
            <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
    );
}

export default App;