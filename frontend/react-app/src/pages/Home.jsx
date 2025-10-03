import React from 'react'

export default function Home() {
  return (
    <div className="text-center">
      <h1 className="display-5">Bienvenido a Toñín Masajes</h1>
      <p className="lead">Centro de masajes — reserva tus servicios y relájate.</p>
      <div className="card mx-auto" style={{maxWidth:800}}>
        <div className="card-body">
          <h5 className="card-title">Relájate y recupérate</h5>
          <p className="card-text">Explora nuestros servicios o conoce a nuestros masajistas.</p>
        </div>
      </div>
    </div>
  )
}
