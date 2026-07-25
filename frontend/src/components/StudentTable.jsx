import { useNavigate } from "react-router-dom";

function StudentTable({ students }) {
    const navigate = useNavigate();

    return (
        <table className="w-full border-collapse">
            <thead>
                <tr className="bg-blue-600 text-white">
                    <th className="p-3">Admission</th>
                    <th>Name</th>
                    <th>Class</th>
                    <th>Section</th>
                    <th>Average</th>
                </tr>
            </thead>

            <tbody>
                {students.map((student) => (
                    <tr
                        key={student.admission_no}
                        onClick={() =>
                            navigate(`/student/${student.admission_no}`)
                        }
                        className="cursor-pointer hover:bg-gray-100 border-b"
                    >
                        <td className="p-3">{student.admission_no}</td>
                        <td>{student.name}</td>
                        <td>{student.student_class}</td>
                        <td>{student.section}</td>
                        <td>{student.average}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
}

export default StudentTable;