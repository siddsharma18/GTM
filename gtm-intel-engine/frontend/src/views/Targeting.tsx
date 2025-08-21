import AccountTable from '../components/AccountTable'
import AccountDetail from '../components/AccountDetail'
import { useEffect, useState } from 'react'
import { getTopAccounts } from '../lib/api'

export default function Targeting(){
  const [accounts, setAccounts] = useState<any[]>([])
  const [selected, setSelected] = useState<any | null>(null)
  useEffect(()=>{ getTopAccounts().then((r)=> setAccounts(r.accounts)) },[])
  return (
    <div className="space-y-5">
      <div className="rounded-xl border border-white/10 bg-slate-900/60 text-slate-100 p-4">
        <div className="text-sm mb-2 opacity-80">Enhanced Targeting</div>
        <AccountTable accounts={accounts} onSelect={setSelected} />
      </div>
      {selected && (
        <div className="rounded-xl border border-white/10 bg-slate-900/60 text-slate-100 p-4">
          <AccountDetail account={selected} />
        </div>
      )}
    </div>
  )
}
