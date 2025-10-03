// src/context/AuthContext.jsx
import React, { createContext, useState, useEffect } from 'react'

export const AuthContext = createContext()

export default function AuthProvider({ children }) {
  const [user, setUser] = useState(null)

  // Cargar token de localStorage al iniciar
  useEffect(() => {
    const token = localStorage.getItem('token')
    const role = localStorage.getItem('role')
    if (token && role) {
      setUser({ token, role })
    }
  }, [])

  const login = (token, role) => {
    localStorage.setItem('token', token)
    localStorage.setItem('role', role)
    setUser({ token, role })
  }

  const logout = () => {
    localStorage.removeItem('token')
    localStorage.removeItem('role')
    setUser(null)
  }

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  )
}
