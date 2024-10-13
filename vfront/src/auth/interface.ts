export interface User {
    username: string;
    password: string;
    refresh: string;
    access: string;
    last_name: string;
    first_name: string;
    middle_name: string;
    email: string;
    tel: string;
    id: string;
    wallet: number;
    paid: boolean;
    paid_date: any;
    paid_next_date?: any;
    tariff?: any;
}