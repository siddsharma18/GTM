import { useEffect, useState } from 'react'
import { getSignals, getOutreach, getScore, postOutreach } from '../lib/api'
import InsightChips from './InsightChips'
import OutreachPreview from './OutreachPreview'
import ScoreBreakdown from './ScoreBreakdown'

export default function AccountDetail({ account }: { account: any }) {
  const [signals, setSignals] = useState<any[]>([])
  const [outreach, setOutreach] = useState<any[]>([])
  const [channel, setChannel] = useState<'email'|'linkedin'|'call'|'video'>('email')
  const [loading, setLoading] = useState(false)
  const [score, setScore] = useState<any | null>(null)
  const [tab, setTab] = useState<'signals'|'outreach'|'score'>('signals')

  useEffect(() => {
    getSignals(account.id).then((r) => setSignals(r.signals))
    getOutreach(account.id).then((r) => setOutreach(r.variants))
    getScore(account.id).then((r)=> setScore(r))
  }, [account.id])

  return (
    <div className="mt-6">
      <div className="flex gap-3 border-b mb-4">
        <button className={tab==='signals' ? 'font-semibold' : ''} onClick={() => setTab('signals')}>Signals</button>
        <button className={tab==='outreach' ? 'font-semibold' : ''} onClick={() => setTab('outreach')}>Outreach</button>
        <button className={tab==='score' ? 'font-semibold' : ''} onClick={() => setTab('score')}>Score</button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Signals column */}
        <div className={tab==='signals' ? '' : 'hidden'}>
          <h2 className="font-semibold mb-2">Signals</h2>
          <InsightChips signals={signals} />
          <div className="mt-3 space-y-2">
            {signals.map((s, i) => (
              <div key={i} className="border border-white/40 bg-white/60 backdrop-blur p-3 rounded">
                <div className="text-sm font-medium">{s.title} (sev {s.severity})</div>
                <div className="text-xs text-gray-600/90">{s.description}</div>
              </div>
            ))}
          </div>
        </div>

        {/* Outreach + Score column */}
        <div className={tab!=='signals' ? '' : 'hidden'}>
          {/* Outreach */}
          <div className={tab==='outreach' ? '' : 'hidden'}>
            <div className="flex items-center justify-between">
              <h2 className="font-semibold mb-2">Outreach</h2>
              <div className="flex gap-2">
                {(['email','linkedin','call','video'] as const).map(c => (
                  <button
                    key={c}
                    onClick={() => setChannel(c)}
                    className={`text-xs px-2 py-1 border rounded ${channel===c ? 'bg-gray-900 text-white' : ''}`}
                  >
                    {c}
                  </button>
                ))}
                <button
                  disabled={loading}
                  onClick={async ()=>{
                    setLoading(true)
                    const r = await postOutreach(account.id, channel)
                    setOutreach(r.variants)
                    setLoading(false)
                  }}
                  className="text-xs px-3 py-1.5 border border-white/40 rounded bg-white/70 backdrop-blur"
                >
                  {loading?'...':'Regenerate'}
                </button>
              </div>
            </div>
            <OutreachPreview variants={outreach} />
          </div>

          {/* Score */}
          <div className={tab==='score' ? '' : 'hidden'}>
            <h2 className="font-semibold mb-2">Score Breakdown</h2>
            <ScoreBreakdown score={score} />
          </div>
        </div>
      </div>
    </div>
  )
}
