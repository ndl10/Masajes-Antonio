import React, { useEffect, useState } from 'react'
import ServiceCard from '../components/ServiceCard'

export default function Services() {
  const [services, setServices] = useState([])

  useEffect(() => {
    fetch('/api/services')
      .then(r => r.json())
      .then(setServices)
      .catch(console.error)
  }, [])

  return (
    <div>
      <h1>Servicios</h1>
      <div className="row">
        {services.map(s => <ServiceCard key={s.id} service={s} />)}
      </div>
    </div>
  )
}
