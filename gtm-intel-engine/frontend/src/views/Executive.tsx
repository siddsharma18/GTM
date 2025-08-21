export default function Executive() {
  return (
    <div className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {[
          {label:'Pipeline Value', value:'$2.4M', delta:'+67%'},
          {label:'Response Rate', value:'14.9%', delta:'+34%'},
          {label:'Conversion Rate', value:'18.5%', delta:'+18%'},
        ].map((k,i)=> (
          <div key={i} className="rounded-xl border border-white/10 bg-slate-900/60 text-slate-100 p-5">
            <div className="text-xs uppercase opacity-70">{k.label}</div>
            <div className="text-3xl font-semibold mt-2">{k.value}</div>
            <div className="text-xs mt-1 text-emerald-400">{k.delta}</div>
          </div>
        ))}
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="rounded-xl border border-white/10 bg-slate-900/60 text-slate-100 p-5 min-h-[220px]">
          <div className="text-sm mb-3 opacity-80">Campaign Performance Trends</div>
          <svg viewBox="0 0 100 40" className="w-full h-40">
            <polyline fill="none" stroke="#22d3ee" strokeWidth="2" points="0,30 20,28 40,24 60,20 80,18 100,16" />
            <polyline fill="none" stroke="#f59e0b" strokeWidth="2" points="0,34 20,30 40,26 60,22 80,20 100,18" />
          </svg>
        </div>
        <div className="rounded-xl border border-white/10 bg-slate-900/60 text-slate-100 p-5 min-h-[220px]">
          <div className="text-sm mb-3 opacity-80">Channel ROI Comparison</div>
          <div className="grid grid-cols-3 gap-4 items-end h-40">
            {['Email','LinkedIn','Video'].map((c,i)=> (
              <div key={i} className="text-center">
                <div className="mx-auto w-10 bg-cyan-400/70" style={{height: `${40 + i*20}px`}}></div>
                <div className="text-xs mt-2 opacity-80">{c}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}
