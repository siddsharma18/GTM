import { useState } from 'react'
import { runAlerts } from '../lib/api'

export default function Delivery(){
  const [sending, setSending] = useState(false)
  const [result, setResult] = useState<any|null>(null)

  async function trigger(){
    setSending(true)
    const r = await runAlerts()
    setResult(r)
    setSending(false)
  }

  return (
    <div className="space-y-4">
      <div className="rounded-xl border border-white/10 bg-slate-900/60 text-slate-100 p-5">
        <div className="text-sm opacity-80 mb-2">Multi-Channel Delivery</div>
        <div className="flex items-center gap-3 mb-3">
          <button onClick={trigger} disabled={sending} className="text-xs px-3 py-1.5 border rounded border-white/10 bg-white/5">{sending?'...':'Send Alerts (Demo)'}</button>
          {result && <span className="text-xs opacity-80">Alert sent</span>}
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {[{name:'Q4 SaaS Leadership Outreach', ch:['Email','LinkedIn','Video']}, {name:'FinTech Executive Engagement', ch:['Email','LinkedIn']}].map((c,i)=> (
            <div key={i} className="rounded-lg border border-white/10 bg-white/5 p-4">
              <div className="font-medium mb-2">{c.name}</div>
              <div className="flex gap-2 mb-3">{c.ch.map((x,j)=> <span key={j} className="text-xs px-2 py-1 rounded bg-white/10 border border-white/10">{x}</span>)}</div>
              <div className="text-xs opacity-70">Response: {9+i*6}.0% · Meetings: {18+i*5}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
