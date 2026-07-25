import { useEffect, useState } from "react";
import api from "../api/api";

export default function Home() {
    const [students, setStudents] = useState([]);

    useEffect(() => {
        loadStudents();
    }, []);

    async function loadStudents(search = "") {
        try {
            const response = await api.get(
                `/students/?search=${search}`
            );

            setStudents(response.data);
        } catch (error) {
            console.error(error);
        }
    }

    return (
        <div className="min-h-screen bg-gray-100">

            <div className="max-w-7xl mx-auto p-10">

                <h1 className="text-4xl font-bold mb-8">
                    Euro International School
                </h1>

                <input
                    type="text"
                    placeholder="Search student..."
                    className="w-full border rounded-lg p-3 mb-8"
                    onChange={(e) => loadStudents(e.target.value)}
                />

                <table className="w-full bg-white rounded-lg shadow">

                    <thead className="bg-blue-600 text-white">

                        <tr>

                            <th className="p-3">Admission</th>

                            <th>Name</th>

                            <th>Class</th>

                            <th>Section</th>

                            <th>Average</th>

                        </tr>

                    </thead>

                    <tbody>

                        {students.map(student => (

                            <tr
                                key={student.admission_no}
                                className="border-b hover:bg-gray-50"
                            >

                                <td className="p-3">
                                    {student.admission_no}
                                </td>

                                <td>{student.name}</td>

                                <td>{student.student_class}</td>

                                <td>{student.section}</td>

                                <td>{student.average}</td>

                            </tr>

                        ))}

                    </tbody>

                </table>

            </div>

        </div>
    );
}