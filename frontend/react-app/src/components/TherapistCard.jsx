import React from 'react'
import { useNavigate } from 'react-router-dom'

export default function TherapistCard({ therapist }) {
  const navigate = useNavigate()

  return (
    <div className="col-md-4 mb-3">
      <div className="card h-100" onClick={() => navigate(`/therapists/${therapist.id}`)} style={{cursor:'pointer'}}>
        {therapist.image && <img src={therapist.image} className="card-img-top" alt={therapist.name} />}
        <div className="card-body">
          <h5 className="card-title">{therapist.name}</h5>
          <p className="card-text">Especialidad: {therapist.specialty}</p>
        </div>
      </div>
    </div>
  )
}
