import React from 'react'

export default function Login() {
  return (
    <div className="col-md-6 mx-auto">
      <h1>Sign In</h1>
      <form>
        <div className="mb-3">
          <label className="form-label">Email</label>
          <input className="form-control" type="email" name="email" />
        </div>
        <div className="mb-3">
          <label className="form-label">Password</label>
          <input className="form-control" type="password" name="password" />
        </div>
        <button className="btn btn-success">Iniciar sesión</button>
      </form>
    </div>
  )
}
