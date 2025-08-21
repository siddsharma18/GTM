import { useEffect, useState } from 'react'
import { getOutreach, postOutreach } from '../lib/api'

export default function Messaging(){
  const [accountId] = useState(1)
  const [channel, setChannel] = useState<'email'|'linkedin'|'call'|'video'>('email')
  const [variants, setVariants] = useState<any[]>([])
  const [loading, setLoading] = useState(false)

  useEffect(()=>{ getOutreach(accountId).then(r=> setVariants(r.variants)) },[accountId])

  async function regenerate(){
    setLoading(true)
    const r = await postOutreach(accountId, channel)
    setVariants(r.variants)
    setLoading(false)
  }

  return (
    <div className="space-y-4">
      <div className="flex gap-2">
        {(['email','linkedin','call','video'] as const).map(c => (
          <button key={c} onClick={()=> setChannel(c)} className={`text-xs px-3 py-1.5 border rounded ${channel===c ? 'bg-cyan-500/20 border-cyan-400/30' : 'border-white/10 bg-white/5'}`}>{c}</button>
        ))}
        <button onClick={regenerate} disabled={loading} className="text-xs px-3 py-1.5 border rounded border-white/10 bg-white/5">{loading?'...':'Regenerate'}</button>
      </div>
      <div className="grid grid-cols-1 gap-3">
        {variants.map((v,i)=> (
          <div key={i} className="rounded-xl border border-white/10 bg-white/5 p-4">
            <div className="text-xs opacity-70 mb-1">{channel.toUpperCase()}</div>
            {v.subject && <div className="text-sm font-medium mb-2">{v.subject}</div>}
            <pre className="whitespace-pre-wrap text-sm">{v.body}</pre>
          </div>
        ))}
      </div>
    </div>
  )
}
