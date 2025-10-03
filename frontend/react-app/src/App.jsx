import React from 'react'
import { Routes, Route, Link } from 'react-router-dom'
import Home from './pages/Home'
import Services from './pages/Services'
import About from './pages/About'
import Login from './pages/Login'
import Contact from './pages/Contact'
import Therapists from './pages/Therapists'

export default function App() {
  return (
    <div>
      <nav className="navbar navbar-expand-lg navbar-dark bg-success">
        <div className="container">
          <Link className="navbar-brand" to="/">Toñín Masajes</Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainNav" aria-controls="mainNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="mainNav">
            <ul className="navbar-nav ms-auto mb-2 mb-lg-0">
              <li className="nav-item"><Link className="nav-link" to="/services">Servicios</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/masajistas">Masajistas</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/about">About</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/contact">Contáctanos</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/login">Sign In</Link></li>
            </ul>
          </div>
        </div>
      </nav>

      <main className="container my-4">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/services" element={<Services />} />
          <Route path="/about" element={<About />} />
          <Route path="/login" element={<Login />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/masajistas" element={<Therapists />} />
        </Routes>
      </main>

      <footer className="footer bg-light text-center py-3">© {new Date().getFullYear()} Toñín Masajes</footer>
    </div>
  )
}
