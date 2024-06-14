import axios from "axios"
import { ACCESS_TOKEN } from "./constants"

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL // This will import from enironment variable file. Setting an base URL so that we don't need to type the whole thing again
})

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN)
        if (token){
            config.headers.Authorization = `Bearer ${token}` // This will add all the authorisation token automatically in all our request 
        }
        return config
    },
    (error) => {
        return Promise.reject(error)
    }
)

export default api