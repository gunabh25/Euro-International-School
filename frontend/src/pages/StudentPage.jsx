import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { getStudent } from "../services/api";

function StudentPage() {
  const { admissionNo } = useParams();
  const navigate = useNavigate();

  const [student, setStudent] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function fetchStudent() {
      try {
        const response = await getStudent(admissionNo);

        // axios returns { data: ... }
        setStudent(response.data);
      } catch (err) {
        console.error(err);
        setError("Unable to load student.");
      } finally {
        setLoading(false);
      }
    }

    fetchStudent();
  }, [admissionNo]);

  if (loading) {
    return (
      <div className="max-w-6xl mx-auto p-8">
        <h1 className="text-3xl font-bold">Loading...</h1>
      </div>
    );
  }

  if (error || !student) {
    return (
      <div className="max-w-6xl mx-auto p-8">
        <h1 className="text-3xl font-bold text-red-600">
          {error || "Student not found"}
        </h1>

        <button
          onClick={() => navigate("/")}
          className="mt-6 bg-blue-600 text-white px-5 py-2 rounded-lg"
        >
          Back
        </button>
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto p-8">

      <button
        onClick={() => navigate("/")}
        className="mb-6 bg-gray-800 text-white px-4 py-2 rounded-lg hover:bg-gray-700"
      >
        ← Back
      </button>

      <div className="bg-white shadow-lg rounded-xl p-8">

        <h1 className="text-4xl font-bold">
          {student.name}
        </h1>

        <p className="text-gray-600 mt-2">
          Admission No: {student.admission_no}
        </p>

        <div className="grid grid-cols-3 gap-4 mt-8">

          <div className="bg-blue-50 rounded-lg p-5">
            <p className="text-gray-500">Class</p>
            <h2 className="text-2xl font-bold">
              {student.student_class}
            </h2>
          </div>

          <div className="bg-green-50 rounded-lg p-5">
            <p className="text-gray-500">Section</p>
            <h2 className="text-2xl font-bold">
              {student.section}
            </h2>
          </div>

          <div className="bg-yellow-50 rounded-lg p-5">
            <p className="text-gray-500">Average</p>
            <h2 className="text-2xl font-bold">
              {student.average}
            </h2>
          </div>

        </div>

        <h2 className="text-2xl font-semibold mt-10 mb-4">
          Subject Marks
        </h2>

        <table className="w-full border">

          <thead className="bg-blue-600 text-white">

            <tr>
              <th className="p-3">Subject</th>
              <th className="p-3">Marks</th>
              <th className="p-3">Max Marks</th>
            </tr>

          </thead>

          <tbody>

            {student.marks.map((mark, index) => (

              <tr
                key={index}
                className="border-b text-center"
              >
                <td className="p-3">{mark.subject}</td>
                <td className="p-3">{mark.marks}</td>
                <td className="p-3">{mark.max_marks}</td>
              </tr>

            ))}

          </tbody>

        </table>

        <div className="grid grid-cols-2 gap-6 mt-8">

          <div className="bg-gray-100 rounded-lg p-5">

            <p>Total Marks</p>

            <h2 className="text-3xl font-bold">
              {student.total}
            </h2>

          </div>

          <div className="bg-green-100 rounded-lg p-5">

            <p>Average</p>

            <h2 className="text-3xl font-bold">
              {student.average}
            </h2>

          </div>

        </div>

        <button
          className="mt-8 bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg"
          onClick={() =>
            navigate(`/student/${student.admission_no}/correct`)
          }
        >
          Correct Marks
        </button>

      </div>
    </div>
  );
}

export default StudentPage;