import { useEffect, useState } from "react";

function App() { // `App` jest głównym komponentem aplikacji React. Zawiera logikę do zarządzania stanem, pobierania danych z backendu oraz renderowania interfejsu użytkownika.
    const [msg, setMsg] = useState("");
    const [title, setTitle] = useState("");
    const [content, setContent] = useState("");
    const [query, setQuery] = useState("");
    const [results, setResults] = useState([]);
    // auth removed — prosty frontend bez logowania

    useEffect(() => { // `useEffect` jest hookiem React, który pozwala na wykonywanie efektów ubocznych w komponentach funkcyjnych. 
        //W tym przypadku, jest używany do pobierania danych z backendu po pierwszym renderowaniu komponentu.
        fetch("http://localhost:8000/hello")
            .then((res) => res.json())
            .then((data) => setMsg(data.message))
            .catch((err) => console.log(err));
        fetchDocuments();
    }, []);

    function fetchDocuments() {
        fetch("http://localhost:8000/documents")
            .then((res) => res.json())
            .then((data) => setResults(data))
            .catch((err) => console.log(err));
    }

    function handleAdd(e) {
        e.preventDefault();
        if (!title.trim() || !content.trim()) {
            alert("Tytuł i treść nie mogą być puste");
            return;
        }
        fetch("http://localhost:8000/documents", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ title, content }),
        })
            .then((res) => res.json())
            .then((data) => {
                setTitle("");
                setContent("");
                fetchDocuments();
            })
            .catch((err) => console.log(err));
    }

    function handleSearch(e) {
        e.preventDefault();
        fetch(`http://localhost:8000/search?q=${encodeURIComponent(query)}`)
            .then((res) => res.json())
            .then((data) => setResults(data))
            .catch((err) => console.log(err));
    }

    function handleDeleteResults() {
        if (!query.trim()) {
            alert("Wprowadź zapytanie, aby usunąć pasujące dokumenty.");
            return;
        }
        if (!confirm(`Usunąć wszystkie dokumenty pasujące do: "${query}" ?`)) return;
        fetch(`http://localhost:8000/documents?q=${encodeURIComponent(query)}`, { method: "DELETE" })
            .then((res) => res.json())
            .then((data) => {
                alert(`Usunięto ${data.deleted} dokumentów`);
                setQuery("");
                fetchDocuments();
            })
            .catch((err) => console.log(err));
    }


    return (
        <div className="container">
            <header className="header">
                <h1>Baza dokumentów i notatek</h1>
                <p className="sub"></p>
            </header>

            <main className="main">
                <section className="card">
                    <h2>Stwórz dokument / notatkę</h2>
                    <form className="form" onSubmit={handleAdd}>
                        <input className="input" placeholder="Tytuł" value={title} onChange={(e) => setTitle(e.target.value)} />
                        <textarea className="textarea" placeholder="Treść" value={content} onChange={(e) => setContent(e.target.value)} />
                        <div className="actions">
                            <button className="btn primary" type="submit">Dodaj</button>
                        </div>
                    </form>
                </section>



                <section className="card">
                    <h2>Wyszukaj</h2>
                    <form className="form-inline" onSubmit={handleSearch}>
                        <input className="input" placeholder="Szukaj..." value={query} onChange={(e) => setQuery(e.target.value)} />
                        <button className="btn" type="submit">Szukaj</button>
                        <button className="btn danger" type="button" onClick={handleDeleteResults}>
                            Usuń wyniki wyszukiwania
                        </button>
                    </form>

                    <h2>Wyniki</h2>
                    <ul className="results">
                        {results.map((r) => (
                            <li className="result-item" key={r.id}>
                                <div className="result-header">
                                    <strong className="result-title">{r.title}</strong>
                                </div>
                                <p className="result-content">{r.content}</p>
                            </li>
                        ))}
                    </ul>
                </section>

                <section className="card">

                </section>
            </main>
        </div>
    );
}

export default App;
