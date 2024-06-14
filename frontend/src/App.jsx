import react from "react"
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import Login from "./pages/Login"
import Register from "./pages/Register"
import Home from "./pages/Home"
import NotFound from "./pages/NotFound"
import ProtectedRoute from "./components/ProtectedRoute"

// logout and clear the stored token 
function logout() {
  localStorage.clear()
  return <Navigate to="/login" />
}

// When user registers it will clear the previous refresh token and won't through any error 
function RegisterAndLogut() {
  localStorage.clear()
  return <Navigate to="/register" />
}


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={
          <ProtectedRoute>
            <Home />
          </ProtectedRoute>
        } />
        <Route path="/login" element={<Login />} />
        <Route path="/Register" element={<RegisterAndLogut />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App


