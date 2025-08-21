import { useState } from 'react'

export default function AccountTable({ accounts, onSelect }: { accounts: any[]; onSelect: (a: any) => void }) {
  const [q, setQ] = useState('')
  const [asc, setAsc] = useState(false)
  const filtered = accounts.filter(a => (a.domain || '').includes(q))
  const sorted = [...filtered].sort((a,b)=> asc ? a.total_score - b.total_score : b.total_score - a.total_score)

  return (
    <div>
      <div className="flex items-center gap-2 mb-2">
        <input
          value={q}
          onChange={e=>setQ(e.target.value)}
          placeholder="Search domain"
          className="border border-white/40 bg-white/70 backdrop-blur px-3 py-2 text-sm rounded"
        />
        <button onClick={()=>setAsc(!asc)} className="text-xs px-3 py-1.5 border border-white/40 rounded bg-white/70 backdrop-blur">
          Sort {asc ? '↑' : '↓'}
        </button>
      </div>
      <table className="w-full text-left border border-white/40 backdrop-blur bg-white/60 rounded-xl overflow-hidden">
        <thead>
          <tr>
            <th className="p-3 border-b">Domain</th>
            <th className="p-3 border-b">Total Score</th>
          </tr>
        </thead>
        <tbody>
          {sorted.map((a) => (
            <tr key={a.id} className="hover:bg-gray-50 cursor-pointer" onClick={() => onSelect(a)}>
              <td className="p-3 border-b">{a.domain}</td>
              <td className="p-3 border-b">{a.total_score}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
