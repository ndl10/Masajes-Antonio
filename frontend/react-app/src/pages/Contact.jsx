import React from 'react'

export default function Contact() {
  return (
    <div className="col-md-8 mx-auto">
      <h1>Contáctanos</h1>
      <p className="text-muted">Escríbenos por email o llámanos para reservar o preguntar por disponibilidad.</p>
      <form>
        <div className="mb-3">
          <label className="form-label">Nombre</label>
          <input className="form-control" type="text" name="name" />
        </div>
        <div className="mb-3">
          <label className="form-label">Email</label>
          <input className="form-control" type="email" name="email" />
        </div>
        <div className="mb-3">
          <label className="form-label">Mensaje</label>
          <textarea className="form-control" name="message" rows="4" />
        </div>
        <button className="btn btn-success">Enviar</button>
      </form>
    </div>
  )
}
