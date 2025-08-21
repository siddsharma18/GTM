import { useState } from 'react'
import Executive from './views/Executive'
import Targeting from './views/Targeting'
import Messaging from './views/Messaging'
import Delivery from './views/Delivery'

export default function App(){
  const [tab, setTab] = useState<'exec'|'target'|'msg'|'delivery'>('target')
  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-900 to-slate-800 text-slate-100 p-8">
      <div className="max-w-6xl mx-auto">
        <div className="flex items-center justify-between mb-6">
          <div className="text-xl font-semibold">GTM Intel Engine</div>
          <span className="text-xs px-2 py-1 rounded bg-emerald-500/15 text-emerald-300 border border-emerald-400/20">healthy</span>
        </div>
        <div className="flex gap-2 mb-6">
          <button onClick={()=>setTab('exec')} className={`px-3 py-1.5 text-sm rounded border ${tab==='exec'?'bg-cyan-500/20 border-cyan-400/30':'border-white/10 bg-white/5'}`}>Executive</button>
          <button onClick={()=>setTab('target')} className={`px-3 py-1.5 text-sm rounded border ${tab==='target'?'bg-cyan-500/20 border-cyan-400/30':'border-white/10 bg-white/5'}`}>Enhanced Targeting</button>
          <button onClick={()=>setTab('msg')} className={`px-3 py-1.5 text-sm rounded border ${tab==='msg'?'bg-cyan-500/20 border-cyan-400/30':'border-white/10 bg-white/5'}`}>AI Messaging Engine</button>
          <button onClick={()=>setTab('delivery')} className={`px-3 py-1.5 text-sm rounded border ${tab==='delivery'?'bg-cyan-500/20 border-cyan-400/30':'border-white/10 bg-white/5'}`}>Multi-Channel Delivery</button>
        </div>
        {tab==='exec' && <Executive />}
        {tab==='target' && <Targeting />}
        {tab==='msg' && <Messaging />}
        {tab==='delivery' && <Delivery />}
      </div>
    </div>
  )
}
