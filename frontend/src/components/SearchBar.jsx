function SearchBar({ value, onChange }) {
    return (
        <input
            type="text"
            placeholder="Search student..."
            value={value}
            onChange={(e) => onChange(e.target.value)}
            className="w-full border rounded-lg p-3 mb-6"
        />
    );
}

export default SearchBar;