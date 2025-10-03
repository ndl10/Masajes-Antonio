import React, { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'

export default function ServiceDetail() {
  const { id } = useParams()
  const [service, setService] = useState(null)
  const [therapists, setTherapists] = useState([])

  useEffect(() => {
    // Fetch del servicio
    fetch(`/api/services/${id}`)
      .then(r => r.json())
      .then(setService)
      .catch(console.error)

    // Fetch de los masajistas que ofrecen este servicio
    fetch(`/api/services/${id}/therapists`)
      .then(r => r.json())
      .then(setTherapists)
      .catch(console.error)
  }, [id])

  if (!service) return <p>Cargando servicio...</p>

  return (
    <div>
      <h1>{service.name}</h1>
      <p>{service.description}</p>
      <p className="text-muted">Precio: {service.price}€ · Duración: {service.duration}min</p>

      <h3>Masajistas que ofrecen este servicio</h3>
      <div className="row g-3">
        {therapists.map(t => (
          <div className="col-md-4" key={t.id}>
            <div className="card h-100">
              <div className="card-body">
                <h5 className="card-title">{t.name}</h5>
                <p className="card-text">{t.specialty}</p>
                <Link to={`/therapists/${t.id}`} className="btn btn-sm btn-primary">Ver detalles</Link>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
