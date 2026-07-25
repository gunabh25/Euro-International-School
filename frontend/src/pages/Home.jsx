import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";
import SearchBar from "../components/SearchBar";
import StudentTable from "../components/StudentTable";

import api from "../services/api";

function Home() {
    const [students, setStudents] = useState([]);
    const [search, setSearch] = useState("");

    useEffect(() => {
        fetchStudents();
    }, [search]);

    const fetchStudents = async () => {
        try {
            const response = await api.get("/students/", {
                params: {
                    search,
                },
            });

            setStudents(response.data);
        } catch (err) {
            console.log(err);
        }
    };

    return (
        <>
            <Navbar />

            <div className="max-w-6xl mx-auto p-8">

                <SearchBar
                    value={search}
                    onChange={setSearch}
                />

                <StudentTable
                    students={students}
                />

            </div>
        </>
    );
}

export default Home;