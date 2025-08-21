import axios from 'axios'

const API = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export async function getTopAccounts() {
	const { data } = await axios.get(`${API}/score/top`)
	return data
}

export async function getSignals(accountId: number) {
	const { data } = await axios.get(`${API}/signals/${accountId}`)
	return data
}

export async function getOutreach(accountId: number) {
	const { data } = await axios.get(`${API}/outreach/${accountId}`)
	return data
}

export async function getScore(accountId: number) {
	const { data } = await axios.get(`${API}/score/${accountId}`)
	return data
}

export async function postOutreach(accountId: number, channel: string){
	const { data } = await axios.post(`${API}/outreach/${accountId}?channel=${channel}`)
	return data
}

export async function getAccounts(){
	const { data } = await axios.get(`${API}/accounts`)
	return data
}

export async function runAlerts(){
	const { data } = await axios.post(`${API}/alerts/run`)
	return data
}
