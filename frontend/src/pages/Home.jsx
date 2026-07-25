import Navbar from "../components/Navbar";

function Home() {
    return (
        <>
            <Navbar />

            <div className="max-w-6xl mx-auto p-8">
                <h2 className="text-2xl font-bold">
                    Student List
                </h2>
            </div>
        </>
    );
}

export default Home;