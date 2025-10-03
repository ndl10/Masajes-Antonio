import React, { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'

export default function TherapistDetail() {
  const { id } = useParams()
  const [therapist, setTherapist] = useState(null)
  const [services, setServices] = useState([])

  useEffect(() => {
    // Fetch del masajista
    fetch(`/api/therapists/${id}`)
      .then(r => r.json())
      .then(setTherapist)
      .catch(console.error)

    // Fetch de los servicios que ofrece este masajista
    fetch(`/api/therapists/${id}/services`)
      .then(r => r.json())
      .then(setServices)
      .catch(console.error)
  }, [id])

  if (!therapist) return <p>Cargando masajista...</p>

  return (
    <div>
      <h1>{therapist.name}</h1>
      <p>Especialidad: {therapist.specialty}</p>

      <h3>Servicios que ofrece</h3>
      <div className="row g-3">
        {services.map(s => (
          <div className="col-md-4" key={s.id}>
            <div className="card h-100">
              <div className="card-body">
                <h5 className="card-title">{s.name}</h5>
                <p className="card-text">{s.description}</p>
                <Link to={`/services/${s.id}`} className="btn btn-sm btn-primary">Ver detalles</Link>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
