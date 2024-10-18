import axios from 'axios'
import {type User} from './interface'
import { USER_URL, CHANGET_URL } from '@/config/main'


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
        return false
    })
    return res
}

export function logout() {
    localStorage.clear()
}

export async function changeTariff(e: MouseEvent, tariff: any, mof: number) {
    e.preventDefault()
    console.log(mof)
    const res = await axios.post(CHANGET_URL,
    {
        tariff: tariff.id,
        number_of_files: mof
    }).then((res) => {
        return res.data
    }).catch((err) => {
        alert('Вы уже оплатили другой тариф. Переключение не удалось.')
        return false
    })
    
}