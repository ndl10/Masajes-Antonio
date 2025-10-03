import React from 'react'
import { useNavigate } from 'react-router-dom'

export default function ServiceCard({ service }) {
  const navigate = useNavigate()

  return (
    <div className="col-md-4 mb-3">
      <div className="card h-100" onClick={() => navigate(`/services/${service.id}`)} style={{cursor:'pointer'}}>
        {service.image && <img src={service.image} className="card-img-top" alt={service.name} />}
        <div className="card-body">
          <h5 className="card-title">{service.name}</h5>
          <p className="card-text">{service.description}</p>
          <p className="text-muted">Precio: {service.price}€ · Duración: {service.duration}min</p>
        </div>
      </div>
    </div>
  )
}
