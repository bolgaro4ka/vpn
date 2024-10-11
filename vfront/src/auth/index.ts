import axios from 'axios'
import {type User} from './interface'
import { USER_URL } from '@/config/main'


export function auth(user : User) {
   
    
    localStorage.setItem('first_name', user.first_name)
    localStorage.setItem('last_name', user.last_name)
    localStorage.setItem('username', user.username)
    localStorage.setItem('email', user.email)
    localStorage.setItem('phone', user.tel)
    localStorage.setItem('jwt', user.access)
    localStorage.setItem('refresh', user.refresh)
    localStorage.setItem('middle_name', user?.middle_name)
    localStorage.setItem('id', user.id)

}

export async function getMe(token : string) {
    const res = await axios.get(USER_URL, {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    }).then((res) => {
        return res.data
    }).catch((err) => {
        console.log(err)
    })

    console.log(res)
    return res
}