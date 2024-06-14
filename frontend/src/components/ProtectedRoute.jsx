import { Navigate } from "react-router-dom"
import { jwtDecode } from "jwt-decode"
import api from "../api"
import { REFRESH_TOKEN, ACCESS_TOKEN } from "../constants"
import { useState, useEffect } from "react"

// This function will create. It acts as a wrapper function
function ProtectedRoute({ children }) {
    const [isAuthorized, SetIsAuthorized] = useState(null)

    // When the access token is expired, it will take some time to check. If we are unauthorized then it will navigate back to login page
    useEffect(() => {
        auth().catch(() => SetIsAuthorized(false))
    }, [])

    // This function will get the refresh token. Implemented try catch to check if any error occurs than it will display the error message 
    const refreshToken = async () => {
        const refreshToken = localStorage.getItem(REFRESH_TOKEN)
        try {
            const res = await api.post("/api/token/refresh/", { // It will fetch the refresh token
                refresh: refreshToken,
            });
            if (res.status == 200) { // Checking if the refresh token is valid 
                localStorage.setItem(ACCESS_TOKEN, res.data.access) // Setting the updated access token to the ACCESS_TOKEN varible 
                SetisAuthorized(true)
            } else {
                SetisAuthorized(false)
            }
        } catch (error) {
            console.log(error)
            SetisAuthorized(false)
        }
    }

    // This will get the access token and check wether it's a valid token or not
    const auth = async () => {
        const token = localStorage.getItem(ACCESS_TOKEN)
        if (!token) {
            SetisAuthorized(false)
            return
        }
        const decoded = jwtDecode(token) // using jwtDecode it will decode the token
        const tokenExpiration = decoded.exp
        const now = Date.now() / 1000 // To get the time in seconds and not in milliseconds

        // checking is the authorisation token is valid 
        if (tokenExpiration < now) {
            await refreshToken()
        } else {
            isAuthorized(true)
        }
    }

    // It checks wether the user is authorized and navigates it to the login page 
    if (isAuthorized === null) {
        return <div>Loading...</div>
    }

    return isAuthorized ? children : <Navigate to="/login" />
}

export default ProtectedRoute