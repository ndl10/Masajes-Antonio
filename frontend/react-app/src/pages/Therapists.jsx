import React, { useEffect, useState } from 'react'
import TherapistCard from '../components/TherapistCard'

export default function Therapists() {
  const [therapists, setTherapists] = useState([])

  useEffect(() => {
    fetch('/api/therapists')
      .then(r => r.json())
      .then(setTherapists)
      .catch(console.error)
  }, [])

  return (
    <div>
      <h1>Masajistas</h1>
      <div className="row">
        {therapists.map(t => <TherapistCard key={t.id} therapist={t} />)}
      </div>
    </div>
  )
}
